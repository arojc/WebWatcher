import tkinter as tk
from tkinter import ttk
import misc_lib
import threading
from webwatcher import webwatcher
import webbrowser
from website import Website, Websites

case_sensitive = False
global name_entry, url_entry, word_entry, case_btn, output_text, sites, site_index


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
    output_text.config(state="normal")
    output_text.insert(tk.END, message + "\n")
    output_text.see(tk.END)  # skrolaj na dno
    output_text.config(state="disabled")

def clear_output():
    output_text.config(state="normal")
    output_text.delete(1.0, tk.END)
    output_text.config(state="disabled")

def izvedi():
    the_name = name_entry.get()
    the_url = url_entry.get()
    the_word = word_entry.get()

    result = webwatcher(the_url, the_word)

    log(misc_lib.make_report_str_found(result, the_name))

    vstavi_link(output_text, the_name, the_url)
    output_text.configure(state="normal")
    output_text.insert("end", "\n")  # nova vrstica
    output_text.configure(state="disabled")

def izvedi_async():
    threading.Thread(target=izvedi, daemon=True).start()

def show_first_site():
    site_index = sites.sites[0]
    show_new_site()

def show_next_site():
    global site_index
    site_index = sites.sites[(sites.sites.index(site_index)+1)%len(sites.sites)]
    show_new_site()

def show_previous_site():
    global site_index
    site_index = sites.sites[(sites.sites.index(site_index)-1)%len(sites.sites)]
    show_new_site()


def show_new_site():
    if site_index is not None:
        name_entry.delete(0, "end")
        url_entry.delete(0, "end")
        word_entry.delete(0, "end")

        name_entry.insert(0, site_index.name)
        url_entry.insert(0, site_index.url)
        word_entry.insert(0, site_index.words_as_string())

def add_new_site():
    global site_index
    new_site = Website("New site", "https://CHANGE.ME", ["Change","those","words", "for", "Gods", "sake"])
    sites.add(new_site)
    site_index = new_site
    show_new_site()
    save_sites()

def save_site():
    site_index.name = name_entry.get()
    site_index.url = url_entry.get()
    site_index.words = word_entry.get().split(",")

    save_sites()

def save_sites():
    sites.save(misc_lib.config_file_path)

def delete_site():
    global site_index

    old_site_index = site_index

    if len(sites) == 0:
        return
    elif len(sites) == 1:
        add_new_site()

    sites.remove_by_name(old_site_index.name)
    sites.save(misc_lib.config_file_path)


def main():
    global name_entry, url_entry, word_entry, case_btn, output_text, sites, site_index

    sites = Websites.load(misc_lib.config_file_path)
    site_index = sites.sites[0]

    root = tk.Tk()
    root.title("Searching GUI")
    root.geometry("600x420")

    # Ime polje
    tk.Label(root, text="Name:").pack(anchor="w", padx=10, pady=5)
    name_entry = ttk.Entry(root, width=60)
    # name_entry.insert(0, misc_lib.name)
    name_entry.pack(padx=10, pady=5)

    # URL polje
    tk.Label(root, text="URL:").pack(anchor="w", padx=10, pady=5)
    url_entry = ttk.Entry(root, width=60)
    # url_entry.insert(0, misc_lib.url)
    url_entry.pack(padx=10, pady=5)

    # Beseda polje
    tk.Label(root, text="Searched words").pack(anchor="w", padx=10, pady=5)
    word_entry = ttk.Entry(root, width=30)
    # word_entry.insert(0, misc_lib.get_text_searched())
    word_entry.pack(padx=10, pady=5)

    show_first_site()

    # Gumbi v vrstici
    btn_frame1 = tk.Frame(root)
    btn_frame1.pack(padx=10, pady=5, fill="x")

    add_btn = ttk.Button(btn_frame1, text="Dodaj", command=add_new_site)
    add_btn.pack(side="left", padx=5)

    save_btn = ttk.Button(btn_frame1, text="Shrani", command=save_site)
    save_btn.pack(side="left", padx=5)

    del_btn = ttk.Button(btn_frame1, text="Zbriši", command=delete_site)
    del_btn.pack(side="left", padx=5)

    back_btn = ttk.Button(btn_frame1, text="<-", command=show_previous_site)
    back_btn.pack(side="left", padx=5)

    forward_btn = ttk.Button(btn_frame1, text="->", command=show_next_site)
    forward_btn.pack(side="left", padx=5)

    btn_frame2 = tk.Frame(root)
    btn_frame2.pack(padx=10, pady=5, fill="x")

    execute_btn = ttk.Button(btn_frame2, text="Izvedi", command=izvedi_async)
    execute_btn.pack(side="left", padx=5)

    clear_btn = ttk.Button(btn_frame2, text="Počisti", command=clear_output)
    clear_btn.pack(side="left", padx=5)

    # Output polje
    tk.Label(root, text="Rezultati:").pack(anchor="w", padx=10, pady=5)
    output_text = tk.Text(root, height=12, width=70, state="disabled", wrap="word")
    output_text.pack(padx=10, pady=5, fill="both", expand=True)

    root.mainloop()




if __name__ == "__main__":
    main()
