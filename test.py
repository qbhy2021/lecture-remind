import requests


if __name__=='__main__':
    url='https://www1.szu.edu.cn/board/infolist.asp?infotype=%BD%B2%D7%F9'
    r=requests.get(url)
    print(r.text)

