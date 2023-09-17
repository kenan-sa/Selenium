import re
import rstr
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random



parser = argparse.ArgumentParser(
                    prog = 'Purchase Order form - What would you like to purchase?',
                    description = 'this program playing with -Purchase Order form- using selenium',
                    epilog = 'Created by ... danialStudent-Kakaroto')# We're marching as the army of the unbreakable.

parser.add_argument('-m', '--mode' , required = True)

###################################################
parser.add_argument('-t', '--thing' , choices=['cap', 'shoes', 'hoodie'],action='append', help = "enter the thing that you want to purchase !")# Append : This will allow the argument to collect multiple values as a list.
parser.add_argument('-e', '--email' )    
parser.add_argument('-f', '--first_name' ,  help = "enter your first name ")
parser.add_argument('-l', '--last_name' ,  help = "enter your last name ")
parser.add_argument('-s', '--street' , help = "enter your street line 1 ")
parser.add_argument('-st', '--streetLtow' ,help = "enter your street line 2 ")
parser.add_argument('-c', '--city' , help = "enter your city name ")
parser.add_argument('-a', '--state' , help = "enter your state ")
parser.add_argument('-p', '--postal' ,  help = "enter your postal card ")


args = parser.parse_args()
if args.mode =='m' and (args.email is None or args.postal is None):
    print("You chose manual,mail and postal card requird")
    exit()


mail_regex='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
postal_regex='^\d{5}(?:[-\s]\d{4})?$'


chrome_options = webdriver.ChromeOptions()#options objectfills a form
chrome_options.add_argument("--start-maximized")
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-infobars")


mail_str=''
pos_str=''
if args.mode=="m":#if manual
    mail_str=args.email
    pos_str=args.postal
    regex=re.compile(mail_regex)
    if(re.search(regex,mail_str) is None): #search takes Pattern and astring to check (Pattern.str)
        print("the mail you input is incorrect")
        exit()

    regex=re.compile(postal_regex)
    
    if re.search(regex,pos_str)is None :
        print("the postal card  you input is incorrect")
        exit()
else:#if auto
    mail_str=rstr.xeger(mail_regex)
    pas_str=rstr.xeger(postal_regex)






web=webdriver.Chrome(options=chrome_options)
web.get('https://www.jotform.com/build/232074130837451')

sleep(2)#to make sure the page is loaded

cap=web.find_element(By.XPATH,'//*[@id="input_3_1004"]')
shoes=web.find_element(By.XPATH,'//*[@id="input_3_1005"]')
hoodie=web.find_element(By.XPATH,'//*[@id="input_3_1006"]')
first_name=web.find_element(By.XPATH,'//*[@id="first_4"]')
last_name=web.find_element(By.XPATH,'//*[@id="last_4"]')
email=web.find_element(By.XPATH,'//*[@id="input_5"]')
street=web.find_element(By.XPATH,'//*[@id="input_6_addr_line1"]')
streetLtow=web.find_element(By.XPATH,'//*[@id="input_6_addr_line2"]')
city=web.find_element(By.XPATH,'//*[@id="input_6_city"]')
state=web.find_element(By.XPATH,'//*[@id="input_6_state"]')
postal=web.find_element(By.XPATH,'//*[@id="input_6_postal"]')
submit=web.find_element(By.XPATH,'//*[@id="input_2"]')

total=web.find_element(By.XPATH,'//*[@id="payment_total"]')

if args.mode == 'm':
    ls=args.thing
    if 'cap'in ls :
        cap.click()
    if 'shoes' in ls:
        shoes.click()
    if 'hoodie' in ls:
        hoodie.click()

    first_name.send_keys(args.first_name)
    last_name.send_keys(args.last_name)
    email.send_keys(mail_str)
    street.send_keys(args.street)
    if args.streetLtow is not None:
        streetLtow.send_keys(args.streetLtow)
    city.send_keys(args.city)
    if args.state is not None:
        state.send_keys(args.state)
    postal.send_keys(pos_str)

    sleep(1)
    print("Total    $"+total.text)#print the total at the end ☺☻♥
    sleep(1)
    web.execute_script("window.scrollTo(0, document.body.scrollHeight);")#sometimes it return error because he didn't 
    submit.click()#                                             find the submit button because he is at the end of the page !☻☻
    sleep(3)
    exit()
else:
    def generate_random_condition():
        conditions = ['cap', 'shoes', 'hoodie']
        return random.choice(conditions)

    first_name_regex = '^[A-Za-z\'-]{1,10}$'
    last_name_regex = '^[A-Za-z\'-]{1,10}$'
    street_regex = '^[A-Za-z0-9\s\'-]{1,10}$'
    street_tow_regex = '^[A-Za-z0-9\s\'-]{1,10}$'
    postal_rand=random.randint(1000,9999)

    def generate_random_cityName():#func that return a random city from the list 
        cities=['New York ','London','Tokyo','Paris','Sydney','Beijing','Dubai','Rio de Janeiro','Moscow','Mumbai']
        return random.choice(cities)
    
    def generate_random_stateName(city):#func that receive a city and return a state of that city
        cities=['New York ','London','Tokyo','Paris','Sydney','Beijing','Dubai','Rio de Janeiro','Moscow','Mumbai']
        if city in cities :
            x=cities.index(city)
            states=['New York ','Greater London','Tokyo','Île-de-France','New South Wales','Beijing','Dubai','Rio de Janeiro','Moscow','Maharashtra']
            return states[x]
        else:
            return "None"
    
    ls=generate_random_condition()
    if 'cap'in ls :
        cap.click()
    if 'shoes' in ls:
        shoes.click()
    if 'hoodie' in ls:
        hoodie.click()

    first_name.send_keys(rstr.xeger(first_name_regex))
    last_name.send_keys(rstr.xeger(last_name_regex))
    email.send_keys(mail_str)
    street.send_keys(rstr.xeger(street_regex))
    streetLtow.send_keys(rstr.xeger(street_tow_regex))
    x=generate_random_cityName()
    city.send_keys(x)
    state.send_keys(generate_random_stateName(x))
    postal.send_keys(postal_rand)
    print("Total    $"+total.text)#print the total at the end ☺☻♥
    sleep(1)
    web.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    submit.click()
    sleep(2)
    exit()