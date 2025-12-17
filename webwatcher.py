from soundwarning import ObvestiloZvok
from webcrawler import web_crawler
import misc_lib
import tkinter as tk
import webbrowser

def webwatcher(url, searched_text):

    zvok_obvestilo = ObvestiloZvok()

    preverjalnik = web_crawler(url, searched_text, zvok_obvestilo)
    result_num = preverjalnik.preveri_string_v_url()
    return result_num


def okno_z_linkom(text_widget: tk.Text, besedilo: str, url: str):
    start_index = text_widget.index("insert")
    text_widget.insert("insert", besedilo)

    end_index = text_widget.index("insert")

    tag_name = f"link_{start_index}"

    text_widget.tag_add(tag_name, start_index, end_index)
    text_widget.tag_config(
        tag_name,
        foreground="blue",
        underline=True
    )

    text_widget.tag_bind(
        tag_name,
        "<Button-1>",
        lambda e: webbrowser.open(url)
    )

if __name__ == "__main__":
    zvok_obvestilo = ObvestiloZvok()

    result_num = webwatcher(misc_lib.url, misc_lib.load())
    print("webwatcher " + misc_lib.load() + " " + str(result_num))

    if result_num > 0:
        zvok_obvestilo.predvajaj()
        zvok_obvestilo.predvajaj()

        root = tk.Tk()
        text = tk.Text(root, width=50, height=10)
        text.pack()
        okno_z_linkom(text, misc_lib.make_report_str_found(result_num, misc_lib.load()), misc_lib.url)
        root.attributes("-topmost", True)
        root.mainloop()
    else:
        zvok_obvestilo.predvajaj()