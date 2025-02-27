import random
import string
import time
import sys

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException, TimeoutException, ElementClickInterceptedException

driver = webdriver.Chrome()

try:
    driver.get("https://shvasa.com")
    
    # Clear cookies
    print(driver.get_cookies())
    driver.delete_all_cookies()
    driver.delete_all_cookies()

    login_button = WebDriverWait(driver, 30).until(
        # EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Start free trial Now')]"))
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div/div/a/div/div"))
    )
    login_button.click()
    
    # No iframe for login
    
    # Wait for the login window to appear
    login_window_present = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']"))
    )
    print("Login form is present!")

    # Generate random name, phone number, and password
    test_name = 'Test'
    test_phone_number = '2345678910'
    test_password = 'test@123'
    test_email = 'testbot@shvasa.com'
    print("Bot Details: ",test_name, test_phone_number, test_password, test_email)

    # Fill in the login form
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/div/input'))
    )
    email_input.click()
    email_input.send_keys(test_email)
    time.sleep(2)

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/div/input'))
    )
    password_input.click()
    password_input.send_keys(test_password)
    time.sleep(2)

    login_submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[4]/button/span[1]/div'))
    )
    login_submit_button.click()
    
    print("Logged In!")
    time.sleep(5)
    
    # book_a_class_button = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '/html/body/div[8]/div[3]/div/div[2]/div[4]/button/span[1]'))
    # )
    # book_a_class_button.click()
    
    # buttons = WebDriverWait(driver, 10).until(
    #     EC.presence_of_all_elements_located((By.XPATH, "//button[contains(., 'Book Class')]"))
    # )

    # booked_classes = 0
    # max_classes_to_book = 3

    # while booked_classes < max_classes_to_book:
    #     for button in buttons:
    #         try:
    #             button.click()
    #             print("Class booked successfully!")
    #             booked_classes += 1
    #             time.sleep(5)
    #             if booked_classes >= max_classes_to_book:
    #                 break
    #         except (ElementClickInterceptedException, ElementNotInteractableException, TimeoutException) as e:
    #             print(f"Skipping non-interactable button due to error: {str(e)}")
    #             driver.execute_script("window.scrollBy(0, 100);")  # Scroll down a bit to try the next button
    #             continue

    #     if booked_classes < max_classes_to_book:
    #         # Scroll down and find more "Book Class" buttons
    #         driver.execute_script("window.scrollBy(0, 1000);")
    #         time.sleep(5)
    #         buttons = driver.find_elements(By.XPATH, "//button[contains(., 'Book Class')]")
        
    # print(f"Booked {booked_classes} classes successfully!")
    # time.sleep(5)  
    
    # go_to_home_button = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div[3]/div[2]/div/div[2]/button/span[1]/span'))
    # )
    # go_to_home_button.click()
    # time.sleep(2)
    
    # cross_button = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/div[1]'))
    # )
    # cross_button.click()
    
    # print("Finally home. :)")
    # time.sleep(15)
    
    
except Exception as e:
    print(f"Error occurred: {str(e)}")
    sys.exit(1)

finally:
    time.sleep(5)  # Add a delay to see the result
    driver.quit()
    
