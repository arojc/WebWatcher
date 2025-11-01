from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re
import time

class web_crawler:

    def __init__(self, url, iskani_niz, obvestilo_zvok=None):
        self.url = url
        self.string = iskani_niz
        self.obvestilo_zvok = obvestilo_zvok

    def preveri_string_v_url(self):
        # Nastavitve za "headless" brskanje (brez GUI-ja)
        options = Options()
        options.add_argument("--headless=new")  # novi headless način
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")  # pomembno za nek JS render

        # Zaženi brskalnik
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        try:
            driver.get(self.url)
            time.sleep(5)  # počakaj, da se JS naloži - prilagodi po potrebi

            html = driver.page_source

            # Odstranimo HTML oznake z BeautifulSoup
            soup = BeautifulSoup(html, "html.parser")
            text = soup.get_text(separator=" ")

            # Normaliziramo presledke (odstranimo več zaporednih presledkov, tabov, \n itd.)
            normalized_text = re.sub(r"\s+", " ", text).strip()

            # Tudi string normaliziramo na enak način
            normalized_string = re.sub(r"\s+", " ", self.string).strip()

            if normalized_string.lower() in normalized_text.lower():
                report = f"Niz '{self.string}' JE bil {normalized_text.lower().count(normalized_string.lower())}-krat najden na strani."
                return report
            else:
                report = f"Niz '{self.string}' NI bil najden na strani."
                return report
        except Exception as e:
            print(f"Napaka: {e}")
        finally:
            driver.quit()
