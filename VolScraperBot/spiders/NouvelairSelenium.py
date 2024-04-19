from selenium import webdriver #webdriver est un classe  de base qui permet d'interagir avec le navigateur importé pour utiliser les méthodes et attributs de cette classe
# import nouvelair.constants as const
import os
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait #attente explicite  sur un élément de la page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Booking (webdriver.Chrome): 
    def __init__(self, driver_path="C:/Users/medamine/VolScraperBot/chromedriver.exe") :
        opts = webdriver.ChromeOptions()
        opts.add_argument("--headless") 
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Booking,self).__init__() 
        self.implicitly_wait(15)
        self.maximize_window()
    
    def land_first_page (self) :
        self.implicitly_wait(60)
        self.get("https://www.nouvelair.com/fr")

    
    def accept_cookies(self):
        self.implicitly_wait(30)
        accept_bouton = WebDriverWait(self,10).until(
        EC.element_to_be_clickable((By.XPATH,'//*[@id="rcc-confirm-button"]'))
        )
        accept_bouton.click()    

    
    def select_place_of_departure(self,place_of_departure) :
        self.implicitly_wait(30)
        country_of_departure = WebDriverWait(self,10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,'div.MuiGrid-root.form-container.departure-container.MuiGrid-item input.MuiInputBase-input.MuiInput-input.MuiAutocomplete-input.MuiAutocomplete-inputFocused'))
        )
        country_of_departure.send_keys(place_of_departure)
        if (str(place_of_departure).lower() == "tunis"):
            self.find_element(By.CSS_SELECTOR , 'li[data-option-index="2"]').click()
            self.implicitly_wait(30)
            time.sleep(1)
        elif (str(place_of_departure).lower() != "tunis"):
            self.find_element(By.CSS_SELECTOR , 'li[data-option-index="0"]').click()
            time.sleep(1)

            
    def select_place_of_arrival(self , place_of_arrival): 
        self.implicitly_wait(30)
        country_of_arrival = WebDriverWait(self, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.MuiGrid-root.form-container.destination-container.MuiGrid-item input.MuiInputBase-input.MuiInput-input.MuiAutocomplete-input.MuiAutocomplete-inputFocused'))
        )
        country_of_arrival.send_keys(place_of_arrival)
        if (str(place_of_arrival).lower() == "tunis"):
            time.sleep(0.5)
            self.find_element(By.CSS_SELECTOR , 'li[data-option-index="2"]').click()
            time.sleep(1)
        elif (str(place_of_arrival).lower() != "tunis") :
            time.sleep(0.5)
            self.find_element(By.CSS_SELECTOR , 'li[data-option-index="0"]').click()
            time.sleep(1)


    def select_dates (self ,check_in_date , check_out_date, type):
        self.implicitly_wait(30)
        calendar = self.find_element(By.CSS_SELECTOR, 'div[class="MuiGrid-root date-selector-container-input   MuiGrid-container"]')
        calendar.click()        
        if  type == "aller-retour" :
            self.implicitly_wait(60)
            time.sleep(0.5)
            date_check_in = WebDriverWait(self, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f'button[aria-label="{check_in_date}"]')))
            date_check_in.click()
            time.sleep(0.5)
            date_check_out = WebDriverWait(self, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f'button[aria-label="{check_out_date}"]')))
            date_check_out.click() 
            self.implicitly_wait(60)

        else :
            self.implicitly_wait(30)
            self.find_element(By.NAME,'oneWay').click()  
            date_check_in = WebDriverWait(self, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f'button[aria-label="{check_in_date}"]')))
            date_check_in.click()
            self.implicitly_wait(30)

            

    def calendar_exit(self):
        self.implicitly_wait(60)
        self.find_element(By.CSS_SELECTOR, 'button[class="MuiButtonBase-root MuiTab-root MuiTab-textColorInherit Mui-selected"]').click()
        self.implicitly_wait(60)


    def click_search(self):
        self.implicitly_wait(60)
        self.find_element(By.CSS_SELECTOR, 'button[class="MuiButtonBase-root MuiButton-root MuiButton-text flights-search-btn"][aria-label="RECHERCHER"]').click()
        self.implicitly_wait(60)
        time.sleep(2)


    def page_loaded(self):
        time.sleep(0.5)
        return self.current_url
    
    
    def close_browser(self):
        self.quit()
    
