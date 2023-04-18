from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://allo.ua/")

search_input = driver.find_element(By.CLASS_NAME, "search-form__input")
search_input.send_keys("смартфон")
search_button = driver.find_element(By.CLASS_NAME, "search-form__submit-button")
search_button.click()

wait = WebDriverWait(driver, 10)
search_results = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "products-layout__item")))

assert len(search_results) > 0,
print(len(search_results))