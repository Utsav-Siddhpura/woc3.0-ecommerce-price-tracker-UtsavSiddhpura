# This is just a temporary partially working script for amazon
# The time interval between two checks are 2 hours and thus 2*60*60 = 7200 seconds
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
from email.message import EmailMessage
import time
import datetime
PATH = "C:\\Program Files (x86)\\chromedriver.exe"
linkVar = input("Please enter the product link of amazon here : ")
desired_priceVar = float(input("Enter desired product price here : "))
emailVar = input("Enter Your Email-Id here : ")
while True:
    timeVar = datetime.datetime.now()
    try:
        textFile = open("timeInfo.txt", "x")
        textFile.write(timeVar.strftime("%c"))
        textFile.close()
    except:
        textFile = open("timeInfo.txt","r")
        lastTime = datetime.datetime.strptime(textFile.read(),"%c")
        textFile.close()
        deltatime = (timeVar - lastTime).total_seconds()
        if deltatime < 7200 :
            time.sleep(7200-deltatime)


# Set def_email and def_password according to sender's email id
    def_email = ''
    def_password = ''

# Opening of amazon product link code
    driver = webdriver.Chrome(PATH)
    driver.get(linkVar)
    priceStr = driver.find_element_by_id("priceblock_dealprice").text
    product_name = driver.find_element_by_id("productTitle").text
    n = priceStr.find(' ')
    priceStr = priceStr[n+1:]
    priceVar = float(priceStr)

# Function to send automatic Emails
    def sendEmail(Msg):
        with smtplib.SMTP_SSL('smtp.gmail.com') as smtp:
            smtp.login(def_email, def_password)
            smtp.send_message(Msg)

# Comparing prices
    if priceVar <= desired_priceVar :
        msg = EmailMessage()
        msg['Subject'] = 'Prices Dropped!!'
        msg['From'] = def_email
        msg['To'] = emailVar
        msgstr = str("Hey, Wake up!!\n\n Price of your favourite product \n\""+product_name+"\"\n have now dropped as low as Rs " + str(priceVar) + ", as you wished for.\n\nSo what are you waiting for!! Go and get it.....\n" + linkVar )
        msg.set_content(msgstr)
        sendEmail(msg)
        driver.quit()
        exit()
    driver.quit()
    textFile = open ("timeInfo.txt", "w")
    timeVar = datetime.datetime.now()
    textFile.write(timeVar.strftime("%c"))
    textFile.close()





