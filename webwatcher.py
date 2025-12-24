from soundwarning import ObvestiloZvok
from webcrawler import web_crawler
import misc_lib
import simple_gui as sg
from website import Websites, Website


def webwatcher(url, searched_text):

    zvok_obvestilo = ObvestiloZvok()

    preverjalnik = web_crawler(url, searched_text.split(','), zvok_obvestilo)
    result_num = preverjalnik.preveri_string_v_url()
    return result_num


if __name__ == "__main__":
    zvok_obvestilo = ObvestiloZvok()

    sites = Websites.load("/home/antonrojc/.config/webwatcher/config2.json")

    for site in sites:
        print(site.name)

        result_num = webwatcher(site.url, site.words_as_string())
        print("webwatcher " + site.name + " " + str(result_num))

        if result_num > 0:
            sg.open_popup(misc_lib.make_report_str_found(result_num, site.name), site.url)
        else:
            sg.open_popup(misc_lib.make_report_str_found(result_num, site.name))

        zvok_obvestilo.predvajaj()


