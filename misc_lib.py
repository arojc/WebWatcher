import os, json

url = "https://e-uprava.gov.si/e-uprava/oglasnadeska.html?lang=si#eyJmaWx0ZXJzIjp7InR5cGUiOlsiLSJdLCJwZXJpb2RhIjpbIi0iXSwicmlqcyI6WyIyMjk2Il0sIm9mZnNldCI6WyIwIl0sInNlbnRpbmVsX3R5cGUiOlsib2siXSwic2VudGluZWxfc3RhdHVzIjpbIm9rIl0sImlzX2FqYXgiOlsiMSJdfX0="
searched_text = "radomlje"

def make_report_str_found(n_of_found: int, thestr: str):
    if n_of_found > 0:
        return f"Niz '{thestr}' JE bil {n_of_found}-krat najden na strani."
    else:
        return f"Niz '{thestr}' NI bil najden na strani."



APP = "webwatcher"
CFG_DIR = os.path.join(os.path.expanduser("~"), ".config", APP)
CFG = os.path.join(CFG_DIR, "config.json")
os.makedirs(CFG_DIR, exist_ok=True)

def get_text_searched():
    if os.path.exists(CFG):
        return json.load(open(CFG))["n"]
    return searched_text

def set_text_searched(n):
    print("save: " + n)
    json.dump({"n": n}, open(CFG, "w"))
