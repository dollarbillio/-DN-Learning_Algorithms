* Using: Scrapy, Numpy, Scipy, Jupyter, Bs4
---
* Install scrapy: ```pip install scrapy```
* Open command line: ```scrapy startproject quotes_spider```
* Go into the project: ```scrapy genspider qoutes(file_name.py) quotes.toscrape.com```
---
* Go to cmd --> ```fetch("http://quotes.toscrape.com/")```
* ```response.xpath('//h1/a/text()').extract()``` --> ['Quotes to Scrape']
* ```response.xpath('//h1/a/text()').extract_first()``` --> 'Quotes to Scrape'
* ```response.xpath('//*[@class="tag-item"]/a/text()').extract_first()``` --> 'love'
* ```response.xpath('//*[@class="tag-item"]/a/text()').extract()``` --> ['love', 'inspirational', 'life', 'humor', 'books', 'reading', 'friendship', 'friends', 'truth', 'simile']
