from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv
from gui import create_window  # Importar la función para crear la ventana
import PySimpleGUI as sg

def main():
    # Cargar variables de entorno desde el archivo .env
    load_dotenv()

    # Crear la ventana

    window = create_window()

    while True:
        event, _ = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == "Run Selenium Script":
            try:
                run_selenium_script()
            except Exception as e:
                sg.popup_error(f"An error occurred: {e}")

    window.close()

def run_selenium_script():
    with webdriver.Chrome() as driver:
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")

        login(driver)
        add_backpack(driver)

def login(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "user-name")))

    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

def add_backpack(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

if __name__ == "__main__":
    main()