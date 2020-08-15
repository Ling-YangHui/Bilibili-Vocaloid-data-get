# encoding: utf-8
import urllib.request
from urllib.parse import quote
import datetime
import json
import string
import time
import math
import os
import threading
from threading import Thread,Lock
import seaborn as sns
from scipy.stats import norm
import matplotlib.pyplot as plt
import sys
import numpy as np

#全局变量区域
#在以后的维护中，请尽量少使用全局变量
lock = threading.Lock() #线程互斥
timeSleep = [0.1,0.15]

class mainRun():
    #在以后的维护中，请尽量少使用全局变量
    def __init__(self):
        super().__init__()
        self.lock = threading.Lock() #线程互斥
        self.timeSleep = [0.1,0.15]
        self.numGet = 0

    class VOCALS_DATA_ANALYSIS():
        #数据分析方法
        def __init__(self):
            self.singerList = [[] for i in range(15)]

        def addData(self,singerID,view):
            self.singerList[singerID].append(view)

        def writeVocalList(self):
            vocalList = [u'洛天依',u'言和',u'乐正绫',u'乐正龙牙',u'徵羽摩柯',u'墨清弦',u'星尘',u'心华',u'初音未来',u'海伊',u'苍穹',u'诗岸',u'赤羽',u'牧心',u'艾可'] #纵向表头
            fieldList = [u'歌姬',u'投稿数',u'过千数',u'过万数',u'殿堂数',u'p-90 %',u'p-95 %',u'p-97.5 %',u'最大数',u'总和']#横向表头
            txt = ''
            for i in range(len(fieldList)):
                txt += fieldList[i] + ','
            txt += '\n'
            for id in range(len(vocalList)):#id指歌姬序号
                npArray = np.asarray(self.singerList[id])#根据Python自带的list创建一个np里的array
                currentLine = ''
                currentLine += vocalList[id] + ',' #歌姬
                currentLine += str(np.sum(npArray >= 0)) + ',' #投稿
                currentLine += str(np.sum(npArray >= 1000)) + ',' #过千数
                currentLine += str(np.sum(npArray >= 10000)) + ',' #过万数
                currentLine += str(np.sum(npArray >= 100000)) + ',' #殿堂数
                currentLine += str(np.percentile(npArray,90)) + ','
                currentLine += str(np.percentile(npArray,95)) + ','
                currentLine += str(np.percentile(npArray,97.5)) + ','
                currentLine += str(np.amax(npArray)) + ','
                currentLine += str(np.sum(npArray)) + ','
                txt += currentLine + '\n'
            return txt

        def writeEnginesSheet(self):
            engineList = [u'中文VOCALOID',u'中文Synthesizer V',u'整体'] #纵向表头
            fieldList = [u'引擎',u'投稿数',u'过千数',u'过万数',u'殿堂数',u'p-90 %',u'p-95 %',u'p-97.5 %',u'最大值',u'总和']#横向表头

            txt = ''
            for i in range(len(fieldList)):
                txt += fieldList[i] + ','
            txt += '\n'
            for id in range(len(engineList)):#id指引擎序号
                array = []
                if id == 0:
                    for i in range(9):
                        array += self.singerList[i]
                elif id == 1:
                    for i in range(9,15):
                        array += self.singerList[i]
                else:
                    for i in range(15):
                        array += self.singerList[i]
                
                npArray = np.asarray(array)
                currentLine = ''
                currentLine += engineList[id] + ','
                currentLine += str(np.sum(npArray >= 0)) + ','
                currentLine += str(np.sum(npArray >= 1000)) + ','
                currentLine += str(np.sum(npArray >= 10000)) + ','
                currentLine += str(np.sum(npArray >= 100000)) + ','
                currentLine += str(np.percentile(npArray,90)) + ','
                currentLine += str(np.percentile(npArray,95)) + ','
                currentLine += str(np.percentile(npArray,97.5)) + ','
                currentLine += str(np.amax(npArray)) + ','
                currentLine += str(np.sum(npArray)) + ','
                txt += currentLine + '\n'

            return txt

    class HASHLIST():
        #哈希表类
        def __init__(self):
            self.list = [[]for i in range(0,50000)]
            self.hashMod = 49999

        def hashFunction(self,aid):
            return int(aid) % self.hashMod

        def insertList(self,aid):
            hashCode = self.hashFunction(aid)
            self.list[hashCode].append(aid)
            return

        def findList(self,aid):
            hashCode = self.hashFunction(aid)
            for i in self.list[hashCode]:
                if i == aid:
                    return 0
            return 1

    class VIDEO():
        def __init__(self,mark):
            self.keyword = mark

    def isJapanese(self,string):
        string = string.replace('初音ミク','')
        featureWords = ['日语','日本语','日文','日本語',
                        'あ','い','う','え','お','か','き','く','け','こ','ま','み','む','め','も',
                        'さ','し','す','せ','そ','は','ひ','ふ','へ','ほ','な','に','ぬ','ね','の',
                        'ぱ','ぴ','ぷ','ぺ','ぽ','ら','り','る','れ','ろ','ば','び','ぶ','べ','ぼ',
                        'わ','を','ん','た','つ','て','と',
                        'ア','イ','ウ','エ','オ','カ','キ','ク','ケ','コ','マ','ミ','ム','メ','モ', 
                        'サ','シ','ス','セ','ソ','ハ','ヒ','フ','ヘ','ホ','ナ','ニ','ヌ','ネ','ノ', 
                        'パ','ピ','プ','ペ','ポ','ラ','リ','ル','レ','ロ','バ','ビ','ブ','ベ','ボ', 
                        'ワ','ヲ','ン','タ','ツ','テ','ト',
                        ]

        for word in featureWords:
            if string.count(word) >= 1:
                return True
        return False

    def getTime(self,deltaTime):
        #将B站使用的Unix时间戳，转换为Excel能够识别的Excel时间
        startTime = 25569
        endTime = startTime + int(deltaTime)/24.0/3600 + 1/3
        return (str(endTime))

    def getVideoList(self,hashList,keyword,page,startDate,endDate,paraMeterList,viewList,fileTxt,vocalsDataAnalysis):
        #变量paraMeterList：【日期截至位，信息获取条数位】
        if paraMeterList[0] == 1:
            return

        #拼接url
        url = '''https://api.bilibili.com/x/web-interface/search/type?search_type=video&keyword='''
        url = url + quote(keyword,safe=string.printable) + '''&page=''' + str(page) + '''&order=pubdate&tids=30'''
        
        #获得一长串文本
        txt = urllib.request.urlopen(url).read() 
        web = txt.decode('utf-8','ignore')
        
        #以下四行用于去除这一长串文本中“没有意义”的内容。注意到都是替换''（空文本
        web = web.replace('''\\u003c''','')
        web = web.replace('''\\u003e''','')
        web = web.replace('''em class=\\"keyword\\"''','')
        web = web.replace('''/em''','')

        #json转化为字典格�?
        jsonDate = json.loads(web)

        subWeb = web.split('''},{''')#将一长串文本分割检测份数
        if(len(subWeb) < 20):#如果不足20份，及时中止
            print ('''【getVidioList】查询API失败''')
            return
        
        #拼接输入的字符串
        resultTxt =''
        for i in range(20):#对于20份，每一份获取数据
            
            video = self.VIDEO(keyword)
            videoDate = jsonDate['data']['result'][i]
            videoDate['pubdate'] = self.getTime(videoDate['pubdate'])
            videoDate['senddate'] = self.getTime(videoDate['senddate'])

            #判断中断条件：查重和时间截止，注意线程上锁和解锁
            self.lock.acquire()
            if hashList.findList(videoDate.get('aid')) == 0:
                self.lock.release()
                continue
            else:
                hashList.insertList(videoDate.get('aid'))
            if int(float(videoDate.get('pubdate'))) < int(float(startDate)): 
                self.lock.release()
                paraMeterList[0] = 1
                break
            if int(float(videoDate.get('pubdate'))) > int(float(endDate)):
                self.lock.release()
                continue
            self.lock.release()

            #获取字典中各项数值，加入到video类中
            video.title = '"' + videoDate['title'] + '"'
            video.author = '"' + videoDate['author'] + '"'
            video.typename = '"' + videoDate['typename'] + '"'
            video.tag = '"' + videoDate['tag'] + '"'
            video.senddate = str(videoDate['senddate'])
            video.pubdate= str(videoDate['pubdate'])
            video.duration= videoDate['duration']
            video.view = str(videoDate['play']).replace('&amp;','&')
            video.favorite= str(videoDate['favorites'] )
            video.reply = str(videoDate['review'])     
            video.aid = str(videoDate['aid'])
            video.bvid = str(videoDate['bvid'])

            #计算不同tag的相对观看数量
            video.vocalInfo = [0] * 15
            vocalList = [u'天依',u'言和',u'乐正绫',u'龙牙',u'摩柯',u'墨清弦',u'星尘',u'心华',u'初音',u'海伊',u'苍穹',u'诗岸',u'赤羽',u'牧心',u'艾可']
            
            for j in range(len(vocalList)):
                if (video.title.count(vocalList[j]) + video.tag.count(vocalList[j]) > 0):
                    video.vocalInfo[j] = 1

            sumV = sum (video.vocalInfo[0:9])
            sumSV = sum (video.vocalInfo[9:15])
            sumVocal = sumV + sumSV
            
            for j in range(len(vocalList)):
                if (video.vocalInfo[j] > 0 and sumVocal > 0):
                    self.lock.acquire()
                    video.vocalInfo[j] = int(video.view) / sumVocal
                    if (self.isJapanese(video.title + video.tag) == False):
                        vocalsDataAnalysis.addData(j,video.vocalInfo[j])
                    self.lock.release()

            # 以下若干行有关于subResultTxt的代码，是用来将各个参数拼接成一行文本，它们用半角逗号隔开
            subResultTxt = video.aid + ','
            subResultTxt = subResultTxt + video.bvid + ','
            subResultTxt = subResultTxt + video.author + ','
            subResultTxt = subResultTxt + video.title + ','
            subResultTxt = subResultTxt + video.typename +','
            subResultTxt = subResultTxt + video.tag + ','
            subResultTxt = subResultTxt + video.pubdate + ','
            subResultTxt = subResultTxt + video.senddate + ','
            subResultTxt = subResultTxt + video.duration + ','
            subResultTxt = subResultTxt + video.view + ','
            subResultTxt = subResultTxt + video.favorite + ','
            subResultTxt = subResultTxt + video.reply + ','

            #拼接加入tag的数
            for j in range(len(vocalList)):
                subResultTxt = subResultTxt + str(video.vocalInfo[j]) + ''','''
            subResultTxt = subResultTxt + str(sumV) + ',' + str(sumSV) + ',' + str(sumVocal) + ','  + str(self.isJapanese(video.title + video.tag)) + '\n'

            #resultTxt20个subResultTxt相加得到的，本函数最终返回它
            resultTxt = resultTxt + subResultTxt

            #后续处理，添加播放量到列表中，参数表中显示播放量的列 + 1，注意线程上锁
            self.lock.acquire()
            viewList.append(int(video.view))
            paraMeterList[1] += 1
            self.lock.release()
            
        self.lock.acquire()
        fileTxt[0] += resultTxt #把filetxt填上本区域的结果
        self.lock.release()

    def searchByKeyword(self,hashList,keyword,startDate,endDate,viewList,vocalsDataAnalysis,mainWindow,isWindow):
        #本函数旨在输入关键字和总页码数，返回一段文本。这段文本是使用UTF-8编码
        fileTxt = ['']
        paraMeterList = [0,0]
        thread = []
        for i in range(50):
            if isWindow:
                mainWindow.changeProgressWindow(1,0,'',i * 2)
            else:
                outTxt = '    '+ keyword +'　\t | [' + str(i+1) + '/50]\t| '
                outTxt += '█' * (i+1)
                if i == 49:
                    print(outTxt)
                else:
                    print(outTxt,end='\r')
            if paraMeterList[0] == 1:
                continue
            # 多线程启动
            t = threading.Thread(target=self.getVideoList,args=(hashList,keyword,i + 1,startDate,endDate,paraMeterList,viewList,fileTxt,vocalsDataAnalysis))
            thread.append(t)
            t.setDaemon(True)
            t.start()
            time.sleep(timeSleep[i % 2])

        for t in thread:
            t.join()
           
        self.numGet += paraMeterList[1]
        return fileTxt[0]

    def processFunction(self,num,typeNum):
        if typeNum == 0:
            return num
        else: 
            if typeNum == 1:
                return math.log2(num)

    def movingAverage(self,array):
        newArray = []
        if array.__len__() <= 10:
            return array
        for i in range(5,array.__len__() - 6):
            newArray.append(array[i])
            for j in range(-5,6):
                newArray[i - 5] += array[i + j]
            newArray[i - 5] -= array[i]
            newArray[i - 5] /= 10
        for i in range(0,newArray.__len__()):
            newArray[i] = self.processFunction(newArray[i],1)
        return newArray

    #————↓ 以下内容为本程序的主干，相当于C++程序的main()函数↓—————
    def main(self,keywordList,startDate,endDate,drawGraph,mainWindow,isWindow):
        if isWindow:
            from PyQt5 import QtCore, QtGui, QtWidgets
            from PyQt5.QtWidgets import QMainWindow, QApplication
        #nowTime仅用于文件命名
        nowTime = datetime.datetime.now().strftime('%Y%m%d %H%M%S')

        #获取路径名称，准备哈希表等变量
        path = os.getcwd() + '\\' + nowTime
        path += ' 查找结果'
        os.makedirs(path)
        path += '\\'
        hashList = self.HASHLIST()
        startDate = time.mktime(datetime.datetime.strptime(startDate,'%Y%m%d').timetuple())
        startDate = self.getTime(startDate)
        endDate = time.mktime(datetime.datetime.strptime(endDate,'%Y%m%d').timetuple())
        endDate = self.getTime(endDate)

        viewList = []
        vocalsDataAnalysis = self.VOCALS_DATA_ANALYSIS()

        result = 'AV号,BV号,up主,标题,分区,标签Tag,发布日期,上传日期/最后修改日期,时长,播放,收藏,评论,洛天依,言和,乐正绫,乐正龙牙,徵羽摩柯,墨清弦,星尘,心华,初音未来,海伊,苍穹,诗岸,赤羽,牧心,艾可,V小记,SV小记,总计,是否为日语' + '\n'
        if isWindow:
            mainWindow.showProgressWindow()
        i = 0
        for keyword in keywordList:
            i += 1
            if isWindow:
                mainWindow.changeProgressWindow(0,i,keyword,0)
            result += self.searchByKeyword(hashList,keyword,startDate,endDate,viewList,vocalsDataAnalysis,mainWindow,isWindow)
        
        if isWindow:
            mainWindow.progressWin.close()
            mainWindow.showNoKeywordWarning('查找完成，一共获取' + str(self.numGet) + '项',"运行完毕")   
        file1 = open(path + 'video_sheet_' + nowTime + '.csv','w')
        result = result.replace('<>','')
        file1.write(result.encode('gbk','ignore').decode('gbk','ignore'))
        viewList.sort(reverse = False)

        #写出歌姬数据
        fileOutput = open(path + 'vocals_sheet_' + nowTime + '.csv','w')
        result = vocalsDataAnalysis.writeVocalList()
        result = result.replace(',\n','\n')
        fileOutput.write(result.encode('gbk','ignore').decode('gbk','ignore'))
        
        #写出引擎数据
        fileOutput = open(path + 'engines_sheet_' + nowTime + '.csv','w')
        result = vocalsDataAnalysis.writeEnginesSheet()
        result = result.replace(',\n','\n')
        fileOutput.write(result.encode('gbk','ignore').decode('gbk','ignore'))

        #移动平均
        viewListMA = self.movingAverage(viewList)
        viewListCount = []
        countList = []
        j = 0

        for i in range(0,viewListMA.__len__()):
            if i == 0:
                countList.append(1)
                viewListCount.append(viewListMA[0])
                j = 0
            else:
                if viewListMA[i] == viewListMA[i - 1]:
                    countList[j] += 1
                else:
                    countList.append(1)
                    viewListCount.append(viewListMA[i])
                    j += 1

        #生成图表
        if viewListCount.__len__() != 0 and drawGraph == 1:
            sns.kdeplot(viewListCount,cumulative=True)
            sns.distplot(viewListCount,norm_hist=True,fit=norm)
            plt.savefig(path + nowTime + '_分布图.png')
            plt.close()
