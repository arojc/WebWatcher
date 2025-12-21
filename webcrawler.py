from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup
import re
import time
import socket
import simple_gui as sg

class web_crawler:

    def __init__(self, url, iskani_nizi, obvestilo_zvok=None):
        self.url = url
        self.stringi = iskani_nizi
        self.obvestilo_zvok = obvestilo_zvok

    def preveri_string_v_url(self):
        # Nastavitve za "headless" brskanje (brez GUI-ja)
        options = Options()
        options.add_argument("-headless")  # novi headless način
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference("useAutomationExtension", False)

        self.wait_for_internet()

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

            thesum = 0
            for word in self.stringi:
                # Tudi string normaliziramo na enak način
                normalized_string = re.sub(r"\s+", " ", word).strip()
                thesum += normalized_text.lower().count(normalized_string.lower())


            return thesum
        except Exception as e:
            print(f"Napaka: {e}")
        finally:
            driver.quit()


    def wait_for_internet(self, interval: int = 5, timeout: int = 3):
        root = None
        popup_shown = False

        while True:
            try:
                socket.create_connection(("8.8.8.8", 53), timeout=timeout)

                # Če je popup odprt, ga zapremo
                if popup_shown and root:
                    sg.close_popup()

                print("Internetna povezava je na voljo.")
                return

            except OSError:
                print("Ni interneta.")

                if not popup_shown:
                    popup_shown = True
                    sg.open_popup("Ni internetne povezave", None)

                time.sleep(interval)


