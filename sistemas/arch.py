#array com os gerenciadores de pacotes snaps e flatpaks para facilitar a instalação em sistemas baseados em arch
def arch():
    arch = [
        "sudo pacman -Syu",
        "git clone https://aur.archlinux.org/snapd.git",
        "cd snapd",
        "makepkg -si",
        "sudo systemctl enable --now snapd.socket",
        "sudo systemctl enable --now snapd.apparmor.service",
        "sudo ln -s /var/lib/snapd/snap /snap",
        "sudo pacman -S flatpak",
    ]
    return arch