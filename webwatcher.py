from soundwarning import ObvestiloZvok
from webcrawler import web_crawler
import misc_lib
import simple_gui as sg


def webwatcher(url, searched_text):

    zvok_obvestilo = ObvestiloZvok()

    preverjalnik = web_crawler(url, searched_text.split(','), zvok_obvestilo)
    result_num = preverjalnik.preveri_string_v_url()
    return result_num


if __name__ == "__main__":
    zvok_obvestilo = ObvestiloZvok()
    the_word = misc_lib.get_text_searched()

    result_num = webwatcher(misc_lib.url, the_word)
    print("webwatcher " + the_word + " " + str(result_num))

    if result_num > 0:
        sg.open_popup(misc_lib.make_report_str_found(result_num, the_word), misc_lib.url)
    else:
        sg.open_popup(misc_lib.make_report_str_found(result_num, the_word))

    zvok_obvestilo.predvajaj()


