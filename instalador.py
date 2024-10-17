import time
import os

array = []
inclusao = []
sistema = []

#funcao incluir dependencias
def IncluirDependencias(array, sistema):
    
    array += sistema;

    res = input("Deseja Incluir Flatpaks? Digite S: ").strip().lower()

    if res == "s":
        array += flatpaks;
        
    Limpar()   
    res = input("Deseja Incluir Snaps? Digite S: ").strip().lower()

    if res == "s":
        array+=snaps
         
#funcao limpar terminal        
def Limpar():
    os.system("clear");


#flatpaks
flatpaks = [
    "flatpak install flathub com.spotify.Client",
    "flatpak install flathub com.brave.Browser",
    "flatpak install flathub com.rtosta.zapzap",
    "flatpak install flathub dev.vencord.Vesktop",
    "flatpak install flathub com.brave.Browser",
    "flatpak install flathub com.spotify.Client",
    "flatpak install flathub net.davidotek.pupgui2",
    "flatpak install flathub com.valvesoftware.Steam"
]

#snaps
snaps = [
    "sudo snap install code --classic",
    "sudo snap install insomnia",
    "sudo snap install obs-studio",
    "sudo snap install arduino",
    "sudo snap install vlc",
    "sudo snap install rider --classic",
    "sudo snap install notion-snap-reborn",
    "sudo snap install obs-studio",
    "sudo snap install notion-snap-reborn",
    "sudo snap install ngrok",
    "sudo snap install arduino",
    "sudo snap install vlc",
    "sudo snap install rider --classic",
    "sudo snap install insomnia"
    
]

#ferramentas pentest, hacking, seguranca(arch linux)
ferramantasHackerA = [
    "sudo pacman -S hydra",
    "sudo pacman -S nmap",
    "sudo pacman -S john",
    "sudo pacman -S metasploit",
    "yay -S burpsuite",
    "yay -S sqlmap",
    "sudo pacman -S openssh",
    "sudo pacman -S aircrack-ng",
    "yay -S social-engineer-toolkit",
    "sudo pacman -S wireshark-qt",
    "sudo pacman -S gnu-netcat",
    "yay -S beef",
    "yay -S fern-wifi-cracker"

]



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
  
]


#array com os gerenciadores de pacotes snaps e flatpaks para facilitar a instalação em sistemas baseados em arch
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

#array com os gerenciadores de pacotes snaps e flatpaks para facilitar a instalação em sistemas baseados em fedora
fedora = [
  "sudo dnf check-update",
  "sudo dnf upgrade",
  "sudo dnf install snapd",
  "sudo ln -s /var/lib/snapd/snap /snap",
  "flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo"

]

#loop do menu, enquanto for verdadeiro, mostra as informações para que não ocorra nenhum problema na instalação
while(True):
    res = input("Distro baseada em A(Arcsh Linux) D(Debian) F(Fedora) C(Cancelar): ").strip().lower()
    if res == "a":
        IncluirDependencias(array, arch)
        Limpar()
        res = input("Deseja Incluir Ferramentas Hackeres? se deseja incluir digite S: ").strip().lower()
        if res == "s":
            array += ferramantasHackerA;
        break

    elif res == "d":
        IncluirDependencias(array, debian)
        break

    elif res == "f":
        IncluirDependencias(array, fedora)
        break;
    elif res == "c":
        break

    else:
        print("Comando digitado incorreto!!")

#loop para escrever os comandos no terminal
for comando in array:
    print(comando)
    time.sleep(1)
    Limpar()
    os.system(comando)


