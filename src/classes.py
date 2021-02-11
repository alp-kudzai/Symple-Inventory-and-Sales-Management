# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 09:57:50 2021

@author: Kudzai Matsika alpha.kudzai@gmail.com
"""

#TATENDA'S WIELDING APP

#TODO: save_inventory is not working

class inventory(object):
    '''Superclass'''
    def __init__(self, items):
        # self.filename = filename
        self.items = items
        
    # def get_filename(self):
        # return self.filename
    
    # def change_filename(self, new_filename):
        # self.filename = new_filename
    
    def set_inventory(self, item, price_quantity):
        '''
        Sets a given item to inventory with the specified price & quantity.
        N.B!: item is a string with no spaces, & price_quantity is a list(
            price,quantity)
        E.G: item = set_inventory(100L_Drum, [100, 1] 
        '''
        assert type(item) == str,'Item is not a string'
        assert type(price_quantity) == list, 'Price_quantity is not a list object.'
        if item in self.items:
            if self.items[item][0] == price_quantity[0]:
                self.items[item][1] += price_quantity[1]
            else:
                new_name = '**'+item
                self.items[new_name] = price_quantity
                # raise IndexError(f'That item named, {item} does in inventory has a different price & quantity value.')
                #self.items[item] = price_quantity
        else:
            self.items[item] = price_quantity
    
    def rm_inventory(self, item, price_quantity):
        '''
        Removes a given item with that price_quantity from the inventory
        '''
        #TODO:error!you are checking if the item is in the dictionary but not
        #           if the price is the same
        assert type(item) == str,'Item is not a string!'
        assert type(price_quantity) == list, 'Price_quantity is not a list object!'
        if not (item in self.items):
            raise IndexError('Item is not in the inventory!')
        else:
            if (self.items[item][1] - price_quantity[1]) <= 0:
                self.items.pop(item)
                # raise IndexError('Item is below 0 quantity, its not in inventory Or you are removing to much stuff!')
            else:
                self.items[item][1] -= price_quantity[1]
        
    
    def save_inventory(self, filename):
        '''
        Saves the dictionary items to a file given
        
        '''
        
        inventory = self.items.items()
        output_file = open(filename, 'w')
        for thing in inventory:
            output_file.write(f'{thing[0]} {thing[1][0]} {thing[1][1]}\n')
        output_file.close()
        print('Inventory Saved in file:', filename)
        
        
    
    def load_inventory(self, filename):
        '''
        Loads a file with inventory into the dict items.
        The file must follow the following format:
            E.G: 100L_Drum 100 1
                 11m_steel 50 20
        '''
        inventory_file = open(filename, 'r')
        inventory_data = inventory_file.read().split('\n')
        inventory_file.close()
        print('Loading Inventory....')
        for thing in inventory_data:
            if len(thing) > 0:
                temp = thing.split(' ')
                name, price, quant = temp[0], float(temp[1]), int(temp[2])
                self.items[name] = [price, quant]
        print('Done')
        
    def get_value(self):
        '''
        Returns the total value of items in the inventory.
        '''
        inventory = self.items.items()
        value = 0
        items = 0
        for thing in inventory:
            items +=  thing[1][1]
            value += thing[1][0]*thing[1][1]
        return (items,value)
    
    def get_value_neat(self):
        '''
        Returns a neat display of the number of items
        in inventory and their value
        '''
        inventory = self.items.items()
        value = 0
        items = 0
        for thing in inventory:
            items +=  thing[1][1]
            value += thing[1][0]*thing[1][1]
        res = f'Number of items: {items}\nTotal Value: {value}'
        return res
    
    def get_inventory(self):
        '''
        Returns all the items in inventory(in self.items)
        -------
        None.
        '''
        copy_inventory = self.items.copy()
        return copy_inventory
    
    def neat_inventory(self):
         '''
         displays a neat presentation of inventory
         '''
         res = ''
         inv = self.items.items()
         for thing in inv:
            res += str(thing[0]) +f': R{thing[1][0]} ({thing[1][1]})\n'
         return res[:-1]
    
    def __str__(self):
        res = ''
        inv = self.items.items()
        for thing in inv:
            res += str(thing[0]) +f': R{thing[1][0]} ({thing[1][1]})\n'
        return res[:-1]
    