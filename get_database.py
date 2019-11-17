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
categories = soup.find_all('a',{"class":'MenuItem__MenuLink-tii3xq-1 efuIbv'})
category, link = [], []
for h in range(len(categories)):
    try:
        link.append(categories[h]['href'])
        category.append(categories[h].text)
    except:
        print('pass')

d = list(zip(category,link))

titles, images, fprice, category, num_reviews, ratings, tikinow, seller, rprice, discount = [], [], [], [], [], [], [], [], [], []
for j in range(len(d)):
    try:
        soup = load_website(d[j][1],prefix='')
        articles = soup.find_all('div', {"class":'product-item'})
        print('Reading '+d[j][1])
        for k in range(len(articles)):
            try:
                images.append(articles[k].img['src'])
                fprice.append(articles[k].find_all("span",{"class":"final-price"})[0].text.strip().split()[0])
                rprice.append(articles[k].find_all("span",{"class":"price-regular"})[0].text)
                discount.append(['None' if len(articles[k].find_all("span",{"class":"final-price"})[0].text.strip().split()) == 1 else articles[k].find_all("span",{"class":"final-price"})[0].text.strip().split()[1]][0])
                seller.append(articles[k]['data-brand'])
                titles.append(articles[k].a['title'].strip())
                category.append(articles[k]['data-category'].strip())
                num_reviews.append([articles[k].find_all('p',{"class":'review'})[0].text.strip('\(\)') if articles[k].find_all('p',{"class":'review'}) != [] else 'Chưa có nhận xét'][0])
                ratings.append([articles[k].find_all('span',{"class":'rating-content'})[0].find('span')['style'].split(':')[1] if articles[k].find_all('span',{"class":'rating-content'}) != [] else 'Rating not available'][0])
                tikinow.append(['NO' if articles[k].find_all('i',{"class":"tikicon icon-tikinow-20"}) == [] else 'YES'][0])
                
                products['image'].append(articles[k].img['src'])
                products['fprice'].append(articles[k].find_all("span",{"class":"final-price"})[0].text.strip().split()[0])
                products['rprice'].append(articles[k].find_all("span",{"class":"price-regular"})[0].text)
                products['discount'].append(['None' if len(articles[k].find_all("span",{"class":"final-price"})[0].text.strip().split()) == 1 else articles[k].find_all("span",{"class":"final-price"})[0].text.strip().split()[1]][0])
                products['seller'].append(articles[k]['data-brand'])
                products['titles'].append(articles[k].a['title'].strip())
                products['category'].append(articles[k]['data-category'].strip())
                products['num_reviews'].append([articles[k].find_all('p',{"class":'review'})[0].text.strip('\(\)') if articles[k].find_all('p',{"class":'review'}) != [] else 'Chưa có nhận xét'][0])
                products['ratings'].append([articles[k].find_all('span',{"class":'rating-content'})[0].find('span')['style'].split(':')[1] if articles[k].find_all('span',{"class":'rating-content'}) != [] else 'Rating not available'][0])
                products['tikinow'].append(['NO' if articles[k].find_all('i',{"class":"tikicon icon-tikinow-20"}) == [] else 'YES'][0])
            except Exception as err:
                print(err,k,sep=' ')
                
        # Read next page cursor at the bottom of a product page        
        links = soup.find_all('div',{"class":'list-pager'})  
        
        #While next page cursor is not empty, read next page cursor to move to next product page
        while links[0].find_all('a', {"class": "next"}) != []:
            try:
                soup = load_website(links[0].find_all('a', {"class": "next"})[0]['href'],prefix='https://tiki.vn')
                articles = soup.find_all('div', class_='product-item')
                print('Reading',d[j][0],links[0].find_all('a', {"class": "next"})[0]['href'].split('&')[1],sep=' ')
                for i in range(len(articles)):
                    try:
                        images.append(articles[i].img['src'])
                        fprice.append(articles[i].find_all("span",{"class":"final-price"})[0].text.strip().split()[0])
                        rprice.append(articles[i].find_all("span",{"class":"price-regular"})[0].text)
                        discount.append(['None' if len(articles[i].find_all("span",{"class":"final-price"})[0].text.strip().split()) == 1 else articles[i].find_all("span",{"class":"final-price"})[0].text.strip().split()[1]][0])
                        seller.append(articles[i]['data-brand'])
                        titles.append(articles[i].a['title'].strip())
                        category.append(articles[i]['data-category'].strip())
                        num_reviews.append([articles[i].find_all('p',{"class":'review'})[0].text.strip('\(\)') if articles[i].find_all('p',{"class":'review'}) != [] else 'Chưa có nhận xét'][0])
                        ratings.append([articles[i].find_all('span',{"class":'rating-content'})[0].find('span')['style'].split(':')[1] if articles[i].find_all('span',{"class":'rating-content'}) != [] else 'Rating not available'][0])
                        tikinow.append(['NO' if articles[i].find_all('i',{"class":"tikicon icon-tikinow-20"}) == [] else 'YES'][0])
                        
                        products['image'].append(articles[i].img['src'])
                        products['fprice'].append(articles[i].find_all("span",{"class":"final-price"})[0].text.strip().split()[0])
                        products['rprice'].append(articles[i].find_all("span",{"class":"price-regular"})[0].text)
                        products['discount'].append(['None' if len(articles[i].find_all("span",{"class":"final-price"})[0].text.strip().split()) == 1 else articles[i].find_all("span",{"class":"final-price"})[0].text.strip().split()[1]][0])
                        products['seller'].append(articles[i]['data-brand'])
                        products['titles'].append(articles[i].a['title'].strip())
                        products['category'].append(articles[i]['data-category'].strip())
                        products['num_reviews'].append([articles[i].find_all('p',{"class":'review'})[0].text.strip('\(\)') if articles[i].find_all('p',{"class":'review'}) != [] else 'Chưa có nhận xét'][0])
                        products['ratings'].append([articles[i].find_all('span',{"class":'rating-content'})[0].find('span')['style'].split(':')[1] if articles[i].find_all('span',{"class":'rating-content'}) != [] else 'Rating not available'][0])
                        products['tikinow'].append(['NO' if articles[i].find_all('i',{"class":"tikicon icon-tikinow-20"}) == [] else 'YES'][0])
                    except Exception as err:
                        print(err,i,sep=' ')
                links = soup.find_all('div',{"class":'list-pager'})
            except:
                continue
    except:
        continue
print("SUCCESS!")

e = list(zip(titles, images, seller, rprice, discount, fprice, category, num_reviews, ratings, tikinow))

with open('tiki_1.json', 'w') as file:
    json.dump(e, file)

products.to_csv('tiki_1.csv')