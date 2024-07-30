import time

import pandas as pd
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# hospital_info_dict = {}
hospitals_list = []
# driver = Chrome()
URL = "https://hospitalpricingfiles.org/"

def get_data(url):
	browser_options = ChromeOptions()
	browser_options.headless = True # keeps browser hidden when we run it
 
	driver = Chrome(options=browser_options)
	driver.get(url)
	
  # Wait until the iframe is present and switch to it
	wait = WebDriverWait(driver, 10)
 
	# Locate and click on the state with class name 'AK state'
	us_state_map = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'us-state-map')))

	# Find the outlines element within the us-state-map
	outlines = us_state_map.find_element(By.CLASS_NAME, 'outlines')

	# Find all child elements within outlines and get their class names
	states = outlines.find_elements(By.XPATH, './*')
	state_classes = [state.get_attribute('class') for state in states]
	# for state_class in state_classes:
	# 		print(state_class)
  
  # Find all child elements within outlines
	states = outlines.find_elements(By.XPATH, './*')
	# print(states)
	state_texts = {}

	for state in states:
			state_class = state.get_attribute('class')
			if state_class == 'UT state':
					print(state)
					utah_state = state
        
  # state_class = state_class.get_attribute('class')
  
  # Click on the state element
	utah_state.click()
 
 	# Wait for 10 seconds
	time.sleep(3)
  
	# Wait until the new page content is loaded
	wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

	# Locate the parent element with the specified class
	parent_elements = driver.find_elements(By.CLASS_NAME, 'search-result-item-wrapper.mobile-search-result-card-style')
	
	for parent in parent_elements:
			# Create a new dictionary for each hospital
			hospital_info_dict = {}
			# Find all child elements within the parent element with the specified class
			hospital_elements = parent.find_elements(By.CLASS_NAME, 'name-hospital-search-result-wrapper')
			hospital_address_elements = parent.find_elements(By.CLASS_NAME, 'address-hospital-search-result-wrap')
			hospital_other_elements = parent.find_elements(By.CLASS_NAME, 'phone-website-ccn-search-result-wrap') #'ccn-number-search-result')

			print('=========================================')
     	# Extract text and store in the dictionary
			hospital_info_dict['name'] = hospital_elements[0].text
			hospital_info_dict['address'] = hospital_address_elements[0].text
			for other_element in hospital_other_elements:
					hospital_ccn_elements = other_element.find_elements(By.CLASS_NAME, 'ccn-number')
					hospital_phone_elements = other_element.find_elements(By.CLASS_NAME, 'phone-number')
					hospital_website_elements = other_element.find_elements(By.CLASS_NAME, 'website-search-result')
					if hospital_ccn_elements:
						hospital_info_dict['ccn'] = hospital_ccn_elements[0].text
					else:
						hospital_info_dict['ccn'] = ''
					hospital_info_dict['phone_no'] = hospital_phone_elements[0].text
					hospital_info_dict['website'] = hospital_website_elements[0].get_attribute('href')
     
			print(f"Hospital Name: {hospital_info_dict['name']}")
			print(f"Hospital Address: {hospital_info_dict['address']}")
			print(f"Hospital CCN: {hospital_info_dict['ccn']}")
			print(f"Hospital Phone Number: {hospital_info_dict['phone_no']}")
			print(f"Hospital Website: {hospital_info_dict['website']}")
			hospitals_list.append(hospital_info_dict)
			# print(hospitals_list)
	print(hospitals_list)
	driver.quit()
	return hospitals_list


def main():
    data = get_data(URL)
    df = pd.DataFrame(data=data).drop_duplicates()
    print(df.head())
    
    
if __name__ == '__main__':
    main()