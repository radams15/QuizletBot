#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys
import Helper

stop_time = 500
min_stop_time = 500
repeat = 30
sleep_time = 0.3
headless = False


if len(sys.argv) > 1:
	repeat = int(sys.argv[1])

if stop_time < min_stop_time:
	stop_time = min_stop_time

def get_div_by_text(text):
	return driver.find_elements_by_xpath("//*[contains(text(), \"{text}\")]".format(text=text))[0]

questions, game_id = Helper.parse_questions()
r_questions = Helper.reverse(questions)

profile = webdriver.FirefoxProfile("/home/rhys/.mozilla/firefox/mwzwjulk.default")

options = webdriver.FirefoxOptions()
options.profile = profile
options.headless = headless

driver = webdriver.Firefox(options=options)


driver.get("https://quizlet.com/{id}/write".format(id=game_id))
time.sleep(sleep_time)

entry = None

while True:
    try:
        try:
            entry = driver.find_element_by_class_name("UITextarea-textarea")
        except:
            continue
        try:
            q = driver.find_element_by_class_name("qDef").text
            a = questions[q]
        except KeyError:
            a = r_questions[q]
        entry.send_keys(a)
        entry.send_keys(Keys.ENTER)



        time.sleep(sleep_time)
        driver.find_element_by_class_name("LearnModeMain-anyKey").send_keys(Keys.ENTER)
    except Exception as e:
        print(e)



driver.close()
