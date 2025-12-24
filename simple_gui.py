import subprocess
import threading

_NOTIFICATION_ID = 4242


def linux_popup(text: str, url: str | None = None, exp_time: int = 0):

    cmd = [
        "notify-send",
        "--replace-id", str(_NOTIFICATION_ID),
        "--urgency", "critical",
        "--expire-time", "0",
        "WebWatcher",
        text
    ]

    if url:
        cmd += [
            "--action", "open=Odpri povezavo"
        ]

        p = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            text=True
        )

        action = p.stdout.read().strip()
        if action == "open":
            subprocess.Popen(["xdg-open", url])

    else:
        subprocess.run(cmd, check=False)


def open_popup(text: str, url: str | None = None, exp_time: int = 0):
    threading.Thread(target=linux_popup, args=(text, url, exp_time)).start()

def close_popup():
    subprocess.run([
        "notify-send",
        "--replace-id", str(_NOTIFICATION_ID),
        "--expire-time", "1",
        " ",
        " "
    ], check=False)

if __name__ == "__main__":
    open_popup(
        "Na strani je bila najdena sprememba.",
        None,
        5
    )
