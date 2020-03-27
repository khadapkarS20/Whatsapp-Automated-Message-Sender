from selenium import webdriver
import sys

person = input("Enter the name of the person: ")
msg = input("Enter the message: ")
count = int(input("Enter the count of msg: "))

chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome('C:/Users/SHREYAS/Downloads/chromedriver_win32/chromedriver.exe',options=chrome_options)
base_url = 'https://web.whatsapp.com/'
browser.get(base_url)

input('Enter anything but scan first')

try:
    chathead=browser.find_element_by_xpath("//span[@title='{}']".format(person))
    # print(chathead)
    chathead.click()
    # //*[@id="main"]/footer/div[1]/div[2]/div/div[2]
    msgbox = browser.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
except:
    print('Something went wrong till the chathead path')
    sys.exit()

try:
    for i in range(count):
        msgbox.send_keys(msg)
        sendbtn = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
        sendbtn.click()
except:
    print(' Error While sending the message or hitting the enter button')
    sys.exit()