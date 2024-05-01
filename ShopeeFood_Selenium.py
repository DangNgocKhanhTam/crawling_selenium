from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from my_lib import *
import os 
import pandas as pd
import time 



driver = webdriver.Chrome()
driver.maximize_window()
url = 'https://shopeefood.vn/ho-chi-minh/food/danh-sach-dia-diem-phuc-vu-food-tai-khu-vuc-quan-1-giao-tan-noi'
driver.get(url)


list_restaurant_link = []
load_more = driver.find_elements(by=By.XPATH, value = '//ul[@class = "pagination"]//a')
for page in load_more[1:-1]: 
        print(page)
        page.click()
        container_list_product = driver.find_element(By.CLASS_NAME, value = 'list-restaurant')
        tag_restaurant_link = driver.find_elements(by= By.XPATH, value = '//div[@class = "item-restaurant"]/a[@class = "item-content"]')
        for link in tag_restaurant_link: 
                restaurant_link = link.get_attribute('href')
                list_restaurant_link.append(restaurant_link)
        time.sleep(1.5)

# Wrire file link_restaurant for back up

list_link = []
file_link = 'link.txt'
for link in list_restaurant_link:
    list_link.append(link + '\n')
write_txt(file_link, list_link)

# Crawling 

list_restaurant_name = []
list_address_restaurant = []
list_stars = []
list_open_time = []
list_cost_restaurant = []
list_cost_service = []
list_voucher = []
df= {}
count = 0

driver_restaurant_details = webdriver.Chrome()
driver_restaurant_details.maximize_window()

for restaurant_link in list_restaurant_link:
    url =restaurant_link
    driver_restaurant_details.get(url)
    time.sleep(1.5)

    # Restaurant Name
    tag_restaurant_name = driver_restaurant_details.find_element(by= By.XPATH, value = '//h1[@class = "name-restaurant"]')
    restaurant_name = tag_restaurant_name.get_attribute('textContent') 
    list_restaurant_name.append(restaurant_name)

    # Address Restaurant
    tag_address_restaurant = driver_restaurant_details.find_element(by= By.XPATH, value = '//div[@class = "address-restaurant"]')
    address_restaurant = tag_address_restaurant.get_attribute('textContent')
    list_address_restaurant.append(address_restaurant)    

    # Stars
    tag_rating = driver_restaurant_details.find_elements(by= By.XPATH, value = '//div[@class = "stars"]/span')
    stars = 0
    for rating in tag_rating:
        if rating.get_attribute('class') == 'full': 
            stars += 1
        if rating.get_attribute('class') == 'half':
            stars += 0.5
    list_stars.append(stars)

    # Open Time
    tag_open_time = driver_restaurant_details.find_element(by= By.XPATH, value = '//div[@class = "time"]')
    open_time = tag_open_time.get_attribute('textContent')
    list_open_time.append(open_time)
    
    # Cost Restaurant 
    tag_cost_restaurant = driver_restaurant_details.find_element(by= By.XPATH, value = '//div[@class = "cost-restaurant"]')
    cost_restaurant = tag_cost_restaurant.get_attribute('textContent')
    list_cost_restaurant.append(cost_restaurant)

    # Cost Service 
    tag_cost_service = driver_restaurant_details.find_element(by= By.XPATH, value = '//div[@class = "utility-content"]/span')
    cost_service = tag_cost_service.get_attribute('textContent')
    list_cost_service.append(cost_service)

    # Voucher
    tag_voucher  = driver_restaurant_details.find_element(by= By.XPATH, value =  '//div[@id = "promotion-item"]//div[@class = "content"]')
    voucher = tag_voucher.get_attribute('textContent')
    list_voucher.append(voucher)
    

    count += 1
    print(f'{count}: {restaurant_name}')
    

else: 
    driver_restaurant_details.close()
    
    df= pd.DataFrame({
        'restaurant_name': list_restaurant_name, 
        'address_restaurant': list_address_restaurant, 
        'stars': list_stars, 
        'open_time': list_open_time, 
        'cost_restaurant': list_cost_restaurant, 
        'cost_service': list_cost_service, 
        'voucher': list_voucher, 
        'restaurant_link': list_restaurant_link
    })

    data_folder = 'crawling'
    if not os.path.exists(data_folder): 
        os.makedirs(data_folder)
    df_shopee_food = df.to_csv(f'{data_folder}/ShopeeFood.csv', index= False)
    print('> Done!!!')

