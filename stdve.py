#!/usr/bin/env python

index = open("index.html", "w")

index.write(" \
<!doctype> \
<html> \
  <head> \
    <meta charset=\"UTF-8\"> \
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
  </head> \
  <body> \
    <div style=\"width:100%; text-align:center\"> \
      <img src=\"img/whose_laughing_now.jpg\" alt=\"Who's laughing now?\">  \
    </div>   \
  </body> \
</html> \
")

index.close()
