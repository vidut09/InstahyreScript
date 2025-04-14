from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the login page
driver.get("https://www.instahyre.com/login")

# Pause to allow manual login
input("Log in manually in the opened browser, then press Enter here to continue...")

# Navigate to the job application page
driver.get("https://www.instahyre.com/candidate/opportunities/?company_size=0&job_functions=%2Fapi%2Fv1%2Fjob_function%2F10&job_type=0&search=true&skills=Java,Spring,Spring+Boot&years=4")

# Wait a bit to ensure the page fully loads
time.sleep(3)

def click_element_with_retry(by_locator, retries=3, wait_time=20):
    """Try to find and click an element, retrying if a stale element error occurs."""
    for attempt in range(retries):
        try:
            element = WebDriverWait(driver, wait_time).until(
                EC.element_to_be_clickable(by_locator)
            )
            element.click()
            return True
        except StaleElementReferenceException:
            print(f"Stale element reference encountered for {by_locator}. Retrying ({attempt+1}/{retries})...")
            time.sleep(1)
    return False

# Try to click the "Apply" button
apply_locator = (By.XPATH, "//button[contains(text(), 'Apply')]")
if click_element_with_retry(apply_locator):
    print("Clicked on the Apply button.")
    # Try to click the "Apply All" button if it appears
    apply_all_locator = (By.XPATH, "//button[contains(text(), 'Apply All')]")
    try:
        if click_element_with_retry(apply_all_locator, retries=2, wait_time=5):
            print("Clicked on the Apply All button.")
        else:
            print("No 'Apply All' popup appeared or it could not be clicked.")
    except Exception as e:
        print("Error while trying to click the 'Apply All' button:", e)
else:
    print("Failed to click the Apply button after several retries.")

# Optionally, close the browser when done
# driver.quit()
