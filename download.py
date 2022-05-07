import requests
from lxml import etree
import os,sys
key = sys.argv[1]
response = requests.get("https://www.vectorstock.com/royalty-free-vectors/"+key+"-vectors")
html=etree.HTML(response.text)
res = html.xpath('//img[@class="reveal"]/@src')
for item in res:
    url = item.replace('thumb-large','1000x1000')
    r = requests.get(url, stream=True)
    with open("./image/"+os.path.basename(url), "wb") as f:
        for bl in r.iter_content(chunk_size=1024):
            if bl:
                f.write(bl)
