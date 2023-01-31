import requests
from pyquery import PyQuery
import time
#下载对应章节txt文件
def write_novel(URL,filename,name):
    html = requests.get(URL).content
    doc = PyQuery(html)
    items = doc(".box_con").items()
    for item in items:
        content = item.find("#content").text()
        text=name+"\n\n"+content
        with open("d:\\一剑独尊\\" + filename + ".txt", "w", encoding="utf-8") as file:
            print("准备写入",filename)
            file.write(text)
            print("写入成功")
            time.sleep(0.1)


try :
    # 获取每章节url
    UA = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76"}
    url = "http://www.gashuw.com/biquge_169948/"
    html = requests.get(url=url, headers=UA).content
    doc = PyQuery(html)
    items = doc("dl dd").items()
    i = 0
    for item in items:
        i+=1
        url = item.find("a").attr("href")
        name =" "+ item.find("a").text()+" "
        URL = "http://www.gashuw.com" + url
        write_novel(URL=URL, filename=str(i),name=name)
except KeyboardInterrupt:
    print("\n写入终止")