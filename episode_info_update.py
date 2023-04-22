import json
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
TMDB = "https://www.themoviedb.org/"


def get_info(fp):
    with open(fp, "r") as inf:
        data = json.load(inf)
        return data


def login():
    driver.get(f"{TMDB}login")

    name_field = driver.find_element(By.ID, "username")
    name_field.send_keys("thesharingbrother")

    email_field = driver.find_element(By.ID, "password")
    email_field.send_keys("Imgreat@1234")
    time.sleep(2)
    email_field.send_keys(Keys.RETURN)
    time.sleep(2)




def add_episodes(ep_info):
    try:
        # driver.get("https://thetvdb.com/series/shrimaan-shrimati/seasons/official/1/bulkadd")
        # driver.get(f"{TMDB}tv/19120-shrimaan-shrimati/season/1/edit?active_nav_item=episodes&language=en-US")
        driver.get(f"{TMDB}tv/58791-lucky/season/1/edit?active_nav_item=episodes&language=en-US")
        # driver.get("file://C:/dev/WebDriver/Misc/Edit Shrimaan Shrimati — The Movie Database (TMDB).html")
        wait = WebDriverWait(driver, 10)
        # for i in range(1, 3):
        for i in range(3, len(ep_info)):
            epi = ep_info[i]
            # Find the form fields and fill them in
            add_ep_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Add New Episode')]")))
            add_ep_button.click()

            # val = min(len(ep_info), 20)
            # for i in range(0, val):
            # div_to_delete = driver.find_element(By.CLASS_NAME, "k-overlay")

            # Execute a JavaScript code to remove the div element
            # driver.execute_script("arguments[0].remove()", div_to_delete)

            popup = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "k-popup-edit-form")))

            """noo = WebDriverWait(popup, 20).until(
                EC.presence_of_element_located((By.XPATH, "//input[@data-bind='value:episode_number']")))
            # print("name field found")
            # noo.clear()
            noo.send_keys(epi['number'])"""

            name = WebDriverWait(popup, 20).until(
                EC.presence_of_element_located((By.XPATH, "//input[@data-bind='value:name']")))
            # print("name field found")
            name.send_keys(epi['name'])
            # keys = ep_info

            ov = WebDriverWait(popup, 20).until(
                EC.presence_of_element_located((By.ID, "en-US_overview_text_box_field")))
            #  (By.XPATH, "//textarea[@data-bind='value:overview']")))
            # print("name field found")
            ov.send_keys(epi['desc'])

            rt = WebDriverWait(popup, 20).until(
                EC.presence_of_element_located((By.XPATH, "//input[@data-bind='value:runtime']")))
            # print("name field found")
            rt.send_keys(epi['runtime'])

            time.sleep(3)
            submit_button = WebDriverWait(popup, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "k-grid-update")))

            #  submit_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Save')]")
            submit_button.click()
            time.sleep(5)
        # Submit the form
        #  submit_button = driver.find_element_by_id("submit-button")

        # Assert that the form was submitted successfully
        # assert "Thank you" in driver.page_source

        # Close the driver
        driver.quit()

        """with open(epfi, "w") as fu:
            fu.write(json.dumps(ep_info, indent=3))"""

    except Exception as e:
        print(e)
    finally:
        time.sleep(20)


epfi = "SS_epinfo.json"
epfi = "linfo.json"

login()
add_episodes(get_info(epfi))

# add_episodes(get_info("SS_epinfo________.json"))
