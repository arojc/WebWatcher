import tkinter as tk
from tkinter import ttk
import misc_lib
import threading
from webwatcher import webwatcher
import webbrowser
from data_man import data_man
from website import Website, Websites

case_sensitive = False

def vstavi_link(text_widget: tk.Text, besedilo: str, url: str):
    text_widget.configure(state="normal")

    start = text_widget.index("end-1c")
    text_widget.insert("end", besedilo)
    end = text_widget.index("end-1c")

    tag = f"link_{start.replace('.', '_')}"

    text_widget.tag_add(tag, start, end)

    # osnovni izgled linka
    text_widget.tag_config(
        tag,
        foreground="blue",
        underline=True
    )

    # hover efekt
    text_widget.tag_bind(tag, "<Enter>", lambda e: text_widget.config(cursor="hand2"))
    text_widget.tag_bind(tag, "<Leave>", lambda e: text_widget.config(cursor=""))

    # klik
    text_widget.tag_bind(
        tag,
        "<Button-1>",
        lambda e: webbrowser.open_new_tab(url)
    )

    text_widget.configure(state="disabled")




def log(message: str):
    """Izpiše sporočilo v tekstovno polje."""
    output_text.config(state="normal")
    output_text.insert(tk.END, message + "\n")
    output_text.see(tk.END)  # skrolaj na dno
    output_text.config(state="disabled")


def clear_output():
    """Počisti izpis v tekstovnem polju."""
    output_text.config(state="normal")
    output_text.delete(1.0, tk.END)
    output_text.config(state="disabled")


def toggle_case():
    """Preklopi stanje case sensitivity."""
    global case_sensitive
    case_sensitive = not case_sensitive
    if case_sensitive:
        case_btn.config(text="Case sensitive: ON")
    else:
        case_btn.config(text="Case sensitive: OFF")


def izvedi():

    the_name = name_entry.get()
    the_url = url_entry.get()
    the_word = word_entry.get()

    result = webwatcher(the_url, the_word)

    log(misc_lib.make_report_str_found(result, the_word))

    vstavi_link(output_text, the_name, the_url)
    output_text.configure(state="normal")
    output_text.insert("end", "\n")  # nova vrstica
    output_text.configure(state="disabled")


def izvedi_async():
    """Zažene izvedi() v ločeni niti, da GUI ne zamrzne."""
    threading.Thread(target=izvedi, daemon=True).start()


def show_site_by_name(name: str):
    site = sites.get_by_name(name)
    if site is not None:
        name_entry.insert(0, site.name)
        url_entry.insert(0, site.url)
        word_entry.insert(0, site.words_as_string())

def show_first_site():
    site = sites.sites[0]
    show_new_site(site)

def show_next_site():
    global site_index
    site_index = (site_index+1)%len(sites.sites)
    site = sites.sites[site_index]
    show_new_site(site)

def show_previous_site():
    global site_index
    site_index = (site_index-1)%len(sites.sites)
    site = sites.sites[site_index]
    show_new_site(site)


def show_new_site(site: Website):
    if site is not None:
        name_entry.delete(0, "end")
        url_entry.delete(0, "end")
        word_entry.delete(0, "end")

        name_entry.insert(0, site.name)
        url_entry.insert(0, site.url)
        word_entry.insert(0, site.words_as_string())



def main():
    global name_entry, url_entry, word_entry, case_btn, output_text, sites, site_index

    sites = Websites.load("/home/antonrojc/.config/webwatcher/config2.json")
    site_index = 0

    root = tk.Tk()
    root.title("Iskalni GUI")
    root.geometry("600x420")

    # Ime polje
    tk.Label(root, text="Ime:").pack(anchor="w", padx=10, pady=5)
    name_entry = ttk.Entry(root, width=60)
    name_entry.insert(0, misc_lib.name)
    name_entry.pack(padx=10, pady=5)

    # URL polje
    tk.Label(root, text="URL:").pack(anchor="w", padx=10, pady=5)
    url_entry = ttk.Entry(root, width=60)
    url_entry.insert(0, misc_lib.url)
    url_entry.pack(padx=10, pady=5)

    # Beseda polje
    tk.Label(root, text="Beseda").pack(anchor="w", padx=10, pady=5)
    word_entry = ttk.Entry(root, width=30)
    word_entry.insert(0, misc_lib.get_text_searched())
    word_entry.pack(padx=10, pady=5)

    show_first_site()

    # Gumbi v vrstici
    btn_frame = tk.Frame(root)
    btn_frame.pack(padx=10, pady=5, fill="x")

    case_btn = ttk.Button(btn_frame, text="Case sensitive: OFF", command=toggle_case)
    case_btn.pack(side="left", padx=5)

    execute_btn = ttk.Button(btn_frame, text="Izvedi", command=izvedi_async)
    execute_btn.pack(side="left", padx=5)

    clear_btn = ttk.Button(btn_frame, text="Počisti", command=clear_output)
    clear_btn.pack(side="left", padx=5)

    save_btn = ttk.Button(btn_frame, text="Shrani", command=save_value)
    save_btn.pack(side="left", padx=5)

    back_btn = ttk.Button(btn_frame, text="<-", command=show_previous_site)
    back_btn.pack(side="left", padx=5)

    forward_btn = ttk.Button(btn_frame, text="->", command=show_next_site)
    forward_btn.pack(side="left", padx=5)

    # Output polje
    tk.Label(root, text="Rezultati:").pack(anchor="w", padx=10, pady=5)
    output_text = tk.Text(root, height=12, width=70, state="disabled", wrap="word")
    output_text.pack(padx=10, pady=5, fill="both", expand=True)

    root.mainloop()

def save_value():
    misc_lib.set_text_searched(word_entry.get())

def str_to_list(words: str):
    return words.split(',')

def list_to_string(words):
    return ",".join(words)


if __name__ == "__main__":
    main()
