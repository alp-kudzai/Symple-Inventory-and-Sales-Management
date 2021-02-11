#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 13:16:49 2021

@author: Kudzai Matsika, alpha.kudzai@gmail.com
"""
from subclasses import *
import PySimpleGUI as sg

rawM_filename = 'raw_mat.txt'
stck_filename = 'stock.txt'
sales_filename = 'sales.txt'

def split_input(tats_input):
    '''
    Splits the input given by tats
    Eg: Braai_Stand 800 2
    '''
    data = tats_input.split(' ')
    name, price, quant  = str(data[0]), float(data[1]), int(data[2])
    return name, price, quant

def main_gui_program():

    #TODO: add commands to get filname and change filename
    commands = ('Load Default Data Files','Save To Deflaut Data Files', 'Load RawM File', 'Load Stock File', 'Load Sales File',
                'Save RawM to File', 'Save Stock to File', 'Save Sales to File',
                'Get Raw Material', 'Get Stock', 
                'Get Sales', 'Get Stock Value', 'Get RawM Value', 'Get Sales Value',
                'Set Raw Material', 'Set Stock', 'Sell Item/Service',
                'Remove Raw Material', 'Remove Stock', 'Remove Sales Item/Service'
                )
    sg.theme('DarkAmber')
    layout = [ [sg.Text('Welcome to Symple, your personal stock management and sales system.\n',size=(80, 5), key='-INFO-')],
               [sg.Input(do_not_clear=False, size=(50, 1), key='-INPUT-'), sg.Button('Submit!')],
               [sg.InputCombo(commands,size=(35,1), default_value='Program Commands', enable_events=True, key='-COMMANDS-')],
               [sg.Multiline(size=(80,20), visible=True, key='-OUTPUT-')], 
               [sg.Button('EXIT')]
        ]
    window = sg.Window('SYMPLE, Stock Management and Sales System', layout, alpha_channel=1.666, resizable=True)
    RMAT = Raw_Material({})
    STCK = Stock({})
    SLS = Sales({})
    # event, values = window.read()
    while True:
        event, values = window.read()
        if event == 'EXIT' or event == sg.WIN_CLOSED:
            break
        # if event == 'OK':
            #we check if anything happened in the commands
        cmds = values['-COMMANDS-']
        #Loading deflaut files#################################################
        if cmds == 'Load Default Data Files':
            window['-INFO-'].update('Loading Data from deflault files')
            
            try:
                RMAT.load_inventory(rawM_filename)
                STCK.load_inventory(stck_filename)
                SLS.load_sales(sales_filename)
                window['-INFO-'].update('Data Loaded')
            except:
                window['-INFO-'].update('ERROR: Could not load data!')  
        elif cmds == 'Save To Deflaut Data Files':
            window['-INFO-'].update('Saving Data to Deflaut Files.')
            try:
                RMAT.save_inventory(rawM_filename)
                STCK.save_inventory(stck_filename)
                SLS.save_sales(sales_filename)
                window['-INFO-'].update('Data Saved')
            except:
                window['-INFO-'].update('ERROR: Could not save data!')
        #Adding individual loading and saving of files#########################
        elif cmds == 'Load RawM File':
            window['-INFO-'].update('Please enter the Raw Material file.\n'\
                                    'Eg: raw_mat.txt')
        elif cmds == 'Load Stock File':
            window['-INFO-'].update('Please enter the Stock file.\n'\
                                    'Eg: stock.txt')
        elif cmds == 'Load Sales File':
            window['-INFO-'].update('Please enter the Sales file.\n'\
                                    'Eg: sales.txt')
        elif cmds == 'Save RawM to File':
            window['-INFO-'].update('Please enter the RawM file to save to.\n'\
                                    'Eg: raw_mat.txt')
        elif cmds == 'Save Stock to File':
            window['-INFO-'].update('Please enter the Stock file to save to.\n'\
                                    'Eg: stock.txt')
        elif cmds == 'Save Sales to File':
            window['-INFO-'].update('Please enter the Sales file to save to.\n'\
                                    'Eg: sales.txt')
        #Setting, Getting and Removing#####################################################
        elif cmds == 'Set Raw Material':
            window['-INFO-'].update('Enter Raw Material Items one at a time.\n'\
                                    'E.g: metal_pipe 100 5.\n'\
                                    '     The name of the item must have no spaces,\n'\
                                    '     Then enter the price and quantity.')
        elif cmds == 'Set Stock':
            window['-INFO-'].update('Enter Stock Items one at a time.\n'\
                                    'E.g: Braai_Stand 800 5.\n' \
                                    '     The name of the item must have no spaces,\n'\
                                    '     Then enter the "price and quantity".')
        elif cmds == 'Get Raw Material':
            window['-OUTPUT-'].update((RMAT.neat_inventory()))
        elif cmds == 'Get Stock':
            window['-OUTPUT-'].update((STCK.neat_inventory()))
        elif cmds == 'Get Stock Value':
            window['-OUTPUT-'].update(STCK.get_value_neat())
        elif cmds == 'Get RawM Value':
            window['-OUTPUT-'].update(RMAT.get_value_neat())
        elif cmds == 'Remove Raw Material':
            window['-INFO-'].update('Which Raw Material item would you like to remove?\n' \
                                    'E.g: Item price & quantity')
            window['-OUTPUT-'].update((RMAT.neat_inventory()))
        elif cmds == 'Remove Stock':
            window['-INFO-'].update('Which Stock item would you like to remove?\n' \
                                       'E.g: Item price & quantity')
            window['-OUTPUT-'].update((STCK.neat_inventory()))
        elif cmds == 'Sell Item/Service':
            window['-INFO-'].update('What have you sold? If it is a service, the name must start with an astericks *.\n' \
                                    'E.g: */Item price & quantity')
            window['-OUTPUT-'].update(STCK.neat_inventory())
        elif cmds == 'Get Sales':
            window['-OUTPUT-'].update(SLS.neat_sales())
        elif cmds == 'Get Sales Value':
            window['-OUTPUT-'].update(SLS.get_value_neat())
        elif cmds == 'Remove Sale Item/Service':
            window['-INFO-'].update('Which Sales item would you like to remove?\n' \
                                    'E.g: Item price & quantity')
            window['-OUTPUT-'].update(SLS.neat_sales())
        elif cmds == 'Get Sales Filename':
            window['-OUTPUT-'].update(SLS.get_filename())
            window['-INFO-'].update('Enter the new file name below with the file extension.\n'\
                                    'Eg: new_sales.txt')
        elif cmds == 'Get Stock Filename':
            window['-OUTPUT-'].update(STCK.get_filename())
            window['-INFO-'].update('Enter the new file name below with the file extension.\n'\
                                    'Eg: new_stock.txt')
        elif cmds == 'Get RawM Filename':
            window['-OUTPUT-'].update(RMAT.get_filename())
            window['-INFO-'].update('Enter the new file name below with the file extension.\n'\
                                    'Eg: new_raw.txt')
        #Submiting Commands###################################################   
        if event == 'Submit!':
            cmds = values['-COMMANDS-']
            tats_input = values['-INPUT-']
            # if cmds == 'Load Data' and len(tats_input) > 0:
            #     try:
            #         RMAT.load_inventory()
            #         STCK.load_inventory()
            #         SLS.load_sales()
            #         window['-INFO-'].update('Data Loaded')
            #     except:
            #         window['-INFO-'].update('ERROR: Could not load data!')
            #Loading and Saving individuals Files#############################
            if cmds == 'Load RawM File' and len(tats_input) > 0:
                fname = tats_input
                try:
                    RMAT.load_inventory(fname)
                    window['-OUTPUT-'].update(RMAT.neat_inventory())
                except:
                    window['-INFO-'].update('ERROR:No such file!')
            elif cmds == 'Load Stock File' and len(tats_input) > 0:
                fname = tats_input
                try:
                    STCK.load_inventory(fname)
                    window['-OUTPUT-'].update(STCK.neat_inventory())
                except:
                    window['-INFO-'].update('ERROR:No such file!')
            elif cmds == 'Load Sales File' and len(tats_input) > 0:
                fname = tats_input
                try:
                    SLS.load_sales(fname)
                    window['-OUTPUT-'].update(SLS.neat_sales())
                except:
                    window['-INFO-'].update('ERROR:No such file!')
            elif cmds == 'Save RawM to File' and len(tats_input) > 0:
                fname = tats_input
                RMAT.save_inventory(fname)
                window['-INFO-'].update(f'File saved as {fname}')
            elif cmds == 'Save Stock to File' and len(tats_input) > 0:
                fname = tats_input
                STCK.save_inventory(fname)
                window['-INFO-'].update(f'File saved as {fname}')
            elif cmds == 'Save Sales to File' and len(tats_input) > 0:
                fname = tats_input
                SLS.save_sales(fname)
                window['-INFO-'].update(f'File saved as {fname}')
            #Setting & Removing###############################################
            elif cmds == 'Set Raw Material' and len(tats_input) > 0:
                name, price, quant = split_input(tats_input)
                RMAT.set_inventory(name, [price,quant])
                window['-OUTPUT-'].update((RMAT.neat_inventory()))
                window['-INFO-'].update(f'{name}, Raw Material has been set.')
            elif cmds == 'Set Stock' and len(tats_input) > 0:
                name, price, quant = split_input(tats_input)
                STCK.set_inventory(name, [price,quant])
                window['-OUTPUT-'].update((STCK.neat_inventory()))
                window['-INFO-'].update(f'{name}, Stock has been set.')
            elif cmds == 'Sell Item/Service' and len(tats_input) > 0:
                name, price, quant = split_input(tats_input)
                SLS.make_sale(STCK, name, [price,quant])
                window['-OUTPUT-'].update(SLS.neat_sales())
                window['-INFO-'].update(f'{name}, Sell Recorded.')
            elif cmds == 'Remove Raw Material' and len(tats_input) > 0:
                name, price, quant = split_input(tats_input)
                RMAT.rm_inventory(name, [price,quant])
                window['-OUTPUT-'].update((RMAT.neat_inventory()))
                window['-INFO-'].update(f'{name}, Has been removed')
            elif cmds == 'Remove Stock' and len(tats_input) > 0:
                name, price, quant = split_input(tats_input)
                STCK.rm_inventory(name, [price,quant])
                window['-OUTPUT-'].update((STCK.neat_inventory()))
                window['-INFO-'].update(f'{name}, Has been removed.')
            elif cmds == 'Remove Sales Item/Service' and len(tats_input) > 0:
                name, price, quant = split_input(tats_input)
                SLS.rm_sales(name, [price,quant])
                window['-OUTPUT-'].update(SLS.neat_sales())
                window['-INFO-'].update(f'{name}, Has been removed.')
            else:
                window['-INFO-'].update('ERROR: Invalid Input!')
            
    window.close()
