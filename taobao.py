'''
author :Liuian
data: 2017-05-05

程序设计结构：
1.提交商品搜索请求，循环获取页面
2.对于每个页面，提取商品名称和价格信息
3.将信息输出到屏幕上

'''
import requests
import re

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # print(r.text[:3000])
        return r.text  # r.text还是个str object
    except:
        print("ERROE!")
        return ""


def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html) #获取所有商品的价格信息
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)  #获取所有商品的名称信息
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:
        print("Nothing!")

def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1]))



def main():
    goods = "书包"
    depth = 3
    start_url = "https://s.taobao.com/search?q=" + goods # 向淘宝提交搜索链接的关键词接口
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)


if __name__ == '__main__':
    main()
