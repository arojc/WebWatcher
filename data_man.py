import os, json
from website import Website, Websites

url = "https://e-uprava.gov.si/e-uprava/oglasnadeska.html?lang=si#eyJmaWx0ZXJzIjp7InR5cGUiOlsiLSJdLCJwZXJpb2RhIjpbIi0iXSwicmlqcyI6WyIyMjk2Il0sIm9mZnNldCI6WyIwIl0sInNlbnRpbmVsX3R5cGUiOlsib2siXSwic2VudGluZWxfc3RhdHVzIjpbIm9rIl0sImlzX2FqYXgiOlsiMSJdfX0="
searched_text = "radomlje"



class data_man():

    def __init__(self):
        # self.watch_list = {}
        self.APP = "webwatcher"
        self.CFG_DIR = os.path.join(os.path.expanduser("~"), ".config", self.APP)
        self.CFG = os.path.join(self.CFG_DIR, "config2.json")
        os.makedirs(self.CFG_DIR, exist_ok=True)

    def get_data(self):
        if os.path.exists(self.CFG):
            return Website.from_dict(json.load(open(self.CFG)))
        return searched_text

    def get_datas(self):
        return Websites.load(self.CFG)

    def set_data(self, n):
        if isinstance(n, Websites):
            n.save(self.CFG)
        else:
            json.dump(n.to_list(), open(self.CFG, "w"))


if __name__ == "__main__":
    site1 = Website(
        name="Example1",
        url="https://example1.com",
        words=["Example1Domain"]
    )
    site2 = Website(
        name="Example2",
        url="https://example2.com",
        words=["Example2Domain"]
    )
    sites = Websites()

    sites.add(site1)
    sites.add(site2)


    dm = data_man()
    dm.set_data(sites)
    sites1 = dm.get_datas()
    print(sites1)
