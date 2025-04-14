import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Replace with your actual credentials
EMAIL = "vidutmishra@gmail.com"
PASSWORD = "beBrave@09"

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the Instahyre login page
driver.get("https://www.instahyre.com/login")

try:
    # Wait for the email field and enter your email
    email_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    email_field.send_keys(EMAIL)

    # Locate and fill the password field
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys(PASSWORD)

    # Locate and click the login button
    login_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")
    login_button.click()

    # Optional: wait for an element that confirms login was successful.
    # For example, wait a few seconds or for a dashboard element to appear.
    time.sleep(5)
except Exception as e:
    print("Error during login:", e)
    driver.quit()
    exit(1)

# Pause to allow you to manually apply filters after login
input("After logging in and applying filters manually, press Enter to start applying for jobs...")

# Loop: Wait for the "Apply" button, click it, and handle the optional "Apply All" popup.
while True:
    try:
        # Wait for an "Apply" button to be clickable (adjust the XPath as needed)
        apply_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Apply')]"))
        )
        apply_button.click()
        print("Clicked the 'Apply' button.")

        # Wait briefly and check for an "Apply All" popup, and click if it appears
        try:
            apply_all_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Apply All')]"))
            )
            apply_all_button.click()
            print("Clicked the 'Apply All' button.")
        except TimeoutException:
            print("'Apply All' popup did not appear for this job.")

        # Wait a short while to allow the application process to complete
        time.sleep(2)
    except TimeoutException:
        print("No more 'Apply' buttons found. Exiting the application loop.")
        break
    except Exception as e:
        print("An error occurred while processing a job:", e)
        break

# Optionally close the browser when finished
driver.quit()
