from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pprint import pprint
from sys import exit
from datetime import datetime,timedelta,date
import mysql.connector

#Import ASCII Text Library
from termcolor import cprint 
from pyfiglet import figlet_format

#print nice title
cprint(figlet_format('lets', font='starwars'),'blue', attrs=['blink'])
cprint(figlet_format('scrap', font='starwars'),'blue', attrs=['bold'])

PATH = "D:\Youtube\Python Projects\WebScrapingProjects\ScrapingWeather\chromedriver\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(PATH,options=options)

driver.get("https://simpleicons.org/")
#remove the ad element
element_ad = driver.find_element_by_class_name('grid-item--ad')
driver.execute_script("""
var element_ad = arguments[0];
element_ad.parentNode.removeChild(element_ad);
""", element_ad)

element_empty = driver.find_element_by_class_name('grid-item--if-empty')
driver.execute_script("""
var element_empty = arguments[0];
element_empty.parentNode.removeChild(element_empty);
""", element_empty)

badge_body = driver.find_element_by_xpath('/html/body/main/ul')
badge_list = badge_body.find_elements_by_tag_name("li")

for bl in badge_list:
    icon_name_array = bl.find_element_by_tag_name("a").text.split()

    icon_name = icon_name_array[0]
    hex_code = bl.find_element_by_tag_name("p").text.replace("#","")
    print("https://img.shields.io/badge/-"+icon_name+"-"+hex_code+"?logo="+icon_name+"&labelColor="+hex_code)