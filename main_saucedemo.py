import pytest
from selenium import webdriver
from pages import LoginPage, InventoryPage

def main_saucedemo_flow():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    
    try:
        #Login
        login_pg = LoginPage(driver)
        driver.get("https://www.saucedemo.com")
        login_pg.login("standard_user", "secret_sauce")
        
        #Add to Cart
        inv_pg = InventoryPage(driver)
        inv_pg.add_first_item()
        
        #Validation
        assert inv_pg.get_cart_count() == "1"
        print("Test Passed: Item added to cart.")
        
    except Exception as e:
        driver.save_screenshot("error_screenshot.png")
        print(f"Test Failed: {e}")
        raise e
    finally:
        driver.quit()
