import random
import string
# import requests
import time
import sys

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException, TimeoutException, ElementClickInterceptedException

driver = webdriver.Chrome()

try:
    driver.maximize_window()
    
    driver.get("https://shvasa.com")
    
    # Clear cookies
    print(driver.get_cookies())
    driver.delete_all_cookies()
    driver.delete_all_cookies()

    start_free_trial_button = WebDriverWait(driver, 30).until(
        # EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Start free trial Now')]"))
        EC.element_to_be_clickable((By.XPATH, "//*[@id='start-7-day-trial']/div[2]/div/a"))
    )
    start_free_trial_button.click()

    # signup_window_present = WebDriverWait(driver, 30).until(
    #     # EC.presence_of_element_located((By.XPATH, "//div[@class='orange-btn-clarity full-width w-button']"))
    #     EC.presence_of_element_located((By.XPATH, "//*[@id='start-7-day-trial']/div[2]/div/a"))
    # )
    # print("Signup window popped up successfully!")
    
    # Check if there is an iframe and switch to it
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "iframe"))
    )
    driver.switch_to.frame(iframe)
    
    # Wait for the signup window to appear
    signup_window_present = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']"))
    )
    print("Signup form is present!")


    # Generate random name, phone number, and password
    # random_name = ''.join(random.choice(string.ascii_uppercase) for _ in range(10))
    random_name = 'TestBot'
    # random_phone_number = ''.join(random.choice(string.digits) for _ in range(12))
    random_phone_number = '1234567890'
    # random_password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12))
    random_password = 'Pass1@TestBot'
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    random_email = f"{random_string}@shvasa.com"
    print("Bot Details: ",random_name, random_phone_number, random_password, random_email)

    # # Generate a temporary email address using TempMail API 
    # url = "https://privatix-temp-mail-v1.p.rapidapi.com/request/delete/id/%7Bmail_id%7D/"
    # headers = {
    #     "x-rapidapi-key": "b2f8796914mshe703e50c0806da4p1ff0bejsnd65b96c7ceb4",
    #     "x-rapidapi-host": "privatix-temp-mail-v1.p.rapidapi.com"
    # }
    # response = requests.get(url, headers=headers)
    # print(response.json())

    # Fill in the signup form
    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']/div/div[1]/div/div/input"))
    )
    name_input.click()
    name_input.send_keys(random_name)
    time.sleep(1)
    
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']/div/div[2]/div/div/input"))
    )
    email_input.click()
    email_input.send_keys(random_email)
    time.sleep(1)

    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']/div/div[3]/div/div/input"))
    )
    phone_input.click()
    phone_input.send_keys(random_phone_number)
    time.sleep(1)
    
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']/div/div[4]/div/div/input"))
    )
    password_input.click()
    password_input.send_keys(random_password)
    time.sleep(1)

    signup_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='loginForm']/div/div[5]/button/span[1]"))
    )
    signup_button.click()
    time.sleep(1)
    
    print("Signup form submitted successfully!")
    time.sleep(3)
    
    # gender_button = WebDriverWait(driver, 20).until(
    #     # EC.presence_of_element_located((By.XPATH, "//*[@id='Ellipse_94-2']"))
    #     EC.presence_of_element_located((By.XPATH, '//*[@id="basic_info_gender_male"]/span[1]'))
    # )
    # gender_button.click()
    # time.sleep(1)
    
    
    gender_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="basic_info_gender_male"]/span[1]'))
    )

    # Ensure the gender button is visible before clicking
    driver.execute_script("arguments[0].scrollIntoView(true);", gender_button)
    time.sleep(1)
    
    try:
        gender_button.click()
    except ElementNotInteractableException:
        driver.execute_script("arguments[0].click();", gender_button)
    time.sleep(1)
    
    age_input = WebDriverWait(driver, 20).until(
        # EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div[1]/div/div/div[2]/div/div/div[4]/form/div[2]/div/div/div/div/input"))
        # EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div[1]/div/div/div[2]/div[2]/div[2]/div/form/div/div[2]/div/div/div[2]/input"))
        EC.presence_of_element_located((By.XPATH, '//*[@id="basic_info_age"]'))
    )
    age_input.click()
    age_input.send_keys(36)
    time.sleep(1)
    
    weight_input = WebDriverWait(driver, 20).until(
        # EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div[1]/div/div/div[2]/div/div/div[4]/form/div[4]/div/div[2]/div/input"))
        # EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div[1]/div/div/div[2]/div[2]/div[2]/div/form/div/div[3]/div[2]/div[1]/div/input"))
        EC.presence_of_element_located((By.XPATH, '//*[@id="basic_info_weight"]'))
    )
    weight_input.click()
    weight_input.send_keys(45)
    time.sleep(1)
    
    next_button = WebDriverWait(driver, 10).until(
        # EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div[1]/div/div/div[2]/div/div/div[4]/form/div[5]/button/span[1]/span"))
        # EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div[1]/div/div/div[2]/div[2]/div[2]/div/form/div/div[4]/button/span[1]/span"))
        EC.presence_of_element_located((By.XPATH, '//*[@id="basic_info_gender_age_btn"]'))        
    )
    next_button.click()
    time.sleep(1)
    
    print("Details page 1/3 filled successfully!")
    time.sleep(3)
    
    med_cond_button_1 = WebDriverWait(driver, 10).until(
        # EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/button/span[1]/div/div[1]/div/svg/g/g[1]/circle'))
        # EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[1]/div/button/span[1]/div/img'))
        EC.presence_of_element_located((By.XPATH, '//*[@id="onboarding_medical_cond_none_btn"]/span[1]/div'))
    )
    med_cond_button_1.click()
    time.sleep(1)
    
    med_cond_button_2 = WebDriverWait(driver, 10).until(
        # EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[5]/div/button/span[1]/div/div[1]/div/svg/g/g/g[1]/circle'))
        # EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[2]/div[2]/div/div[2]/div[1]/div/div/div[5]/div/button/span[1]/div/img'))
        EC.presence_of_element_located((By.XPATH, '//*[@id="onboarding_medical_cond_hypertension_btn"]/span[1]/div'))
    )
    med_cond_button_2.click()
    time.sleep(1)

    continue_button = WebDriverWait(driver, 10).until(
        # EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div[1]/div/div/div[2]/div/div/div[4]/button/span[1]/span"))
        # EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div[1]/div/div/div[2]/div[2]/div/div[2]/div[3]/button"))
        EC.presence_of_element_located((By.XPATH, '//*[@id="basic_info_medical_btn"]/span[1]/span'))
    )
    continue_button.click()
    time.sleep(1)
    
    print("Details page 2/3 filled successfully!")
    time.sleep(1)
    
    lifestyle_button = WebDriverWait(driver, 10).until(
        # EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div/button/span[1]/div/img'))
        EC.presence_of_element_located((By.XPATH, '//*[@id="onboarding_time_goals_midday_btn"]/span[1]/div/img'))
    )
    lifestyle_button.click()
    time.sleep(1)
    
    continue_button_2 = WebDriverWait(driver, 10).until(
        # EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div[1]/div/div/div[2]/div[2]/div[2]/div/div[4]/button"))
        EC.presence_of_element_located((By.XPATH, '//*[@id="basic_info_timing_btn"]'))
    )
    continue_button_2.click()
    
    print("Details page 3/3 filled successfully!")
    time.sleep(3)
    
    book_a_class_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[8]/div[3]/div/div[2]/div[4]/button/span[1]'))
    )
    book_a_class_button.click()
    
    # Switch back to the main content
    # driver.switch_to.default_content()
    
    # ----------------
    # Try - 1
    # book_class_button_1 = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Book')]"))
    # )
    # book_class_button_1 = driver.find_elements(By.XPATH, "//button[contains(text(), 'Book')]")
    # book_class_button_1.click()
    
    # book_class_button_2 = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '//*[@id="6668ad3783b508af71e8b643"]/div/div[2]/div/div[2]/div/div[2]/div/button/span[1]'))
    # )
    # book_class_button_2.click()
    
    # book_class_button_3 = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '//*[@id="6668ad3783b508af71e8b577"]/div/div[2]/div/div[2]/div/div[2]/div/button/span[1]'))
    # )
    # book_class_button_3.click()
    # ----------------
    
    # ----------------
    # Try - 2
    # book_class_button = WebDriverWait(driver, 30).until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Book Class')]"))
    # )
    # book_class_button.click()
    # time.sleep(2)
    
    # book_class_button = WebDriverWait(driver, 30).until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Book Class')]"))
    # )
    # book_class_button.click()
    # time.sleep(2)
    
    # book_class_button = WebDriverWait(driver, 30).until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Book Class')]"))
    # )
    # book_class_button.click()
    # time.sleep(2)
    # ----------------
    
    # ----------------
    # Try - 3
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_all_elements_located((By.XPATH, '//*[@id="app"]/div/div[1]/div[3]/div[1]/div/div[4]/div/div/div/div/div'))
    # )
    
    # # Get all class schedule items
    # class_items = driver.find_elements(By.XPATH, '//*[@id="app"]/div/div[1]/div[3]/div[1]/div/div[4]/div/div/div/div/div')
    
    # count = 0
    # for item in class_items:
    #     # Check if the class is locked
    #     if item.find_elements(By.XPATH, ".//span[contains(., 'Locked class')]"):
    #         print("Skipping locked class")
    #         continue
        
    #     # Get the "Book Class" button within the class item
    #     book_button = item.find_element(By.XPATH, ".//button[contains(., 'Book Class')]")
        
    #     # Click the button and increase the count
    #     book_button.click()
    #     count += 1
    #     print("Clicked 'Book Class' button")
        
    #     # Sleep for a short duration to avoid issues with rapid clicking
    #     time.sleep(2)
        
    #     # Stop after clicking the first three available buttons
    #     if count >= 3:
    #         break
    # ----------------
    
    # ----------------
    # Try - 4
    buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//button[contains(., 'Book Class')]"))
    )

    booked_classes = 0
    max_classes_to_book = 3

    while booked_classes < max_classes_to_book:
        for button in buttons:
            try:
                button.click()
                print("Class booked successfully!")
                booked_classes += 1
                time.sleep(5)
                if booked_classes >= max_classes_to_book:
                    break
            except (ElementClickInterceptedException, ElementNotInteractableException, TimeoutException) as e:
                print(f"Skipping non-interactable button due to error: {str(e)}")
                driver.execute_script("window.scrollBy(0, 100);")  # Scroll down a bit to try the next button
                continue

        if booked_classes < max_classes_to_book:
            # Scroll down and find more "Book Class" buttons
            driver.execute_script("window.scrollBy(0, 1000);")
            time.sleep(5)
            buttons = driver.find_elements(By.XPATH, "//button[contains(., 'Book Class')]")
        
    print(f"Booked {booked_classes} classes successfully!")
    time.sleep(5)
    # ----------------
    
    # ----------------
    # Try - 5
    # for button in book_class_buttons:
    #     button.click()
        # time.sleep(2)  # Adjust sleep time as needed
    # ----------------    
    
    go_to_home_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div[3]/div[2]/div/div[2]/button/span[1]/span'))
    )
    go_to_home_button.click()
    time.sleep(2)
    
    cross_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/div[1]'))
    )
    cross_button.click()
    
    print("Finally home. :)")
    
    time.sleep(15)
    
except (ElementNotInteractableException, TimeoutException, ElementClickInterceptedException) as e:
    print(f"Error occurred: {str(e)}")
    sys.exit(1)

finally:
    time.sleep(5)  # Add a delay to see the result
    driver.quit()
    

# Notes for self:
# a popup for "book class now, blue button" or a popup for "plan and free 7 day trial" or no popup

# work on login bot as well ^

# vercel, webook trigger using lambda function 

# clear cookies ^
# wait before submitting ^
# look for XPath alternate, can be by test or css alternate 

# check how we can trigger a github action thru vercel otherwise aws ec2 instance 
# crons in python - how we can use it? - it is a scheduled job 
# vercel app deployment

# keep the name same ^
# change the phone no. to any us number also change input to 12 digit ^
# Password same and global ^

# /html/body/div[1]/div/div[1]/div/div[2]/div/form/div/div[1]/div/div/input
# //*[@id="loginForm"]/div/div[1]/div/div

# /html/body/div[3]/div[2]/section[1]/div/div[1]/div/div/div[2]/div/a
# //*[@id="start-7-day-trial"]/div[2]/div/a

# <span class="MuiButton-label">Book Class</span>
# //*[@id="6668ad8f83b508af71e8b7cb"]/div[2]/div[2]/div/button/span[1]
#\36 668ad8f83b508af71e8b7cb > div.MuiBox-root.jss391.mt-6.md\:mt-0.md\:w-1\/3.flex.flex-row.md\:justify-end.md\:items-center.items-end.justify-between.gap-3 > div.MuiBox-root.jss395.flex.flex-row.md\:gap-3.gap-2 > div > button > span.MuiButton-label