from selenium import webdriver

person = input("Enter the name of the person: ")
msg = input("Enter the message: ")
count = int(input("Enter the count of msg: "))

chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome('C:/Users/SHREYAS/Downloads/chromedriver_win32/chromedriver.exe',options=chrome_options)
base_url = 'https://web.whatsapp.com/'
browser.get(base_url)

input('Enter anything but scan first')

chathead=browser.find_element_by_xpath("//span[@title='{}']".format(person))
# print(chathead)
chathead.click()

msgbox = browser.find_element_by_class_name('_3u328')


for i in range(count):
    msgbox.send_keys(msg + str(i))
    sendbtn = browser.find_element_by_class_name('_3M-N-')
    sendbtn.click()