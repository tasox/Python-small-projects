import sys
import re
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
import argparse
import json

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def searchWeb(url,cookie):

    externalLinks_array=[]
    internalLinks_array=[]
    imageLinks_array=[]
    links_array=[]
    javascriptLinks_array=[]
    metaLinks_array=[]
    baseUrl = ''
    if(url):
        if (cookie != ""):	
            r = requests.get(url,cookies=cookie,verify=False)
        else:
            r = requests.get(url,verify=False)
        
        s = BeautifulSoup(r.text,'lxml')
        print("Response Headers:")
        print(r.headers)
        print("\n")
        print(Style.BRIGHT + Fore.RED + "Response Content - External Urls:" + Fore.RESET)
        for link in s.findAll('a', attrs={'href': re.compile("^htt(ps)://")}):
            extURL = re.search(url,link.get('href'))
            if(link.get('href') and not extURL):
                #print(extURL
                if (link.get('href') not in externalLinks_array):
                    externalLinks_array.append(link.get('href'))
                    print("[*] "+link.get('href')+" added!")
        print("\n")
        print(Style.BRIGHT + Fore.RED + "Response Content - Internal Urls:" +url + Fore.RESET)
        for ilink in s.findAll('a', attrs={'href': re.compile("^\/[^\/]")}):
            if(ilink.get('href')):
                #print(ilink.get('href')
                if baseUrl+ilink.get('href') not in internalLinks_array:
                    internalLinks_array.append(baseUrl+ilink.get('href'))
                    print("[*] "+baseUrl+ilink.get('href')+" added!")
        print("\n")
        print(Style.BRIGHT + Fore.RED + "Response content - Image Urls:" + Fore.RESET)
        for img in s.findAll('img'):
            if(img.get('src')):
                #print(img.get('src')
                if img.get('src') not in imageLinks_array:
                    imageLinks_array.append(baseUrl+img.get('src'))
                    print("[*] "+baseUrl+img.get('src')+" added!")
        
        print("\n")
        print(Style.BRIGHT + Fore.RED + "Response content - Link Urls:" + Fore.RESET)
        for link in s.findAll('link'):
            if(link.get('href')):
                print(link.get('href'))
        if link.get('href') not in links_array:
            links_array.append(baseUrl+link.get('href'))
            print("[*] "+baseUrl+link.get('href')+" added!")
        print("\n")
        print(Style.BRIGHT + Fore.RED + "Response Content - Javascript Urls:" + Fore.RESET)
        for js in s.findAll('script'):
            if(js.get('src')):
                #print(js.get('src')
                if js.get('src') not in javascriptLinks_array:
                    javascriptLinks_array.append(baseUrl+js.get('src'))
                    print("[*] "+js.get('src')+" added!")
        
        print("\n")
        print(Style.BRIGHT + Fore.RED + "Response Content - Meta Content Urls:" + Fore.RESET)
        #print(s.findAll('meta', attrs={'content': re.compile("^htt(ps)://\w+.\w+")})
        for content in s.findAll('meta', attrs={'content': re.compile("^htt(ps)://")}):
        #	print("OK!!!"
            if(content.get('content')):
                                print(content.get('content'))
            if content.get('content') not in metaLinks_array:
                try:
                    metaLinks_array.append(baseUrl+content.get('content'))
                    print("[*] "+baseUrl+content.get('content')+" added!")
                except Exception as e:
                    print("[-] "+e)
        #for x in internalLinks_array:
        #	searchWeb(x,cookie)

    else:

        print("You must give a url!")
        print("(+) %s -u <taget_ul>" % (sys.argv[0]))
def main():

    
    parser=argparse.ArgumentParser(description='Python Spidering')
    parser.add_argument("-u","--url",help="Url to Spider",required=True)
    parser.add_argument("-c","--cookie",help="{\"cookie_param1\":\"123456\",\"JSESSION\":\"78901\"}",required=False)
    parser.add_argument("-s","--spider")
    global args
    args=parser.parse_args()

    #Burp Cookie to JSON
    dict={}
    if(args.cookie and args.cookie != ""):
        cookie_val = args.cookie
        for element in cookie_val.split('; '):
            x, y = element.split('=',1)
            dict[x]=y
        cookie_value=dict
    
    else:
        cookie_value=""

    if(args.url != ""):
        url_value=args.url
    else:
        url_value=""

    searchWeb(url_value,cookie_value)


if __name__=="__main__":
    main()