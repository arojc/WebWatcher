from soundwarning import ObvestiloZvok
from webcrawler import web_crawler

def webwatcher(url, searched_text):

    zvok_obvestilo = ObvestiloZvok()

    preverjalnik = web_crawler(url, searched_text, zvok_obvestilo)
    report = preverjalnik.preveri_string_v_url()
    print("webwatcher " + report)
    return report


if __name__ == "__main__":
    url = "https://e-uprava.gov.si/e-uprava/oglasnadeska.html?lang=si#eyJmaWx0ZXJzIjp7InR5cGUiOlsiLSJdLCJwZXJpb2RhIjpbIi0iXSwicmlqcyI6WyIyMjk2Il0sIm9mZnNldCI6WyIwIl0sInNlbnRpbmVsX3R5cGUiOlsib2siXSwic2VudGluZWxfc3RhdHVzIjpbIm9rIl0sImlzX2FqYXgiOlsiMSJdfX0="
    searched_text = "radomlje"
    zvok_obvestilo = ObvestiloZvok()

    webwatcher(url, searched_text)
