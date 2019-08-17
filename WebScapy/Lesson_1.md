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
