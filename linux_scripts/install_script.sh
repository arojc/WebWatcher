mkdir -p ~/.config/systemd/user
cp webwatcher.service ~/.config/systemd/user


systemctl --user daemon-reexec

systemctl --user enable webwatcher.service

#systemctl --user start webwatcher.service
#journalctl --user -u webwatcher.service -f


