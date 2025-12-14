from soundwarning import ObvestiloZvok
from webcrawler import web_crawler
import misc_lib

def webwatcher(url, searched_text):

    zvok_obvestilo = ObvestiloZvok()

    preverjalnik = web_crawler(url, searched_text, zvok_obvestilo)
    result_num = preverjalnik.preveri_string_v_url()
    print("webwatcher " + str(result_num))
    return result_num


if __name__ == "__main__":
    zvok_obvestilo = ObvestiloZvok()

    webwatcher(misc_lib.url, misc_lib.searched_text)
