import requests
from pyquery import PyQuery



#下载相应章节text
def write_novel(URL,filename):
    htmll = requests.get(URL).content
    doc = PyQuery(htmll)

    items = doc(".txt").items()
    for item in items:
        item.text()
        with open("D:\\novel\\全职法师\\"+filename+'.txt',"w",encoding="utf-8") as file:
            file.write(item.text())

try:
    html = requests.get("https://m.92qb.com/xiaoshuo/14/14647/").content
    doc = PyQuery(html)
    # 获取每章url及名字
    items = doc(".chapter > li").items()
    for item in items:
        name = item.find("a").text()  # 每章节的名字
        url = item.find('a').attr("href")
        write_novel("https://m.92qb.com/xiaoshuo/14/14647/" + url[:-5] + ".html", name)
        print("%s下载完成。"%name)
        # 每章的url网址

except KeyboardInterrupt:
    print("下载终止")





