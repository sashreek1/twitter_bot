from selenium import webdriver
import time

def tweet_msg(tweet,user_name,password):
    driver = webdriver.Firefox()
    driver.get("https://twitter.com/home")
    element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[1]/input")
    element.send_keys(user_name)
    time.sleep(2)
    element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input")
    element.send_keys(password)
    time.sleep(2)
    element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/div[2]/button")
    element.click()
    time.sleep(3)
    element = driver.find_element_by_xpath("/html/body/div/div/div/div/header/div/div/div/div/div[3]/a")
    element.click()
    element = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div")
    element.send_keys(tweet)
    element = driver.find_element_by_xpath("/html/body/div/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]")
    element.click()
    time.sleep(3)
    driver.close()
    driver.quit()


def fetch_results():
    driver = webdriver.Firefox()
    driver.get("https://fedoramagazine.org/")
    title = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/div[1]/div[2]/h2/a")
    title1 = title.text
    link = title.get_attribute("href")
    driver.close()
    driver.quit()
    return title1,link
user_name = input("please enter your user name/email id/phone number : ")
password = input("please enter your password : ")
title,link = fetch_results()
tweet_text = "latest fedora article: \n"+title+'\n'+link
print(tweet_text)
tweet_msg(tweet_text,user_name,password)