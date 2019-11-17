# tiki-scraping
A web crawler that scraps a single page or all product pages on Tiki.vn \n
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
    - Wait and inspect error messages while the crawler iterate through each product category. The most common error is ```ERROR: HTTPSConnectionPool(host='tiki.vn', port=443): Max retries exceeded with url: /thiet-bi-kts-phu-kien-so/c1815?src=c.1815.hamburger_menu_fly_out_banner&page=35 (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x111f1f358>: Failed to establish a new connection: [Errno 60] Operation timed out'))```
2. Inspect the result data
    - Data is available in json file and csv file as a result of pandas dataframe
    - run `len()` or `df.size()` to get the total number of items
3. Visualize the result
    - Edit the app.py file so that tiki.json will be read
    - On terminal run  `python app.py`
