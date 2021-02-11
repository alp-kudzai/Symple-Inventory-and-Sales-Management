# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 13:11:55 2021

@author: Kudzai Matsika alpha.kudzai@gmail.com
"""
from subclasses import *

#TODO:add more test cases
#TODO: add get_filename and change_filename()

#Lets test every method in inventory class except load_inventory and save_inventory
#start with objects in classes.py
def test_create_inventory(checker=False):
    print('\nCreating inventory...')
    try:
        inventory_items = {'metal_pipe': [20, 5],
                           '100L_Drum': [250, 1],
                           'metal_mash': [40, 4],
                           'paint': [100, 2]}
        Inventory = inventory({})
        #set inventory
        for thing in inventory_items.items():
            name, price_quantity = thing[0], thing[1]
            Inventory.set_inventory(name, price_quantity)
        print('Created inventory!')
        print('Testing Method: set_inventory()')
        if Inventory.get_inventory() == inventory_items:
            print('PASSED!')
            checker = True
    except:
        print('Failed to create inventory!')
        
    if checker == True:
        return checker
    else:
        print('FAILED!')
        return checker
    
def test_rm_inventory(checker=False):
    print('\nTesting Method: inventory.rm_inventory().')
    try:
        expected_result = {'100L_Drum': [250, 1],
                            'metal_mash': [40, 1],
                            'paint': [100, 1]}
        inventory_items = {'metal_pipe': [20, 5],
                            '100L_Drum': [250, 1],
                            'metal_mash': [40, 4],
                            'paint': [100, 2]}
        #we remove 3 metal_mash, 1 paint, and 5 metal_pipes
        itemsToremove = {'metal_pipe': [20, 5],
                          'paint': [100, 1],
                          'metal_mash': [40, 3]}
        
        rm_Inventory = inventory({})
        #set inventory
        for thing in inventory_items.items():
            name, price_quantity = thing[0], thing[1]
            rm_Inventory.set_inventory(name, price_quantity)
        # removing items
        # print(rm_Inventory.get_inventory())
        for thing in itemsToremove.items():
            name, price_quantity = thing[0], thing[1]
            rm_Inventory.rm_inventory(name, price_quantity)
        #test against expected_result
        # print(Inventory.get_inventory())
        # print()
        # print(expected)
        if rm_Inventory.get_inventory() == expected_result:
            print('PASSED!')
            checker = True
        else:
            print('FAILED!')
    except:
        print('ERROR!')
        
    finally:
        return checker
    
def test_inventory_value(checker=False):
    print('\nCreating inventory...')
    try:
        inventory_items = {'metal_pipe': [20, 5],
                           '100L_Drum': [250, 1],
                           'metal_mash': [40, 4],
                           'paint': [100, 2]}
        expected_result = (12, 710)
        Inventory = inventory({})
        #set inventory
        for thing in inventory_items.items():
            name, price_quantity = thing[0], thing[1]
            Inventory.set_inventory(name, price_quantity)
        print('Created inventory!')
        print('Testing Method: get_value()')
        if Inventory.get_value() == expected_result:
            print('PASSED!')
            checker = True
        else:
            print('FAILED!')
    except:
        print('ERROR!')
    finally:
        return checker
    
def test_rm_raw(checker=False):
    print('\nTesting Method: Raw_Material.rm_inventory().')
    try:
        inventory_items = {'metal_pipe': [20, 5],
                           '100L_Drum': [250, 1],
                           'metal_mash': [40, 4],
                           'paint': [100, 2]}
        #we remove 3 metal_mash, 1 paint, and 5 metal_pipes
        itemsToremove = {'metal_pipe': [20, 5],
                         'paint': [100, 1],
                         'metal_mash': [40, 3]}
        expected_result = {'100L_Drum': [250, 1],
                           'metal_mash': [40, 1],
                           'paint': [100, 1]}
        rawM = Raw_Material({})
        #set inventory
        for thing in inventory_items.items():
            name, price_quantity = thing[0], thing[1]
            rawM.set_inventory(name, price_quantity)
        #removing items
        for thing in itemsToremove.items():
            name, price_quantity = thing[0], thing[1]
            rawM.rm_inventory(name, price_quantity)
        #test against expected_result
        if rawM.get_inventory() == expected_result:
            print('PASSED!')
            checker = True
        else:
            print('FAILED!')
    except:
        print('ERROR!')
        
    finally:
        return checker
    
def test_rawM_value(checker=False):
    print('\nCreating inventory...')
    try:
        inventory_items = {'metal_pipe': [20, 5],
                           '100L_Drum': [250, 1],
                           'metal_mash': [40, 4],
                           'paint': [100, 2]}
        expected_result = (12, 710)
        rawM = Raw_Material({})
        #set inventory
        for thing in inventory_items.items():
            name, price_quantity = thing[0], thing[1]
            rawM.set_inventory(name, price_quantity)
        print('Created inventory!')
        print('Testing Method: Raw_Material.get_value()')
        if rawM.get_value() == expected_result:
            print('PASSED!')
            checker = True
        else:
            print('FAILED!')
    except:
        print('ERROR!')
    finally:
        return checker

def test_print_rawM(checker=False):
    print('\nCreating inventory...')
    try:
        inventory_items = {'metal_pipe': [20, 5],
                           '100L_Drum': [250, 1],
                           'metal_mash': [40, 4],
                           'paint': [100, 2]}
        rawM = Raw_Material({})
        #set inventory
        for thing in inventory_items.items():
            name, price_quantity = thing[0], thing[1]
            rawM.set_inventory(name, price_quantity)
        print('Created inventory!')
        print(rawM)
    except:
        print('ERROR!')
        
def test_rm_stock(checker=False):
    print('\nTesting Method: Stock.rm_inventory().')
    try:
        inventory_items = {'metal_pipe': [20, 5],
                           '100L_Drum': [250, 1],
                           'metal_mash': [40, 4],
                           'paint': [100, 2]}
        #we remove 3 metal_mash, 1 paint, and 5 metal_pipes
        itemsToremove = {'metal_pipe': [20, 5],
                         'paint': [100, 1],
                         'metal_mash': [40, 3]}
        expected_result = {'100L_Drum': [250, 1],
                           'metal_mash': [40, 1],
                           'paint': [100, 1]}
        stock = Stock({})
        #set inventory
        for thing in inventory_items.items():
            name, price_quantity = thing[0], thing[1]
            stock.set_inventory(name, price_quantity)
        #removing items
        for thing in itemsToremove.items():
            name, price_quantity = thing[0], thing[1]
            stock.rm_inventory(name, price_quantity)
        #test against expected_result
        if stock.get_inventory() == expected_result:
            print('PASSED!')
            checker = True
        else:
            print('FAILED!')
    except:
        print('ERROR!')
        
    finally:
        return checker
    
def test_stock_value(checker=False):
    print('\nCreating inventory...')
    try:
        inventory_items = {'metal_pipe': [20, 5],
                           '100L_Drum': [250, 1],
                           'metal_mash': [40, 4],
                           'paint': [100, 2]}
        expected_result = (12, 710)
        stock = Stock({})
        #set inventory
        for thing in inventory_items.items():
            name, price_quantity = thing[0], thing[1]
            stock.set_inventory(name, price_quantity)
        print('Created inventory!')
        print('Testing Method: stock_get_value()')
        if stock.get_value() == expected_result:
            print('PASSED!')
            checker = True
        else:
            print('FAILED!')
    except:
        print('ERROR!')
    finally:
        return checker
    
def test_print_stock():
    print('\nCreating inventory...')
    try:
        inventory_items = {'metal_pipe': [20, 5],
                           '100L_Drum': [250, 1],
                           'metal_mash': [40, 4],
                           'paint': [100, 2]}
        stock = Stock({})
        #set inventory
        for thing in inventory_items.items():
            name, price_quantity = thing[0], thing[1]
            stock.set_inventory(name, price_quantity)
        print('Created inventory!')
        print(stock)
    except:
        print('ERROR!')

#test Sales        
def test_makeSale(toprint=True):
    if toprint:
        print('\nCreating Stock...')
    try:
        inventory_items = {'Braai_Stand': [800, 2],
                           'Hoe': [100, 5],
                           'Burglar_Bar': [300, 4]}
        itemsTosale = {'Braai_Stand': [800, 1],
                       '*Stuff_repairs': [200, 1],
                       'Hoe': [100, 1],
                       'Burglar_Bar': [300, 2]}
        expected_inventory = {'Braai_Stand': [800, 1],
                              'Hoe': [100, 4],
                              'Burglar_Bar': [300, 2]}
        stock = Stock({})
        #set inventory
        for thing in inventory_items.items():
            name, price_quantity = thing[0], thing[1]
            stock.set_inventory(name, price_quantity)
        print(stock.get_inventory())
        if toprint:
            print('Created Stock!')
            print('Testing Method: Sales.make_sale()')
        sales = Sales({})
        for thing in itemsTosale.items():
            name, price_quantity = thing[0], thing[1]
            sales.make_sale(stock, name, price_quantity)
        if toprint:
            # print(stock.get_inventory())
            # print(expected_inventory)
            if (stock.get_inventory() == expected_inventory) and (sales.get_sales() == itemsTosale):
                print('PASSED!')
            else:
                if toprint:
                    print('FAILED!')
        else:
            return stock, sales
        
        
    except:
        print('ERROR!')
    
def test_rm_sales():
    print('\nTesting Method: Sales.rm_sales(item, price_quantity)')
    stock, sales = test_makeSale(toprint=False)
    itemsToremoves = {'Braai_Stand': [800, 1],
                      'Burglar_Bar': [300, 1]}
    expected_result = {'*Stuff_repairs': [200, 1],
                       'Hoe': [100, 1],
                       'Burglar_Bar': [300, 1]}
    try:
        for thing in itemsToremoves.items():
            sales.rm_sales(thing[0], thing[1])
        if sales.get_sales() == expected_result:
            print('PASSED!')
        else:
            print('FAILED!')
    except:
        print('ERROR!')
        
def test_sales_get_value():
    print('\nTesting Method: Sales.get_value(item, price_quantity)')
    stock, sales = test_makeSale(toprint=False)
    expected_result = (5, 1700)
    try:
        if sales.get_value() == expected_result:
            print('PASSED!')
        else:
            print('FAILED!')
    except:
        print('ERROR!')

def full_test():
    print('****************************************************')
    test_create_inventory()
    print('****************************************************')
    test_rm_inventory()
    print('****************************************************')
    test_inventory_value()
    print('****************************************************')
    test_rm_raw()
    print('****************************************************')
    test_rawM_value()
    print('****************************************************')    
    test_print_rawM()
    print('****************************************************')
    test_rm_stock()
    print('****************************************************')
    test_stock_value()
    print('****************************************************')
    test_print_stock()
    print('****************************************************')
    test_makeSale()
    print('****************************************************')
    test_rm_sales()
    print('****************************************************')
    test_sales_get_value()
    print('****************************************************')
    
if __name__ == '__main__':
    print('--------------TESTING CLASSES--------------')
    full_test()
    