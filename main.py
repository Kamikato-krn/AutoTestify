from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get("https://allo.ua/")

#Test1
search_input = driver.find_element(By.CLASS_NAME, "search-form__input")
search_input.send_keys("смартфон")
search_button = driver.find_element(By.CLASS_NAME, "search-form__submit-button")
search_button.click()

wait = WebDriverWait(driver, 10)

try:
    search_results = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "products-layout__item")))
except TimeoutException:
    print("Превышено время ожидания")

assert len(search_results) > 0
print(len(search_results))

#Test2
product_card = search_results[2]
product_card.click()

try:
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.ID, "product-buy-button")))
    add_to_cart_button.click()
    sleep(10)

except TimeoutException:
    print("Превышено время ожидания")

driver.quit()