import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

def load_website(url,prefix):
    try:
        response = requests.get(prefix+url)
        return BeautifulSoup(response.text)
    except Exception as err:
        print(f'ERROR: {err}')


soup = load_website('https://tiki.vn/',prefix='')    
categories = soup.find_all('a',class_='MenuItem__MenuLink-tii3xq-1 efuIbv')
category, link = [], []
for h in range(len(categories)):
    try:
        link.append(categories[h]['href'])
        category.append(categories[h].text)
    except:
        print('pass')

d = list(zip(category,link))

titles, images, fprice, category, num_reviews, ratings, tikinow = [], [], [], [], [], [], []
for j in range(len(d)):
    try:
        soup = load_website(d[j][1],prefix='')
        articles = soup.find_all('div', class_='product-item')
        print('Reading',d[j][1],sep=' ')
        for k in range(len(articles)):
            try:
                images.append(articles[k].img['src'])
                fprice.append(articles[k].find_all("span",class_="final-price")[0].text.strip().split()[0])
                titles.append(articles[k].a['title'].strip())
                category.append(articles[k]['data-category'].strip())
                num_reviews.append([articles[k].find_all('p',class_='review')[0].text.strip('\(\)') if articles[k].find_all('p',class_='review') != [] else 'Chưa có nhận xét'][0])
                ratings.append([articles[k].find_all('span',class_='rating-content')[0].find('span')['style'].split(':')[1] if articles[k].find_all('span',class_='rating-content') != [] else 'Rating not available'][0])
                tikinow.append(['NO' if articles[k].find_all('i',class_="tikicon icon-tikinow-20") == [] else 'YES'][0])
            except Exception as err:
                print(err,k,sep=' ')
        links = soup.find_all('div',class_='list-pager')        
        while links[0].find_all('a', {"class": "next"}) != []:
            try:
                soup = load_website(links[0].find_all('a', {"class": "next"})[0]['href'],prefix='https://tiki.vn')
                articles = soup.find_all('div', class_='product-item')
                print('Reading',d[j][0],links[0].find_all('a', {"class": "next"})[0]['href'].split('&')[1],sep=' ')
                for i in range(len(articles)):
                    try:
                        images.append(articles[i].img['src'])
                        fprice.append(articles[i].find_all("span",class_="final-price")[0].text.strip().split()[0])
                        titles.append(articles[i].a['title'].strip())
                        category.append(articles[i]['data-category'].strip())
                        num_reviews.append([articles[i].find_all('p',class_='review')[0].text.strip('\(\)') if articles[i].find_all('p',class_='review') != [] else 'Chưa có nhận xét'][0])
                        ratings.append([articles[i].find_all('span',class_='rating-content')[0].find('span')['style'].split(':')[1] if articles[i].find_all('span',class_='rating-content') != [] else 'Rating not available'][0])
                        tikinow.append(['NO' if articles[i].find_all('i',class_="tikicon icon-tikinow-20") == [] else 'YES'][0])
                    except Exception as err:
                        print(err,i,sep=' ')
                links = soup.find_all('div',class_='list-pager')
            except:
                continue
    except:
        continue

d = list(zip(titles, images, fprice, category, num_reviews, ratings, tikinow))

with open('tiki.json', 'w') as file:
    json.dump(d, file)

products = pd.DataFrame(columns=['Title','Price','Image','Category','Number of Reviews','Ratings','TikiNOW'])    
for m in range(len(titles)):
    products = products.append({'Title':titles[m],'Price':fprice[m],'Image':images[m],'Category':category[m],'Number of Reviews':num_reviews[m],'Ratings':ratings[m],'TikiNOW':tikinow[m]},ignore_index=True)

products.to_csv('tiki.csv')