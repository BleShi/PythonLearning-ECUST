import re
import urllib.request
import tkinter

def craw(url,page):
    html1=urllib.request.urlopen(url).read()
    html1=str(html1)
    pat1='<ul class="content">.+?<div class="pageindex">'
    result1=re.compile(pat1).findall(html1)
    result1=result1[0]
    pat2='<img src="https://(.+?\.jpg)"'
    imagelist=re.compile(pat2).findall(result1)
    x=1
    for imageurl in imagelist:
        imagename='d:/img/P'+str(page)+'N'+str(x)+'.jpg'
        imageurl="https://"+imageurl
        try:
            urllib.request.urlretrieve(imageurl,filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                x+=1
            if hasattr(e,"reason"):
                x+=1
        x+=1
for i in range(1,2):
    url='https://car.autohome.com.cn/jingxuan/list-0-p'+str(i)+'.html'
    craw(url,i)
    
win = tkinter.Tk()
w = win.winfo_screenwidth()
h = win.winfo_screenheight()
win.geometry("%dx%d" %(w,h))
win.mainloop()