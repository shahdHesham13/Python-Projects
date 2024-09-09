from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


# Function to extract Product Title
def get_title(soup):

    try:
        title = soup.find("span", attrs={"id":'productTitle'})
        title_string = title.text.strip()

    except AttributeError:
        title_string = ""

    return title_string


# Function to extract Product Price
def get_price(soup):

    try:
        price = soup.find("span", attrs={'id':'priceblock_ourprice'}).string.strip()

    except AttributeError:
        try:
             # in case of deal price
            price = soup.find("span", attrs={'id':'priceblock_dealprice'}).string.strip()
        except:
            price = ""

    return price


# Function to extract Product Rating
def get_rating(soup):

    try:
        rating = soup.find("i", class_ = 'a-icon a-icon-star a-star-4-5').string.strip()
    
    except AttributeError:
        try:
            rating = soup.find("span", class_ = 'a-icon-alt').string.strip()
        except:
            rating = ""	

    return rating

# Function to extract Number of Reviews
def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()

    except AttributeError:
        review_count = ""	

    return review_count


# Function to extract Availability
def get_availability(soup):
    try:
        available = soup.find("div", attrs={'id':'availability'})
        available = available.find("span").string.strip()

    except AttributeError:
        available = "Not Available"	

    return available



if __name__ == '__main__':

    Header = ({'User-Agent':'', 'Accept-Language': 'en-US, en;q=0.5'})
    URL = "https://www.amazon.com/s?k=makeup&crid=8VE50JUX51W8&sprefix=make%2Caps%2C235&ref=nb_sb_ss_ts-doa-p_1_4"
    page = requests.get(URL, headers=Header)
    soup = BeautifulSoup(page.content, "html.parser")

    # to get all the 'a' tags in the page under that class
    links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})

    links_list = []

    # Loop to extract the link of the product from each tag and add each individual link of the products in list
    for link in links:
            links_list.append(link.get('href'))

    dict = {"title":[], "price":[], "rating":[], "reviews":[],"availability":[]}
    
    # Loop across the list to extract each product details from its link 
    for link in links_list:
        new_webpage = requests.get("https://www.amazon.com" + link, headers=Header)

        new_soup = BeautifulSoup(new_webpage.content, "html.parser")

        # calling the information functions
        dict['title'].append(get_title(new_soup))
        dict['price'].append(get_price(new_soup))
        dict['rating'].append(get_rating(new_soup))
        dict['reviews'].append(get_review_count(new_soup))
        dict['availability'].append(get_availability(new_soup))

    
    amazon_data = pd.DataFrame.from_dict(dict)
    amazon_data['title'].replace('', np.nan, inplace=True)
    amazon_data = amazon_data.dropna(subset=['title'])
    amazon_data.to_csv("amazon_data.csv", header=True, index=False)



print(amazon_data)