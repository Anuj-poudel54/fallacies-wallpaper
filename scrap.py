from selenium import webdriver
import selenium.common
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import selenium

import os
# To get all the logical fallacies

URL = "https://www.yourlogicalfallacyis.com/strawman"

chrome = webdriver.Chrome()

chrome.get(URL)

wait = WebDriverWait(chrome, 10)
all_fallacies = []

try:
    os.mkdir("data")
except FileExistsError:
    ...
except Exception as e:
    print("Error while creating file")
    print(e)
    exit(1)

fallacies_file = open("data/fallacies.txt", "a+")
while True:
    try:
        # Wait til web page loads
        fallacy_title = wait.until(EC.visibility_of(chrome.find_element(
            By.CSS_SELECTOR, "article.fallacy-detailed h1")))

        if fallacy_title.text in all_fallacies:
            break

        all_fallacies.append(fallacy_title.text)

    except selenium.common.TimeoutException:
        print("Timout occured while trying to get title\nTrying again...")
        continue

    except Exception as e:
        print("ERROR :", e)
        fallacies_file.close()

    short_description = chrome.find_element(
        By.CSS_SELECTOR, "article.fallacy-detailed h1")
    p_contents = chrome.find_elements(
        By.CSS_SELECTOR, "article.fallacy-detailed .body > p")

    # Writing in file
    fallacies_file.write(f"TITLE: {fallacy_title.text}")
    fallacies_file.write(f"DESC: {short_description.text}")
    fallacies_file.write(f"EXT DESC: {p_contents[0].text}")
    fallacies_file.write(f"EXAMPLE: {p_contents[1].text}")

    # Clicking next button
    next_button = chrome.find_element(By.CSS_SELECTOR, "span.next")
    next_button.click()

fallacies_file.close()
