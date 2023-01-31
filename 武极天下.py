import requests
from pyquery import PyQuery
import time



#下载相应章节text
def write_novel(URL,filename):
    html = requests.get(URL).content
    doc = PyQuery(html)

    items = doc("#content").items()
    for item in items:
        item.text()
        with open("D:\\novel\\武极天下\\" + filename + '.txt', "w", encoding="utf-8") as file:
            file.write(item.text())


try:
    html = requests.get("https://www.xxbiqudu.com/51_51313/").content
    doc = PyQuery(html)

    items = doc("#list  > dl > dd ").items()
    for item in items:
        name = item.text()
        url = item.find("a").attr("href")
        print("正在下载%s"%name)
        write_novel(url,name)
        print("下载完成")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("下载终止")





