# ESG Crawler

A web crawler for ESG news from Business Today. （https://esg.businesstoday.com.tw/catalog/180686/）.


## Environment Requirements

- Python 3.8
- Pandas 2.0.0
- Scrapy 2.8.0
- Scrapy-splash 0.8.0
- Bs4 0.0.1

## Usage
- First, you need to install the requirements.（Note that the training set has already in **data/**.）

```
pip install -r requirements.txt
```

- Then, you can crawl the news content with HTML tags and the clean news content of all urls in the training set by giving the argument `-a dataset=Train`, `-a dataset=Dev` or `-a dataset=Test`.


- Finally, you can easily output the result into json or csv files as follows. The output will have two new columns along with the four columns of training set, so the output data shape will be（# of news, 6）. 

    - news_content：clean news content
    - news_content_html：origin HTML tags of news content

```
scrapy crawl business_today -a dataset={dataset} -o {output.csv}
scrapy crawl business_today -a dataset={dataset} -o {output.json}
```

## Reference

Please refer to FinNLP-2023 website for more details.

[FinNLP 2023] Shared Task: Multi-Lingual ESG Issue Identification (ML-ESG)：https://sites.google.com/nlg.csie.ntu.edu.tw/finnlp-2023/shared-task-esg-issue