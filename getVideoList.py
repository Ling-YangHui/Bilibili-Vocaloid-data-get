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

#全局变量区域
#在以后的维护中，请尽量少使用全局变量
lock = threading.Lock() #线程互斥锁
timeSleep = [0.1,0.15]

class mainRun():
    #全局变量区域
    #在以后的维护中，请尽量少使用全局变量
    def __init__(self):
        super().__init__()
        self.lock = threading.Lock() #线程互斥锁
        self.timeSleep = [0.1,0.15]

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

    def getVideoList(self,hashList,keyword,page,startDate,endDate,paraMeterList,viewList,fileTxt):
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

        #json转化为字典格式
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
                self.lock.release
                continue
            self.lock.release()

            #获取字典中各项数值，加入到video类中去
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

            #计算不同tag的相对观看数量值
            video.vocalInfo = [0,0,0,0,0,0,0,0,0]
            vocalList = [u'天依',u'言和',u'阿绫',u'龙牙',u'摩柯',u'墨清弦',u'星尘',u'心华',u'初音',]
            for j in range(9):
                if (video.title.count(vocalList[j]) + video.tag.count(vocalList[j]) > 0):
                    video.vocalInfo[j] = 1
            sumVocal = sum(video.vocalInfo)
            for j in range(9):
                if (video.vocalInfo[j] > 0):
                    video.vocalInfo[j] = int(video.view) / sumVocal

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

            #拼接加入tag的数量
            for j in range(9):
                subResultTxt = subResultTxt + str(video.vocalInfo[j]) + ','
            subResultTxt = subResultTxt + str(sumVocal) + ',' + str(self.isJapanese(video.title + video.tag)) + '\n'

            #resultTxt20个subResultTxt相加得到的，本函数最终返回它
            resultTxt = resultTxt + subResultTxt

            #后续处理，添加播放量到列表中，参数表中显示播放量的列表 + 1，注意线程上锁
            self.lock.acquire()
            viewList.append(int(video.view))
            paraMeterList[1] += 1
            self.lock.release()
        self.lock.acquire()
        fileTxt[0] += resultTxt
        self.lock.release()

    def searchByKeyword(self,hashList,keyword,startDate,endDate,viewList):
        #本函数旨在输入关键字和总页码数，返回一段文本。这段文本是使用UTF-8编码的
        fileTxt = ['']
        paraMeterList = [0,0]
        thread = []
        for i in range(50):
            outTxt = '    '+ keyword +'　\t | [' + str(i+1) + '/50]\t| '
            outTxt += '█' * (i+1)
            if i == 49:
                print(outTxt)
            else:
                print(outTxt,end='\r')

            if paraMeterList[0] == 1:
                continue
            # 多线程启动
            t = threading.Thread(target=self.getVideoList,args=(hashList,keyword,i + 1,startDate,endDate,paraMeterList,viewList,fileTxt))
            thread.append(t)
            t.setDaemon(True)
            t.start()
            time.sleep(timeSleep[i % 2])

        for t in thread:
            t.join()

        print (str(paraMeterList[1]) + 'items got')    
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

    #————↓ 以下内容为本程序的主干，相当于C++程序的main()函数↓——————
    def main(self,keywordList,startDate,endDate):
        import matplotlib.pyplot as plt
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

        result = 'aid,bvid,uploader,title,typename,tags,pubdate,senddate,duration,view,favo,reply,LTY,YH,YZL,YZLY,ZYMK,MQX,XC,XH,CYWL,sumVocal,isJapanese' + '\n'
        for keyword in keywordList:
            result += self.searchByKeyword(hashList,keyword,startDate,endDate,viewList)
        
        adrres = path + nowTime + ' 查找结果.csv'    
        file1 = open(adrres,'w')
        result = result.replace('<>','')
        file1.write(result.encode('gbk','ignore').decode('gbk','ignore'))
        viewList.sort(reverse = False)

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
        if viewListCount.__len__() != 0:
            sns.kdeplot(viewListCount,cumulative=True)
            sns.distplot(viewListCount,norm_hist=True,fit=norm)
            plt.savefig(path + nowTime + '_分布图.png')
            plt.close()