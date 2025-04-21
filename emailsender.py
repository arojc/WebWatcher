import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class ObvestiloEmail:
    def __init__(self, posiljatelj, geslo, prejemnik):
        self.posiljatelj = posiljatelj
        self.geslo = geslo
        self.prejemnik = prejemnik

    def poslji(self, zadeva, sporocilo):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.posiljatelj
            msg['To'] = self.prejemnik
            msg['Subject'] = zadeva
            msg.attach(MIMEText(sporocilo, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.posiljatelj, self.geslo)
            server.sendmail(self.posiljatelj, self.prejemnik, msg.as_string())
            server.quit()
            print("E-poštno obvestilo poslano.")
        except Exception as e:
            print(f"Napaka pri pošiljanju e-pošte: {e}")
