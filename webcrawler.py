from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
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
        options.add_argument("-headless")  # novi headless način
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference("useAutomationExtension", False)

        # Zaženi brskalnik
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

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
