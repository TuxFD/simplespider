from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://shop.ms-armaturen.de/Rohrverbindungen/?order=m-s-artikelnummer-aufsteigend&p=1"


def selenium_spell(url=URL):
    fox_options = Options()
    driver = webdriver.Firefox(options=fox_options)
    try:
        driver.get(url)
        element = driver.find_element(By.CLASS_NAME, "page-last")
        element.click()

        wait = WebDriverWait(driver, 30)
        wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "filter-panel-item-toggle"))
        )

        element = driver.find_element(
            By.XPATH, "//nav/ul/li[contains(@class, 'page-item') and contains(@class, 'active')]"
        )
        last_page = element.text
        print(last_page)
        driver.close()
    except Exception as e:
        print("==== ERROR ====")
        print(e)
        driver.close()


if __name__ == "__main__":
    selenium_spell()
