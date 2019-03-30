import sys

import tkinter as tk

import requests

import json

import re

from tkinter import messagebox

import random

class Spider:
    
        def __init__(self):

            self.video_api = "https://www.bilibili.com/video/av"    # 视频信息
        

        def get_api(api_url):                       

            headers = {
                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
                 'Host': 'www.bilibili.com',
                 'Accept-Language': 'zh-Hans-CN, zh-Hans; q=0.8, en-GB; q=0.7, ja; q=0.5, en-IE; q=0.3, en; q=0.2',
                 'Accept-Encoding': 'gzip, deflate, br',
                 'Accept': 'text/html, application/xhtml+xml, application/xml; q=0.9, */*; q=0.8',
                 'Upgrade-Insecure-Requests': '1',
                 'Cache-Control': 'max-age=0',
                 'Connection': 'Keep-Alive',
                 'DNT':'1',
                }                               #请求头信息

            res = requests.get(api_url, headers=headers)

            return res.text
        
        def get_video_info(self):
            aid= str(random.randint(1,40000000))

            res = Spider.get_api(self.video_api + aid)

            pattern = re.compile(r'<h1 title="(.*)" class="video-title">',re.S)          #正则提取：标题
            ret1 = re.findall(pattern,res)
            str1 = ' '.join(['标题：']+ret1)


            pattern2 = re.compile(r'<div class="info open">([\s\S]*?)</div>',re.S)       #正则提取：视频简介
            ret3 = re.findall(pattern2,res)
            str3 = ' '.join(['视频简介：']+ret3)
            if ret1==[]:
                tk.messagebox.showinfo(title='Error',message = 'av'+aid+'\n'+'该视频已下架')
            else:
                tk.messagebox.showinfo(title='视频信息',message = (str1+'\n'+'av'+aid+'\n'+str3))

