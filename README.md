# ESG Crawler
A web crawler for ESG news from Business Today. （https://esg.businesstoday.com.tw/catalog/180686/）.

[FinNLP 2023] Shared Task: Multi-Lingual ESG Issue Identification (ML-ESG)

## Environment Requirements

- Python 3.8
- Pandas 2.0.0
- Scrapy 2.8.0
- Scrapy-splash 0.8.0


## Usage
- First, you need to install the requirements.
```
pip install -r requirements.txt
```

- Second, you need to prepare the web url list as the same format as `url_example.csv`.

- Last, you can crawl the HTML content of all web in your web url list and output the result into json or csv files.
```
scrapy crawl business_today -o {output.csv}
scrapy crawl business_today -o {output.json}
```

## 