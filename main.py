from selenium import webdriver

# driver = webdriver.Chrome(executable_path='./chromedriver/chromedriver')
driver = webdriver.Chrome('./chromedriver/chromedriver_mac64_74')
driver.get('https://web.whatsapp.com/')

# name = input('Enter the name of user or group : ')
name_list = ['Edmund Situmorang', 'Mom']

msg = input('Enter your message : ')
count = int(input('Enter the count : '))

input('Enter anything after scanning QR code')

for name in name_list:
    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_2S1VP')

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_35EW6')
        button.click()