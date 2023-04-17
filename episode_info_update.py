from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, json, re

driver = webdriver.Chrome()

def get_info(fp):
    with open(fp, "r") as inf:
        data =  json.load(inf)
        return data


def login():
    driver.get("https://thetvdb.com/auth/login")

    name_field = driver.find_element(By.ID,"email")
    name_field.send_keys("jayduttjoshiunofficial@gmail.com")

    email_field = driver.find_element(By.ID,"password")
    email_field.send_keys("Imgreat@1234")

    email_field.send_keys(Keys.RETURN)


def add_episodes(ep_info, epfi): 
    try:
        driver.get("https://thetvdb.com/series/shrimaan-shrimati/seasons/official/1/bulkadd")    
        driver.get("https://www.themoviedb.org/tv/19120-shrimaan-shrimati/season/1/edit?active_nav_item=episodes&language=en-US")    
        # driver.get("file://C:/dev/WebDriver/Bulk Add Episodes - TheTVDB.com.html")    
        
        # Find the form fields and fill them in
        submit_button = driver.find_element(By.XPATH,"//button[contains(text(), 'Add Another')]")
        val = min(len(ep_info),20)
        for i in range(0,val):
            submit_button.click()
        
        number_fields = driver.find_elements(By.NAME,"number[]")
        name_fields = driver.find_elements(By.NAME,"name[]")
        overview_fields = driver.find_elements(By.NAME,"overview[]")
        
        keys = list(filter(lambda x: not x['added'], ep_info))
        
        for i in range(0,val):
            number_fields[i].clear()
            number_fields[i].send_keys(keys[i]["number"])
            name_fields[i].clear()
            name_fields[i].send_keys(keys[i]["name"])
            overview_fields[i].clear()
            overview_fields[i].send_keys(keys[i]["desc"])
            
            [x.update({'added': True}) for x in ep_info if x["number"] == keys[i]["number"]]
            
            time.sleep(2)
        
        # Submit the form
        #  submit_button = driver.find_element_by_id("submit-button")
        
        # Assert that the form was submitted successfully
        # assert "Thank you" in driver.page_source
        
        # Close the driver
        # driver.quit()
        
        time.sleep(60)
        
        with open(epfi, "w") as fu:
            fu.write(json.dumps(ep_info, indent=3))

        
    except Exception as e:
        print(e)
    finally:
        time.sleep(20)

epfi = "SS_epinfo.json"

login()
add_episodes(get_info(epfi), epfi)

# add_episodes(get_info("SS_epinfo________.json"))