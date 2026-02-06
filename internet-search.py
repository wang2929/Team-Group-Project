import os

def internet_search():
    while True:
        print('\nYou are in the web browser function.')
        browser_input = input('Select the following options:\n 1. Open brower\n or 2. Return to main menu.\n>> ')
    
        if browser_input == '1':
            print('Opening Google browser...')
            url = "https://www.google.com"
            os.system(f"explorer.exe {url}")
    
        elif browser_input == '2':
            return #main_menu here
    
        else:
            print('You have selected an unavaiable option. Please try again.')

internet_search()