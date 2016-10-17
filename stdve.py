#!/usr/bin/env python

import glob
import os

def images():
  img_dir = "img/"
  files = filter(os.path.isfile, glob.glob(img_dir + "*.jpg"))
  return files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

def head():
    return "\
            <head> \
            <meta charset=\"UTF-8\"> \
            <meta name=\"description\" content=\"steve, stdve, dteve, sliky blue\"> \
            <title>stdve</title> \
            <style> \
            body{ \
            max-width:40em; \
            padding:4em 2em; \
            margin:auto; \
            font-family:'Helvetica Neue', sans-serif; \
            } \
            </style> \
            <script> \
            (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){ \
            (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o), \
            m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m) \
            })(window,document,'script','https://www.google-analytics.com/analytics.js','ga'); \
            \
            ga('create', 'UA-84198117-1', 'auto'); \
            ga('send', 'pageview'); \
            </script> \
            </head>"

def body():
    return "\
            <body> \
            <div style=\"width:100%; text-align:center\"> \
            <img id=\"img\" alt=\"Who's laughing now?\">  \
            </div>" \
            + script() \
            + "</body>"

def script():
  return "<script> \
  function img() { \
    document.getElementById(\"img\").src=\"img/whos_laughing_now.jpg?\"+new Date().getTime(); \
  } \
  img(); \
  </script>" 

index = open("index.html", "w")

index.write(" \
<!doctype> \
<html>"
  + head()
  + body()
  + "</html>")

index.close()

