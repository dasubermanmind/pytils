
import requests, os, bs4

class Scraper():
    def __init__(self,url, location, file_name,content, images, datas=[],endpoint='#'):
        self.url = url
        self.location = location
        self.datas= datas
        self.filename = file_name
        self.endpoint = endpoint
        self.content = content
        self.images = images
                
        os.mkdir(self.filenme, exist_ok=True)

        for data in datas:
            print(data)

        while not self.url.endsWith(endpoint):
            res = requests(self.url)
            res.raise_for_status()
            bs4.BeautifulSoup(res.txt, 'html.parser')
            divToSelect=''
            # if we have content from the endpoint
            # parse it out, and return res
            bs4.select(divToSelect)
