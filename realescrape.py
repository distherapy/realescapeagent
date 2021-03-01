import pandas as pd
import requests
import scrapy
import re
#pseudolayout
#
#starts with $y. pays the taxes and sells residential property back to the delinquent owners at a reduced rate if need be, so they can't have their land stolen for not paying the state their extortion racket fees, or commercial property and sell it to the general public. there is no interest and no keeping the land. land obtained using realescape agent that is not returned to the owners will be converted into park or public needs. the user running realEscapeAgent will receive an available property of their choosing(relative to $y) that has been defaulted on by a corporation.
#
#ask user which county and state
#ask user commercial, residential, county plat map
#
faceamount = response.xpath('faceValue')
print(faceamount)

x = raw_input("Which county and which state are you looking?")
y = raw_input("Enter 'C' or 'R' for Commericial, Residential")

allowed_domains = ["arizonataxsale.com"]

class taxLien(scrapy.Spider):
    name = "taxlien"

    def start_requests(self):
        urls = ['https://apache.arizonataxsale.com/index.cfm?folder=previewitems',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = f'taxlien-{page}.html'
        # with open(filename, 'wb') as f:
            # f.write(response.body)
        # self.log(f'Saved file {filename}')
        
    def parse(self, response):
        available = response.xpath('//*[@id="previewResults"]/table//tr')
        for debts in available[1:]:
            item['debt'] = product.xpath('td[faceValue]//text()').extract_first()
            yield item

url = "https://apache.arizonataxsale.com/index.cfm?folder=previewitems"

r = requests.get(url)
df_list = pd.read_html(r.text)
df = df_list[0]
df.head()
print(df)
