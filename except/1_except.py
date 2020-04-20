import requests
from pyquery import PyQuery

def main():
    print("spide unknown website...")
    url = "http://www.aaa.com/"
    count = 0
    while(count < 3):
        doc = None
        item_lists = []
        try:
            resp = requests.get("https://blog.csdn.net/")
            doc = PyQuery(resp.text)
            print(resp.text)
            print(resp.status_code)
            item_lists = doc.items("div[class='feed_company csdn-tracking-statistics'] ul[class='company_list'] li")
        except:
            print("This web site is not reachable!")
            print("try for the %d th time" % count)
            print(doc)
            count += 1

        for item in item_lists:
            print(item)

main()
