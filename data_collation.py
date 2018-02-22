# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 16:21:28 2017

@author: bob.lee
"""
from selenium import webdriver
import time
import re
import numpy as np
from lxml import etree


def data_coll(date_start, data_end):
    """
    dat输入格式'2016/08/24'
    最终结果保存在price.txt
    """
    try:
        driver = webdriver.Chrome()
        driver.get("https://cn.investing.com/commodities/gold-historical-data")
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="flatDatePickerCanvasHol"]').click()
        driver.find_element_by_id('startDate').clear()
        driver.find_element_by_id('startDate').send_keys(date_start)
        driver.find_element_by_id('endDate').clear()
        driver.find_element_by_id('endDate').send_keys(data_end)
        driver.find_element_by_id('applyBtn').click()
        time.sleep(15)
        with open("price_data.txt", "a", encoding='utf-8') as f:
            f.write(driver.find_element_by_xpath('//*[@id="curr_table"]').text)
    except Exception as e:
        print(e)
    return "price_data.txt"
driver = webdriver.Chrome()
driver.get('https://www.vmovier.com/series/45?from=series_list')
# video = etree.HTML(self.driver.page_source).xpath( '///*[@id="youku-playerBox"]/div[1]/video')
for element in driver.find_elements_by_xpath('//*[@id="youku-playerBox"]/div[1]/video'):
    img_url = element.get_attribute('src')
    print(img_url)#//*[@id="iframeId"]
# print(driver.find_element_by_xpath('//*[@id="main-container"]').text)
def number_find(extent, content):
    re_words = re.compile(extent)
    result = re.findall(re_words, content)
    result = "".join(result)
    return result


def text_find(key_word, content):
    location = []
    for i in re.finditer(key_word, content):
        location.append(i.span()[0])
    return location


def data_handle(file_name):
    price = []
    for line in open(file_name, encoding='utf-8'):
        location = text_find(' ', line)
        if len(location) == 6:
            result = line[location[0]:location[1]]
            price.append(number_find("[\d\.]+", result))
    while '' in price:
        price.remove('')
    price = list(reversed(price))
    for i in range(len(price)):
        price[i] = float(price[i])
    normalize_data = (price-np.mean(price))/np.std(price)  # 标准化
    normalize_data = normalize_data[:, np.newaxis]
    return normalize_data