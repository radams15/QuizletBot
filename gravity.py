#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import Helper
import time

stop_time = 500
min_stop_time = 500
repeat = 30
sleep_time = 0.3
pts_wanted = 20000000
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

driver.get("https://quizlet.com/{id}/gravity".format(id=game_id))
time.sleep(sleep_time)

entry = None
is_playing = True
t = time.time()

while True:
	try:
		if is_playing:
			pl = driver.find_elements_by_class_name("GravityModeControls-value")
			level = int(pl[1].text.replace(",", ""))
			points = int(pl[0].text.replace(",", ""))

			if points >= pts_wanted:
				is_playing = False
				continue
			if not entry:
				try:
					entry = driver.find_element_by_class_name("GravityTypingPrompt-input")
				except:
					entry = None
			q = driver.find_element_by_class_name("TermText").text
			a = questions[q]
			print(points, q, a)
			entry.send_keys(a)
			entry.send_keys(Keys.ENTER)
		else:
			a = driver.find_element_by_class_name("GravityCopyTermView-definitionText").find_element_by_class_name("TermText").text
			driver.find_element_by_class_name("GravityCopyTermView-input").send_keys(a)
			time.sleep(0.5)
			is_playing = True
	except:
		pass



driver.close()
