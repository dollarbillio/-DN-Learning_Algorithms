* Using: Scrapy, Numpy, Scipy, Jupyter, Bs4
---
* Install scrapy: ```pip install scrapy```
* Open command line: ```scrapy startproject quotes_spider```
* Go into the project: ```scrapy genspider qoutes(file_name.py) quotes.toscrape.com```
---
* Go to cmd -->```scrapy shell```--> ```fetch("http://quotes.toscrape.com/")```
*                                --> ```response```: <200 http://quotes.toscrape.com/>

---
```response``` in '''scrapy shell```

* ```response.xpath('//h1/a/text()').extract()``` --> find h1 -> a tag ->['Quotes to Scrape']
* ```response.xpath('//h1/a/text()').extract_first()``` --> 'Quotes to Scrape'
* ```response.xpath('//*[@class="tag-item"]/a/text()').extract_first()``` --> 'love'
* ```response.xpath('//*[@class="tag-item"]/a/text()').extract()``` --> ['love', 'inspirational', 'life', 'humor', 'books', 'reading', 'friendship', 'friends', 'truth', 'simile']
---
* Change the spider file using Sublime and change to this
```py
def parse(self, response):
    	h1_tag = response.xpath('//h1/a/text()').extract_first()
    	tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()
        
    	yield {'H1 Tag':h1_tag, 'Tags':tags}
 ```
 * ```scrapy list```: to see spider 
 * ```scrapy crawl spider_name```: run spider in terminal
---
* ```scrapy shell url```
* ```quotes = response.xpath('//*[@class="quote"]')```
* ```quote = quotes[0]```
* ```quote.xpath('.//a')```: only a in quote
* ```quotes = response.xpath('.//*[@class="quote"]')```
* ```quote.xpath('.//*[@class="text"]')```
* ```quote.xpath('.//*[@class="text"]/text()').extract_first()```: text
---
After having this
```py
def parse(self, response):
    quotes = response.xpath('//*[@class="quote"]')
    for quote in quotes:
        text = quote.xpath('.//*[@class="text"]/text()').extract_first()
        author = quote.xpath('.//*[@itemprop="author"]/text()').extract_first()
        tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()

        yield{'Text': text,
              'Author': author,
              'Tags': tags}

     # go to next page
     next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
     absolute_next_page_url = response.urljoin(next_page_url)
     yield scrapy.Request(absolute_next_page_url)
```
In terminal
* ```scrapy crawl quotes -o item.csv/item.json```
