import keyboard
import time
import os

def clear():
    command = 'cls'
    os.system(command)

clear()
starter = input('Press enter: ')
if starter == '':
    while True:
        clear()
        print(' ----------------------------------------------------------------------')
        print('|                     Python FH5 Sniping Script                        |')
        print('|                                                                      |')
        print('|   1- First select the car you want and the potential max buyout      |')
        print('|   2- Make sure to focus the FH5 window when the countdown starts     |')
        print('|   3- Second monitor highly recommended because when you want to      |')
        print('|      close the script you have to just force close the window        |')
        print('|      (Put the game in windowed mode and put the script over it       |')
        print('|       if you don\'t have a second monitor)                            |')
        print('|   4- It will start counting down from 5 once you start the script.   |')
        print('|                                                                      |')
        print('|      GOOD LUCK SNIPING!                                              |')
        print(' ----------------------------------------------------------------------')
        a = str(input('\nDo you want to start the script? y/n: '))
        if a == 'n':
            break
        elif a == 'y':
            clear()    
            for i in range(5, -1, -1):        
                print('!!FOCUS WINDOW!!\nSniping in: ')        
                print(str(i) + ' seconds')                
                time.sleep(1)
                clear()        
            print('Sniping...')
            while True:         
                time.sleep(1)     
                keyboard.press_and_release('Enter')
                time.sleep(0.25)
                keyboard.press_and_release('Enter')
                time.sleep(0.7)
                keyboard.press_and_release('y')
                time.sleep(0.25)      
                keyboard.press_and_release('down')
                time.sleep(0.15)
                keyboard.press_and_release('Enter')
                time.sleep(0.35)    
                keyboard.press_and_release('Enter')
                time.sleep(0.15)   
                keyboard.press_and_release('Escape')                                
        else:            
            while True:
                clear()
                restart = input('You didn\'t press \'y\' to start the script, do you want to restart? y/n : ')
                if restart == 'y':
                    break            
                else:
                    exit()
else:
    exit()
clear()    
