def debian():
    debian = [
        "sudo apt update",
        "sudo apt install -y snapd",
        "sudo snap install hello-world",
        "sudo apt install -y flatpak",
        "sudo add-apt-repository -y ppa:flatpak/stable",
        "sudo apt update",
        "sudo apt install -y flatpak",
        "sudo apt install -y gnome-software-plugin-flatpak",
    ]
    return debian