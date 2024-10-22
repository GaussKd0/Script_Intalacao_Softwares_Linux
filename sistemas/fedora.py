#array com os gerenciadores de pacotes snaps e flatpaks para facilitar a instalação em sistemas baseados em fedora
def fedora():
    fedora = [
    "sudo dnf check-update",
    "sudo dnf upgrade",
    "sudo dnf install snapd",
    "sudo ln -s /var/lib/snapd/snap /snap",
    "flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo"

    ]
    return fedora
