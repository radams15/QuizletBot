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

def match(question, card):
	if question in questions.keys():
		try:
			cards[questions[question]].click()
			card.click()
		except:
			return False

profile = webdriver.FirefoxProfile("/home/rhys/.mozilla/firefox/mwzwjulk.default")

options = webdriver.FirefoxOptions()
options.profile = profile
options.headless = headless

driver = webdriver.Firefox(options=options)

for i in range(repeat):
	driver.get("https://quizlet.com/{id}/match".format(id=game_id))
	time.sleep(sleep_time)

	driver.find_element_by_class_name("UIModal").send_keys(Keys.RETURN)
	driver.execute_script("setTimeout(function(){for(var F = setTimeout(';'), i = 0; i < F; i++) clearTimeout(i)}, "+str(stop_time)+");")

	time.sleep(0.1)

	cards = {}
	for card in driver.find_elements_by_class_name("MatchModeQuestionGridBoard-tile"):
		text = card.find_elements_by_css_selector("*")[-1].text
		#match(text, card)
		cards[text] = card

	for question, card in cards.items():
		o = match(question, card)

driver.close()
