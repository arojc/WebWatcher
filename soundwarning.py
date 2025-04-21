import platform
import os

class ObvestiloZvok:
    def predvajaj(self):
        sistem = platform.system()
        try:
            if sistem == "Windows":
                import winsound
                winsound.Beep(1000, 500)  # frekvenca, trajanje
            elif sistem == "Darwin":
                os.system('say "Obvestilo"')  # macOS
            elif sistem == "Linux":
                os.system('paplay /usr/share/sounds/freedesktop/stereo/complete.oga')  # Ubuntu
            print("Zvok predvajan.")
        except Exception as e:
            print(f"Napaka pri predvajanju zvoka: {e}")
