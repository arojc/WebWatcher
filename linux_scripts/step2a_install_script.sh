# execute from /linux_scripts

## PROGRAM FILES
sudo cp ../dist/webwatcher /usr/bin
sudo cp ../dist/webwatchergui /usr/bin

## CONFIG
sudo mkdir -p /etc/webwatcher

## SERVICE FOR DAEMON
mkdir -p ~/.config/systemd/user
cp webwatcher.service ~/.config/systemd/user
systemctl --user daemon-reexec
systemctl --user enable webwatcher.service

# DO NOT DELETE!!!
#systemctl --user start webwatcher.service
#journalctl --user -u webwatcher.service -f

# LAUNCH ICON
sudo cp webwatchergui.desktop /usr/share/applications
## make dir if needed
#sudo mkdir -p /usr/share/icons/hicolor/256x256/apps
sudo cp webwatcher.png /usr/share/icons/hicolor/256x256/apps/
sudo gtk-update-icon-cache /usr/share/icons/hicolor
desktop-file-validate /usr/share/applications/webwatchergui.desktop







