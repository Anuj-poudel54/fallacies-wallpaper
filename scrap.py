# script to scrap all the logical fallacies from https://www.yourlogicalfallacyis.com/

from selenium import webdriver
import selenium.common
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import selenium

import os

from data_type import Fallacy

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

fallacies_file = open("data/fallacies.txt", "w")

print("[INFO] Getting all fallacies...")
max_trying_attempt = 3
while max_trying_attempt > 0:
    try:
        # Wait til web page loads
        fallacy_title = wait.until(EC.visibility_of(chrome.find_element(
            By.CSS_SELECTOR, "article.fallacy-detailed h1")))

        if fallacy_title.text in all_fallacies:
            break

        all_fallacies.append(fallacy_title.text)

    except selenium.common.TimeoutException:
        print("Timout occured while trying to get title\nTrying again...")
        max_trying_attempt -= 1
        continue

    except Exception as e:
        print("ERROR :", e)
        fallacies_file.close()

    short_description = chrome.find_element(
        By.CSS_SELECTOR, "article.fallacy-detailed h2")
    p_contents = chrome.find_elements(
        By.CSS_SELECTOR, "article.fallacy-detailed .body > p")

    print(f"[INFO] Got '{fallacy_title.text} fallacy'")

    # Writing in file

    fallacy = {
        "title": fallacy_title.text.replace("\n", " ").strip("\n"),
        "desc": short_description.text.replace("\n", " ").strip("\n"),
        "ext_desc": p_contents[0].text.replace("\n", " ").strip("\n"),
        "example": p_contents[1].text.replace("\n", " ").strip("\n"),
    }

    fallacy = Fallacy( **fallacy )

    fallacies_file.write( fallacy.model_dump_json() )
    fallacies_file.write("\n")

    # Clicking next button
    next_button = chrome.find_element(By.CSS_SELECTOR, "span.next")
    next_button.click()

    # Again reloading page with next url. Not good way since page should not be reloaded. Need to look into
    chrome.get(chrome.current_url)

fallacies_file.close()

if max_trying_attempt <= 0 or len(all_fallacies) == 0:
    print("Couldnot get fallacies")

else:
    print("Finished fetching.")
    print(f"Got {len(all_fallacies)} fallacies.")
