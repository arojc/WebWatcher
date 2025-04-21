from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import re
import time

from soundwarning import ObvestiloZvok

# Globalni spremenljivki
url = "https://e-uprava.gov.si/e-uprava/oglasnadeska.html?lang=si#eyJmaWx0ZXJzIjp7InR5cGUiOlsiLSJdLCJwZXJpb2RhIjpbIi0iXSwicmlqcyI6WyIyMjk2Il0sIm9mZnNldCI6WyIwIl0sInNlbnRpbmVsX3R5cGUiOlsib2siXSwic2VudGluZWxfc3RhdHVzIjpbIm9rIl0sImlzX2FqYXgiOlsiMSJdfX0="
# string = "330-189"
string = "20 rezultatov"

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
            driver.get(url)
            time.sleep(5)  # počakaj, da se JS naloži - prilagodi po potrebi

            html = driver.page_source

            # Odstranimo HTML oznake z BeautifulSoup
            soup = BeautifulSoup(html, "html.parser")
            text = soup.get_text(separator=" ")

            # Normaliziramo presledke (odstranimo več zaporednih presledkov, tabov, \n itd.)
            normalized_text = re.sub(r"\s+", " ", text).strip()

            # Tudi string normaliziramo na enak način
            normalized_string = re.sub(r"\s+", " ", string).strip()

            if normalized_string.lower() in normalized_text.lower():
                print(f"Niz '{string}' JE bil najden na strani {url}.")
                self.obvestilo_zvok.predvajaj()
            else:
                print(f"Niz '{string}' NI bil najden na strani {url}.")
        except Exception as e:
            print(f"Napaka: {e}")
        finally:
            driver.quit()

