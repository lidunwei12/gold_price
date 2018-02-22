# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 16:21:28 2017

@author: bob.lee
"""
from src.data_collation import data_coll
from src.data_collation import data_handle
from src.train import train_lstm
from src.train import prediction
date_end = time.strftime('%Y/%m/%d', time.localtime(time.time()))
file_name = data_coll('2008/01/01', date_end)
data = data_handle(file_name)
train_lstm(data)
prediction(data)
