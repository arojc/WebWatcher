import os, json

url = "https://e-uprava.gov.si/e-uprava/oglasnadeska.html?lang=si#eyJmaWx0ZXJzIjp7InR5cGUiOlsiLSJdLCJwZXJpb2RhIjpbIi0iXSwicmlqcyI6WyIyMjk2Il0sIm9mZnNldCI6WyIwIl0sInNlbnRpbmVsX3R5cGUiOlsib2siXSwic2VudGluZWxfc3RhdHVzIjpbIm9rIl0sImlzX2FqYXgiOlsiMSJdfX0="
searched_text = "radomlje"



class data_man():

    def __init__(self):
        self.watch_list = {}
        self.APP = "webwatcher"
        self.CFG_DIR = os.path.join(os.path.expanduser("~"), ".config", self.APP)
        self.CFG = os.path.join(self.CFG_DIR, "config2.json")
        os.makedirs(self.CFG_DIR, exist_ok=True)

    def get_data(self):
        if os.path.exists(self.CFG):
            return json.load(open(self.CFG))
        return searched_text

    def set_data(self, n):
        json.dump(n, open(self.CFG, "w"))


if __name__ == "__main__":
    name = "uedomzale"
    dm = data_man()
    dm.watch_list[name] = []
    dm.watch_list[name].append("url")
    dm.watch_list[name].append("radomlje")
    dm.watch_list[name].append("trzin")
    dm.set_data(dm.watch_list)
    data = dm.get_data()
    print(data)
