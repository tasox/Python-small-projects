import requests,re
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import argparse
import subprocess

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


def searchWeb(url,tor):

    urlFinalDict= {}
    urlList = []

    scriptsList = []
    scriptsDict = {}
    
    noscriptsList = []
    noscriptsDict = {}

    if(url):
        headers = { "User-Agent": UserAgent().random}
        proxies = {
            'http': 'socks5://127.0.0.1:9050',
            'https': 'socks5://127.0.0.1:9050'
        }

        if tor != "":
           
            cmd_output = subprocess.call(['sudo', 'service', 'tor', 'start'])
            print(cmd_output)
            r = requests.get(url,verify=False,headers=headers,proxies=proxies)
        else:
            r = requests.get(url,verify=False,headers=headers)
        
        print("Response Headers:")
        print(r.headers)

        s = BeautifulSoup(r.text,'lxml')

        src_tags = s.find_all(['a','link','img','script','iframe','body','input','object','embed','video','form','noscript'])
        href_tags = s.find_all(href=True)
        script_tags = s.find_all('script')
        noscript_tags = s.find_all('noscript')
        
        c = 0
        if href_tags != None:
            for href in href_tags:
                if  href != None and href.has_attr('href'):
                    urlList.append({c:href['href'],'OpenCTIScore':0})
                    c += 1
        if src_tags != None and len(src_tags) >0:
            for src in src_tags:
                if src != None and src.has_attr('src'):
                    urlList.append({c:src['src'],'OpenCTIScore':0})
                    c += 1
        if script_tags != None and len(script_tags) >0:
            for script_tag in script_tags:
                if script_tag != None:
                    scriptsList.append(script_tag)
        
        if noscript_tags != None and len(noscript_tags) >0:
            print("[*] Noscript tag found! ")
            for noscript_tag in noscript_tags:
                if noscript_tag != None:
                    noscriptsList.append(noscript_tag)
        
        urlFinalDict.update({'urls':urlList})
        scriptsDict.update({'scripts':scriptsList})
        noscriptsDict.update({'noscripts':noscriptsList})
        
        print(urlFinalDict)
        print("\n")  
        print(scriptsDict)
        print("\n")
        print(noscriptsDict)
        print("\n")   
     

def main():
    
    parser=argparse.ArgumentParser(description='Python Spidering')
    parser.add_argument("-u","--url",help="Url to Spider",required=True)
    parser.add_argument("-t","--tor",action="store_true",help="TOR-as-Proxy",default=False,required=False)
    global args
    args=parser.parse_args()

    if(args.url != ""):
        url_value=args.url
    else:
        url_value=""
    
    if(args.tor != ""):
        tor_value=args.tor
    else:
        tor_value=""
