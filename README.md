# tiki-scraping
A web crawler that scraps a single page or all product pages on Tiki.vn
The visualizer is based on Flask framework
## Scrap a single product page
1. Prepare the database in json
  - run tiki_web_scrapping.ipynb
  - insert tiki product page into BASE_URL
  - retrieve json file
2. Run the visualizer
  - On terminal run `python app.py`
  
## Scrap all products available on tiki.vn
1. Prepare the database
  - run tiki-scrap-all.ipynb
  - insert tiki.vn into BASE_URL
  - Wait and inspect error messages while the crawler iterate through each product category. The most common error is 
