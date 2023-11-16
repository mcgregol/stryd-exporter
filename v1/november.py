from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime, os, time

def export(email, passwd, save_path, days_list):
	#  prep selenium
	options = webdriver.FirefoxOptions()
	options.set_preference("browser.download.folderList", 2)
	options.set_preference("browser.download.dir", save_path)
	options.set_preference("browser.download.manager.showWhenStarting", False)
	options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
	
	for day in days_list:
		browser = webdriver.Firefox(options=options)

		#  login
		browser.get('https://www.stryd.com/us/en/signin')
		browser.find_element(By.XPATH, '/html/body/div[1]/main/section/div/form/div/div[1]/div/input').send_keys(email)
		browser.find_element(By.XPATH, '/html/body/div[1]/main/section/div/form/div/div[2]/div/div/input').send_keys(passwd)
		browser.find_element(By.XPATH, '/html/body/div[1]/main/section/div/form/button').click()

		#  goto workouts
		ensure_load_calendar = WebDriverWait(browser, 60).until(
			EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/main/div/div/section/section/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/div')))
		try:
			browser.find_element(By.XPATH, '/html/body/div[1]/div/nav/div[2]/div[1]/div/div[2]/a').click()
		except:
			browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/button').click()
			browser.find_element(By.XPATH, '//*[@id="calendar-link"]').click()

		#  locate desired date
		ensure_load_workout = WebDriverWait(browser, 60).until(
			EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-date="' + day + '"]')))

		#  open workout options as list
		ensure_load_workout.find_element(By.CLASS_NAME, 'css-1pwidyo').click()
		workout_options = browser.find_elements(By.CSS_SELECTOR, '.MuiMenu-list > li')

		#  download workout .fit
		workout_options[1].click()

		time.sleep(8)
		browser.quit()

name = input("Enter player name: ")
init_email = input("Enter player email: ")
init_passwd = input("Enter player password: ")
first_name, last_name = name.split()
init_save_path = os.getcwd() + "/" + first_name + "_" + last_name

#  get list of days to grab from
init_days_list = []
while True:
    user_input = input("Enter a day in november (or type 'done' to finish): ")

    if user_input.lower() == 'done':
        break

    try:
        user_integer = int(user_input)
        init_days_list.append(user_integer)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

#  run program
export(init_email, init_passwd, init_save_path, init_days_list)
print("Done!\nFiles saved in " + init_save_path)