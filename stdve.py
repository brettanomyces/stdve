#!/usr/bin/env python

import glob
import os
import json
from yattag import Doc, indent

def images():
    img_dir = "img/"
    files = filter(os.path.isfile, glob.glob(img_dir + "*.jpg"))
    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    return files

doc, tag, text = Doc().tagtext()
doc.asis('<!DOCTYPE html>')
with tag('html'):
    with tag('head'):
        doc.stag('meta', charset='UTF-8')
        doc.stag('meta', name='description', content='steve, stdve, dteve, sliky bule')
        with tag('title'):
            text('stdve')
        with tag('style'):
            text('body { max-width:40em; padding:4em 2em; margin:auto; font-family:\'Helvetica Neue\', sans-serif; }')
        with tag('script'):
            text("""
                    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){ 
                    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o), 
                    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m) 
                    })(window,document,'script','https://www.google-analytics.com/analytics.js','ga'); 
                    ga('create', 'UA-84198117-1', 'auto'); 
                    ga('send', 'pageview');""")

        with tag('body'):
            with tag('div', ('style', 'width:100%; text-align:center')):
                doc.stag('img', alt='pumped, pummelled and pulverized', onclick='next()', id='img')

            with tag('script'):
                doc.asis(" \
                        var imgs = " + json.dumps(images()) + "; \
                        var idx = 0; \
                        document.getElementById(\"img\").src=imgs[idx]+\"?\"+new Date().getTime(); \
                        function next() {  \
                            idx = idx + 1; \
                            if (idx >= imgs.length){ \
                              idx = 0; \
                            } \
                            document.getElementById(\"img\").src=imgs[idx]+\"?\"+new Date().getTime(); \
                        };")


index = open("index.html", "w")
index.write(indent(doc.getvalue()))
index.close()
