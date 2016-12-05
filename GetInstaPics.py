import urllib.request
from bs4 import BeautifulSoup
from pathlib import Path
class Insta_pic(object):
    def __init__(self,url):
        self.url=url
    def get_url(self):
        fp=urllib.request.urlopen(self.url)
        soup=BeautifulSoup(fp,"html.parser")
        soup.prettify()
        for url in soup.findAll("img",src=True):
            raw_url=url["src"]
        return raw_url
    def download(self,path,name,raw_url):
        my_file=Path(path+name+".jpg")
        f=True
        while(f==True):
            if my_file.is_file():
                ans=input("There is an existing file with that name, please giveme another name or type continue for replace the existing file: ")
                if ans=="continue":
                   break
                if ans!="continue":
                   name=ans
                   break
            else:
               f=False
        urllib.request.urlretrieve(raw_url, path+name+".jpg")
def main():
    t=True
    print("Hello, this software was developed by Bruno Ortiz")
    while(t==True):
        a=True
        s=True
        while(s==True):
            while(a==True):
                url=input("url: ")
                insta_pic=Insta_pic(url)
                try:
                   insta_pic.get_url()
                   a=False
                except:
                   print("Enter an url")
            if "instagram" in url:
                     s=False
        try:
            path
        except NameError:
            path=input("Type where you want to save the picture(c:/user/..../: ")
        name=input("Name which you want to save the photo: ")
        insta_pic=Insta_pic(url)
        raw_url=insta_pic.get_url()
        insta_pic.download(path,name,raw_url)
        print("Photo saved in "+path+", with the name "+'"'+name+'"')
        ans=input("Do yoy want to download another picture? ")
        if ans=="yes" or ans=="Yes":
            a=True
            while(a==True):
                 ans=input("Do you want to change the saving path? (y/n) ")
                 if ans=="y":
                    path=input("Type the new path: ")
                    a=False
                 if ans=="n":
                    a=False
                 else:
                      print("Please enter a valid input ")           
        else:
            print("Good bye")
            t=False
main()

