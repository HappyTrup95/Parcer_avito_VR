from pickle import TRUE
from selenium import webdriver
import time
import datetime
import requests
from random import randint

def tg_bot(ad_url1,sait,avto_name,avto_price):
    g=0

    for proverka_sait in sait:
        if proverka_sait==ad_url1:
            g+=1        

    if g==0:
        sait.append(ad_url1)
        base_url='http://api.telegram.org/bot5183475207:AAHJVgxcqk4ptQz-Iz0Z-rcGcTWXiAxs6mU/sendMessage?chat_id=-657570594&text="{}"'.format("Новый авто: " + avto_name + "\n Цена - " + avto_price + "\n Ссылка:" + ad_url1)
        requests.get(base_url)

def load_price_saita():
    
    driver.implicitly_wait(5)

    driver.switch_to.window(driver.window_handles[1])
    driver.implicitly_wait(5)

                    
    ad_url1=driver.current_url  

    avto_name = driver.find_element_by_class_name("title-info-title-text")
    avto_name = avto_name.text

    avto_price = driver.find_element_by_class_name("js-item-price")
    avto_price = avto_price.text

    tg_bot(ad_url1,sait,avto_name,avto_price)

    driver.close()
    driver.implicitly_wait(5)   
    driver.switch_to.window(driver.window_handles[0])
    return()

#Доработать функцию отлова ошибки на сайте
#def proverka_na_oshibku():
    #try:
        #id_find = [x.get_attribute("id") for x in driver.find_elements_by_xpath("//div[@data-marker='item']")]
    #except:
        #driver.get("https://www.avito.ru/volgograd/avtomobili/s_probegom-ASgBAgICAUSGFMjmAQ?f=ASgBAQICAUSGFMjmAQFAptoOFAI&radius=100&s=104&user=1")
     
# options
options = webdriver.ChromeOptions()

# for ChromeDriver version 79.0.3945.16 or over
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(executable_path="brauser\\chromedriver.exe",options=options)

try:
    #start_time = datetime.datetime.now()

    driver.get("https://www.avito.ru/volgograd/avtomobili/s_probegom-ASgBAgICAUSGFMjmAQ?f=ASgBAQICAUSGFMjmAQFAptoOFAI&radius=100&s=104&user=1")  
    url = "https://www.avito.ru/volgograd/avtomobili/s_probegom-ASgBAgICAUSGFMjmAQ?f=ASgBAQICAUSGFMjmAQFAptoOFAI&radius=100&s=104&user=1"
    driver.implicitly_wait(5)
    i = 0
    base_url1 = []
    ad_url1 = []        
    sait=[]
    driver.implicitly_wait(5)   
    id_find = [x.get_attribute("id") for x in driver.find_elements_by_xpath("//div[@data-marker='item']")]
    while True:

        #proverka_na_oshibku()      
   
        while i<60:

            #proverka_na_oshibku()

            id_find1 = driver.find_elements_by_xpath("//div[@data-marker='item']")            
            title = id_find1[i].get_attribute("id")            

            if title not in id_find:

                items = driver.find_elements_by_xpath("//div[@data-marker='item-photo']")          
                items[i].click()

                load_price_saita()

                i+=1               
            else:
                i=60
        id_find = [x.get_attribute("id") for x in driver.find_elements_by_xpath("//div[@data-marker='item']")]        
        driver.get("https://www.avito.ru/volgograd/avtomobili/s_probegom-ASgBAgICAUSGFMjmAQ?f=ASgBAQICAUSGFMjmAQFAptoOFAI&radius=100&s=104&user=1")        
        time.sleep(randint(10,100))

        i=0       
  
except Exception as ex:

    print(ex)

finally:

    driver.close()
    driver.quit()

