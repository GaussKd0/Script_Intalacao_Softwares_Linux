def debian():
    #array com os gerenciadores de pacotes snaps e flatpaks para facilitar a instalação em sistemas baseados em debian
    debian = [
        "sudo apt update",
        "sudo apt install -y snapd",
        "sudo snap install hello-world",
        "sudo apt install -y flatpak",
        "sudo add-apt-repository -y ppa:flatpak/stable",
        "sudo apt update",
        "sudo apt install -y flatpak",
        "sudo apt install -y gnome-software-plugin-flatpak",
        "sudo apt install nodejs npm"
    ]
    return debian