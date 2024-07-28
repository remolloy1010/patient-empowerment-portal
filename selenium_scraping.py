import time

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = Chrome()
URL = "https://hospitalpricingfiles.org/"

def get_data(url):
	browser_options = ChromeOptions()
	browser_options.headless = True # keeps browser hidden when we run it
 
	driver = Chrome(options=browser_options)
	driver.get(url)
	# element = driver.find_element(By.LINK_TEXT, "here")

	# print(element.text)
	# elements = driver.find_elements(By.CLASS_NAME, "us-state-map")
	
	# # Collect and print link texts and hrefs
	# links = []
	# for element in elements:
	# 		link_text = element.text
	# 		link_href = element.get_attribute("href")
	# 		links.append((link_text, link_href))
	# 		print(f"Text: {link_text}, URL: {link_href}")
   
  # Wait until the iframe is present and switch to it
	wait = WebDriverWait(driver, 10)
 
	# Locate a specific div by its class name
	# map_div = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "us-state-map")))

	# # Interact with elements inside the div
	# elements = map_div.find_elements(By.TAG_NAME, "title")

	# # Collect and print link texts and hrefs
	# links = []
	# for element in elements:
	# 		link_text = element.text
	# 		link_href = element.get_attribute("href")
	# 		links.append((link_text, link_href))
	# 		print(f"Text: {link_text}, URL: {link_href}")
 
	# # Locate and click on the state with class name 'AK state'
	# state_element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'AK state')))
	us_state_map = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'us-state-map')))

	# Find the outlines element within the us-state-map
	outlines = us_state_map.find_element(By.CLASS_NAME, 'outlines')

	# Find all child elements within outlines and get their class names
	states = outlines.find_elements(By.XPATH, './*')
	state_classes = [state.get_attribute('class') for state in states]

	for state_class in state_classes:
			print(state_class)
  
  # Find all child elements within outlines
	states = outlines.find_elements(By.XPATH, './*')

	state_texts = {}

	for state in states:
			state_class = state.get_attribute('class')
			print(state_class)
        
  # state_class = state_class.get_attribute('class')
  
  # Click on the state element
	state.click()
 
 	# Wait for 10 seconds
	time.sleep(3)
  
	wait = WebDriverWait(driver, 10)
	# Wait until the new page content is loaded
	wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

	# Extract all text from the resulting page
	body_text = driver.find_element(By.TAG_NAME, 'body').text
	state_texts[state_class] = body_text
	print(f"Text for {state_class}: {body_text}")
 
	driver.quit()


def main():
    data = get_data(URL)
    
    
if __name__ == '__main__':
    main()