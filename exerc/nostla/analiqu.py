from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, str_path))).click()
