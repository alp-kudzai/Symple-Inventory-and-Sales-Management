# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 10:33:15 2021

@author: Kudzai Matsika, alpha.kudzai@gmail.com
"""

from classes import *

class Raw_Material(inventory):
    '''
    Intialise with empty LIST
    '''
    def __init__(self, items):
        inventory.__init__(self, items)
        # self.items = items

class Stock(inventory):
    '''
    Intialise with empty LIST
    '''
    def __init__(self, items):
        inventory.__init__(self, items)
        # self.items = items

def Value_Created(Raw_Material, Stock):
    '''
    Raw_Material is the object class Raw_Material.
    Stock is the object class Stock.
    Returns the value created from the manufacturing of the raw material
    to stock.
    '''
    RM_value = Raw_Material.get_value()
    S_value = Stock.get_value()
    value_created = S_value[1] - RM_value[1]
    return value_created

class Sales(object):
    '''
    Intialise with empty LIST
    This object handles the sales of the app.
    It will take a stock object after it has been intialised.
    It will then Remove the sold item from stock, then store the sale with a 
    price.
    '''
    def __init__(self, sales):
        # self.filename = filename
        self.sales = sales
        
    # def get_filename(self):
    #     return self.filename
    
    # def change_filename(self, new_filename):
    #     self.filename = new_filename
        
    def get_sales(self):
        return self.sales.copy()
    
    def neat_sales(self):
        '''
        Displays a neat presentation of the sales
        '''
        res = ''
        s = self.sales.items()
        for thing in s:
            res += str(thing[0]) +f': R{thing[1][0]} ({thing[1][1]})\n'
        return res[:-1]
    
    def make_sale(self, Stock, item, price_quantity):
        '''
        Add the item item to sales at the given price_quantity.
        It then removes the item from the Stock
        If the sale made is for repairs or items not in Stock add an asterick at the
        beginning of the string.
        '''
        #TODO:make sale not sensitive to price given just the name
        #set the item given in self.sales dict
        assert type(item) == str,'Item is not a string'
        assert type(price_quantity) == list, 'Price_quantity is not a list object.'
        if not (item[0] == '*'):
            if item in self.sales:
                if self.sales[item][0] == price_quantity[0]:
                    self.sales[item][1] += price_quantity[1]
                else:
                    new_name = '**'+item
                    self.sales[new_name] = price_quantity
                    # raise IndexError(f'That item named, {item} in Sales has a different price & quantity value.')
                    #self.items[item] = price_quantity
            else:
                self.sales[item] = price_quantity
            #remove the item at the price_quantity from Stock
            Stock.rm_inventory(item, price_quantity)
        else:
            if item in self.sales:
                if self.sales[item][0] == price_quantity[0]:
                    self.sales[item][1] += price_quantity[1]
                else:
                    new_name = '**'+item
                    self.sales[new_name] = price_quantity
                    # raise IndexError(f'That item named, {item} in Sales has a different price & quantity value.')
                    #self.items[item] = price_quantity
            else:
                self.sales[item] = price_quantity
            if not (item[0] == '*'):
                Stock.rm_inventory(item, price_quantity)
    
    def save_sales(self, filename):
        print(f'\nSaving file to {filename}.')
        output_file = open(filename, 'w')
        sales_items = self.sales.items()
        for s in sales_items:
            output_file.write(f'{s[0]} {s[1][0]} {s[1][1]}\n')
        print('Done!')
        output_file.close()
        
    def load_sales(self, filename):
        print(f'\nLoading Sales from {filename}.')
        try:
            input_file = open(filename, 'r')
            sales_data = input_file.read().split('\n')
            input_file.close()
            for s in sales_data:
                thing = s.split(' ')
                name, price, quant = thing[0], float(thing[1]), int(thing[2])
                self.sales[name] = [price, quant]
            print('Done\n')
        except:
            pass
        
    def rm_sales(self, item, price_quantity):
        '''
        Removes an item from self.sales
        '''
        if item in self.sales:
            if self.sales[item][0] == price_quantity[0] \
            and (self.sales[item][1] - price_quantity[1]) > 0:
                self.sales[item][1] -= price_quantity[1]
            elif self.sales[item][0] == price_quantity[0] \
            and (self.sales[item][1] - price_quantity[1]) <= 0:
                self.sales.pop(item)
            else:
                raise ValueError(f'{item} does not have the given price!')
        else:
            raise IndexError(f'{item} is not in sales!')
        
    def get_value(self):
        sales = self.sales.items()
        value = 0
        items = 0
        for thing in sales:
            items +=  thing[1][1]
            value += thing[1][0]*thing[1][1]
        return (items,value)
    
    def get_value_neat(self):
        '''
        Returns a neat display of the number of items
        in sales and their value
        '''
        sales = self.sales.items()
        value = 0
        items = 0
        for thing in sales:
            items +=  thing[1][1]
            value += thing[1][0]*thing[1][1]
        res = f'Number of items Sold: {items}\nTotal Value: {value}'
        return res
    
    
    def __str__(self):
        res = ''
        s = self.sales.items()
        for thing in s:
            res += str(thing[0]) +f': R{thing[1][0]} ({thing[1][1]})\n'
        return res[:-1]
        
        