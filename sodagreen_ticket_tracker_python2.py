# -*- coding:utf-8 -*-
import urllib
import webbrowser

number=1404

while 1:
  response = urllib.urlopen('https://tixcraft.com/ticket/area/16_soda/'+str(number))
  html = response.read().decode('utf8')
  print(html)
  if number==1404:
    event='8/5同名'
  elif number==1405:
    event='8/6同名'
  elif number==1406:
    event='8/7同名'
  elif number==1407:
    event='8/12小宇宙'
  elif number==1408:
    event='8/13小宇宙'
  elif number==1409:
    event='8/14小宇宙'
  elif number==1410:
    event='8/19無與倫比的美麗'
  elif number==1411:
    event='8/20無與倫比的美麗'
  elif number==1412:
    event='8/21無與倫比的美麗'
  elif number==1413:
    event='8/27陪我歌唱'
  elif number==1414:
    event='8/28陪我歌唱'
  elif number==1415:
    event='9/2夏／狂熱'
  elif number==1416:
    event='9/3夏／狂熱'
  elif number==1417:
    event='9/4夏／狂熱'
  elif number==1418:
    event='9/9秋：故事'
  elif number==1419:
    event='9/10秋：故事'
  elif number==1420:
    event='9/11秋：故事'
  elif number==1421:
    event='9/16冬　未了'
  elif number==1422:
    event='9/17冬　未了'
  elif number==1423:
    event='9/18冬　未了'
  elif number==1424:
    event='9/23你在煩惱什麼'
  elif number==1425:
    event='9/24你在煩惱什麼'
  elif number==1426:
    event='9/25你在煩惱什麼'
  elif number==1427:
    event='10/1十年一刻'
  elif number==1428:
    event='10/2十年一刻'
  elif number==1429:
    event='10/7春．日光'
  elif number==1430:
    event='10/8春．日光'
  elif number==1431:
    event='10/9春．日光'
  if html.find(u'此場次/區域已完售')>=0:
    print(event+' 售完')    
  else:
    print(event+' 快買')
    webbrowser.open('https://tixcraft.com/ticket/area/16_soda/'+str(number))
  number+=1
  if number==1432:
    number=1404
    
