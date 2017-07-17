from urllib.request import urlopen
import re

def crawl_pages(rng):
    
    idx = 44726
    base_url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    for i in range(rng):
        text = urlopen(base_url + str(idx))
        contents = str(text.read())
        print(contents)
        res = re.search('and the next nothing is ', contents)
        if res:
            res = res.start()
            idx = contents[res+24:res+29]
            print(idx)

        else:
            print('Done')
            break

crawl_pages(400)
        


