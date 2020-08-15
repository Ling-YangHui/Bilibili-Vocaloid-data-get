from getVideoList import mainRun
import datetime

#无GUI运行程序
run = mainRun()
keywordList = ['洛天依','乐正绫','言和','墨清弦','乐正龙牙','徵羽摩柯','星尘','心华','初音未来','海伊','赤羽','诗岸','苍穹','SynthV','艾可']
nowDate = str(datetime.datetime.now().strftime('%Y%m%d'))
print(nowDate)
startDate = str((datetime.datetime.now() + datetime.timedelta(days=-30)).strftime('%Y%m%d'))
print(startDate)
run.main(keywordList,startDate,nowDate,True,None,False)