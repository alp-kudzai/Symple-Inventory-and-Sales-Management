# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 14:47:57 2021

@author: Kudzai
"""
from classes import *

stock = inventory({})
stock.load_inventory('inv.txt')
print(stock)


print('\nSetting stock')
pq1 = [75, 1]
stock.set_inventory('stuff', pq1)
print(stock.get_inventory())

print('\nTesting the Value')
items_value = stock.get_value()
print(f'Number of items in inventory: {items_value[0]}\n' +
      f'Value of inventory: {items_value[1]}.')

# print('\nTesting Remove')
# pq2 = [75,74]
# stock.rm_inventory('stuff', pq2)
# print(stock.get_inventory())

# print('Stock\n',stock)

print('\nTesting Saving')
stock.save_inventory('inv.txt')

print('\nDone Testing')


