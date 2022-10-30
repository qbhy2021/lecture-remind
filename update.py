import requests
from bs4 import BeautifulSoup
import time
import sqlite3
import os

from email_text import Email


class Lecture:
    def __init__(self):
        self.ROOT_URL = 'https://www1.szu.edu.cn/board/'
        self.URL = 'https://www1.szu.edu.cn/board/infolist.asp?infotype=%BD%B2%D7%F9'
        self.HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
        self.db_file = os.path.join(os.path.dirname(__file__), 'lecture.db')
        self.Lecture_list = []

    def get_html(self, url, headers):
        s = requests.Session()
        rep = s.get(url=url, headers=headers)
        rep.encoding = 'gbk'
        return rep.text

    def get_info(self):
        soup = BeautifulSoup(self.get_html(self.URL, self.HEADERS), 'html.parser')
        url_list = soup.find_all('td', align='left')  # 或attrs={'class':'fontcolor3'} ——>class_='fontcolor3'
        for lecture in url_list:
            parent = lecture.parent
            if not parent.contents[5].font:
                break
            Ttime = parent.contents[5].string.split(' ')
            time = Ttime[0].split('/')[0] + '月' + Ttime[0].split('/')[1] + '日' + Ttime[1]  # ｜｜
            place = parent.contents[3].string.split('｜')[1]  # | ？？？
            if place == '其他':
                place = '腾讯会议'
            theme = lecture.a.string
            url = self.ROOT_URL + lecture.a['href']
            department = lecture.next_sibling.next_sibling.a.string
            self.Lecture_list.append([time, place, theme, department, url])
            print([time, place, theme, department, url], '\n')
        return self.Lecture_list

    def judge_new(self, info):
        data = []
        # 数据库中读取上次数据
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()
            # 判断数据表是否存在
            cursor.execute("create table if not exists lecture1 (time varchar(20),place varchar(20),theme varchar(20),"
                           "department varchar(20),url varchar(20))")  # ,speaker varchar(20)
            select = cursor.execute("select * from lecture1")

            for row in select:
                if row:
                    data.append([i for i in row])
            # print(data)
            cursor.execute('delete from lecture1')  # 清除上次数据

            for i in range(0, len(info)):
                print(i)
                # '{info[i][0]}', '{info[i][1]}', '{info[i][2]}', '{info[i][3]}', '{info[i][4]}'
                cursor.execute(f"insert into lecture1 (time,place,theme,department,url) values "
                               f"('{info[i][0]}', '{info[i][1]}', '{info[i][2]}', '{info[i][3]}', '{info[i][4]}')")

                if info[i][3] == '电子与信息工程学院' and info[i] not in data:
                # if True:
                    news = Email(info[i])
                    news.send()
                    time.sleep(5)
        except:
            print('error!')
        finally:
            cursor.close()
            conn.commit()
            conn.close()


if __name__ == '__main__':
    lect = Lecture()
    while True:
        lect.judge_new(lect.get_info())
        time.sleep(60 * 60 * 2)
