#coding: utf-8
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime

# 日本語での曜日
date = [u'月',u'火',u'水',u'木',u'金',u'土',u'日']

# chouseiData.txtを開いて諸事項を取得
f = open("/Users/k_kiuchi/Desktop/chouseiData.txt", "r")
# 内容をlines2にコピー
lines2 = f.readlines()
f.close()
# 開始日と終了日
sday = datetime.datetime.strptime(lines2[0].strip(), '%Y-%m-%d').date()
eday = datetime.datetime.strptime(lines2[1].strip(), '%Y-%m-%d').date()
# タイトルとメモ
title = lines2[2].strip()
memo = lines2[3].strip()

#開始日、終了日から候補リストdayListを作成
dayList = []
# 候補日の数だけ繰り返し
for i in range((eday-sday).days + 1):
    # このループでの日をtDayとする
    tDay = sday + datetime.timedelta(days=i)
    # 1~7限まで作るのでrange(1,8)で繰り返し
    for j in range(1,8):
        # dayListに"月/日 (曜日) ○限"というフォーマットでappend
        dayList.append(tDay.strftime("%m/%d") + "（" + date[tDay.weekday()] + "）" + str(j) + u"限")


# firefoxを起動
browser = webdriver.Firefox()
# 調整さんトップページにアクセス
browser.get("https://chouseisan.com")
# name,comment,kouhoのidをもつフィールドに
browser.find_element_by_id('name').send_keys(title)
browser.find_element_by_id('comment').send_keys(memo)
browser.find_element_by_id('kouho').send_keys("\n".join(dayList))
# eName.send_keys(title)
# eMemo.send_keys(memo)
# dayListを要素間に"\n"を入れて文字列化
# eDate.send_keys("\n".join(dayList))
cBtn = browser.find_element_by_id('createBtn').send_keys(Keys.ENTER)
