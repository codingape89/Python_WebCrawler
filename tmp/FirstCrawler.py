import urllib2

def getHtml(url):
    page = urllib2.urlopen(url)
    html = page.read()
    return html

html = getHtml("http://index.0256.cn/pricex.htm")

print html
