import tkinter as tk
from tkinter import ttk
import threading

from webwatcher import webwatcher

case_sensitive = False
url = "https://e-uprava.gov.si/e-uprava/oglasnadeska.html?lang=si#eyJmaWx0ZXJzIjp7InR5cGUiOlsiLSJdLCJwZXJpb2RhIjpbIi0iXSwicmlqcyI6WyIyMjk2Il0sIm9mZnNldCI6WyIwIl0sInNlbnRpbmVsX3R5cGUiOlsib2siXSwic2VudGluZWxfc3RhdHVzIjpbIm9rIl0sImlzX2FqYXgiOlsiMSJdfX0="
word = "radomlje"


import webbrowser
# import tkinter as tk

import webbrowser
# import tkinter as tk

def vstavi_link(text_widget: tk.Text, besedilo: str, url: str):
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
    """Tukaj bo kasneje glavna logika."""

    # url = "https://e-uprava.gov.si/e-uprava/oglasnadeska.html?lang=si#eyJmaWx0ZXJzIjp7InR5cGUiOlsiLSJdLCJwZXJpb2RhIjpbIi0iXSwicmlqcyI6WyIyMjk2Il0sIm9mZnNldCI6WyIwIl0sInNlbnRpbmVsX3R5cGUiOlsib2siXSwic2VudGluZWxfc3RhdHVzIjpbIm9rIl0sImlzX2FqYXgiOlsiMSJdfX0="
    # word = "radomlje"

    report = str(webwatcher(url_entry.get(), word_entry.get()))

    log(report)

    root = tk.Tk()

    text = tk.Text(root, width=50, height=10)
    text.pack()

    vstavi_link(text, "Odpri OpenAI", "https://www.openai.com")

    root.mainloop()


def izvedi_async():
    """Zažene izvedi() v ločeni niti, da GUI ne zamrzne."""
    threading.Thread(target=izvedi, daemon=True).start()


def main():
    global url_entry, word_entry, case_btn, output_text

    root = tk.Tk()
    root.title("Iskalni GUI")
    root.geometry("600x420")

    # URL polje
    tk.Label(root, text="URL:").pack(anchor="w", padx=10, pady=5)
    url_entry = ttk.Entry(root, width=60)
    url_entry.insert(0, url)
    url_entry.pack(padx=10, pady=5)

    # Beseda polje
    tk.Label(root, text="Beseda").pack(anchor="w", padx=10, pady=5)
    word_entry = ttk.Entry(root, width=30)
    word_entry.insert(0, word)
    word_entry.pack(padx=10, pady=5)

    # Gumbi v vrstici
    btn_frame = tk.Frame(root)
    btn_frame.pack(padx=10, pady=5, fill="x")

    case_btn = ttk.Button(btn_frame, text="Case sensitive: OFF", command=toggle_case)
    case_btn.pack(side="left", padx=5)

    execute_btn = ttk.Button(btn_frame, text="Izvedi", command=izvedi_async)
    execute_btn.pack(side="left", padx=5)

    clear_btn = ttk.Button(btn_frame, text="Počisti", command=clear_output)
    clear_btn.pack(side="left", padx=5)

    # Output polje
    tk.Label(root, text="Rezultati:").pack(anchor="w", padx=10, pady=5)
    output_text = tk.Text(root, height=12, width=70, state="disabled", wrap="word")
    output_text.pack(padx=10, pady=5, fill="both", expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()
