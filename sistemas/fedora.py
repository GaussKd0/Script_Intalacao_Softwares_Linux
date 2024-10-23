#lista com os gerenciadores de pacotes snaps e flatpaks para facilitar a instalação em sistemas baseados em fedora
def fedora():
    fedora = [
        "sudo dnf check-update",
        "sudo dnf upgrade",
        "sudo dnf install snapd",
        "sudo ln -s /var/lib/snapd/snap /snap",
        "flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo",
        "curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash",
        'export NVM_DIR="$HOME/.nvm"',
        '[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"',
        '[ -s "$NVM_DIR/bash_completion" ] && . "$NVM_DIR/bash_completion"',
        "nvm install 23",

    ]
    return fedora
