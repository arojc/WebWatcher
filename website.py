from typing import List, Dict
import json


class Website:
    def __init__(self, name: str, url: str, words: List[str] | None = None):
        self._name = ""
        self._url = ""
        self._words = []

        self.name = name
        self.url = url
        self.words = words if words is not None else []

    # ---------- name ----------
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("name mora biti neprazen string")
        self._name = value.strip()

    # ---------- url ----------
    @property
    def url(self) -> str:
        return self._url

    @url.setter
    def url(self, value: str):
        if not isinstance(value, str) or not value.startswith(("http://", "https://")):
            raise ValueError("url mora biti veljaven http/https naslov")
        self._url = value.strip()

    # ---------- words ----------
    @property
    def words(self) -> List[str]:
        return self._words

    @words.setter
    def words(self, value: List[str]):
        if not isinstance(value, list):
            raise ValueError("words mora biti lista stringov")

        cleaned = []
        for word in value:
            if not isinstance(word, str) or not word.strip():
                raise ValueError("vsak element v words mora biti neprazen string")
            cleaned.append(word.strip())

        self._words = cleaned

    # ---------- helpers ----------
    def add_word(self, word: str):
        if not isinstance(word, str) or not word.strip():
            raise ValueError("word mora biti neprazen string")
        word = word.strip()
        if word not in self._words:
            self._words.append(word)

    def remove_word(self, word: str):
        if word in self._words:
            self._words.remove(word)

    def words_as_string(self) -> str:
        return ",".join(self._words)

    # ---------- JSON ----------
    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "url": self.url,
            "words": self.words
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "Website":
        return cls(
            name=data.get("name", ""),
            url=data.get("url", ""),
            words=data.get("words", [])
        )

    def __repr__(self):
        return f"Website(name='{self.name}', url='{self.url}', words={self.words})"


class Websites:
    def __init__(self, sites: List[Website] | None = None):
        self._sites: List[Website] = sites if sites is not None else []

    # ---------- access ----------
    @property
    def sites(self) -> List[Website]:
        return self._sites

    def add(self, site: Website):
        if not isinstance(site, Website):
            raise ValueError("site mora biti instance Website")

        if self.get_by_url(site.url):
            raise ValueError(f"Website z URL '{site.url}' že obstaja")

        if self.get_by_name(site.name):
            raise ValueError(f"Website z imenom '{site.name}' že obstaja")

        self._sites.append(site)

    def remove_by_url(self, url: str):
        self._sites = [s for s in self._sites if s.url != url]

    def remove_by_name(self, name: str):
        self._sites = [s for s in self._sites if s.name != name]

    def get_by_url(self, url: str) -> Website | None:
        for site in self._sites:
            if site.url == url:
                return site
        return None

    def get_by_name(self, name: str) -> Website | None:
        for site in self._sites:
            if site.name == name:
                return site
        return None

    def get_by_name(self, name: str) -> Website | None:
        for site in self._sites:
            if site.name == name:
                return site
        return None

    # ---------- JSON ----------
    def to_list(self) -> List[Dict]:
        return [site.to_dict() for site in self._sites]

    @classmethod
    def from_list(cls, data: List[Dict]) -> "Websites":
        sites = [Website.from_dict(item) for item in data]
        return cls(sites)

    def save(self, path: str):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_list(), f, indent=2, ensure_ascii=False)

    @classmethod
    def load(cls, path: str) -> "Websites":
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return cls.from_list(data)

    # ---------- helpers ----------
    def __len__(self):
        return len(self._sites)

    def __iter__(self):
        return iter(self._sites)

    def __repr__(self):
        return f"Websites({self._sites})"
