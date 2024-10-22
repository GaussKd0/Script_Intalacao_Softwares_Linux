from ferramentasHacker import ferramentasHackerYay

def ferramentas():
    
    ferramantas = [
        "sudo pacman -S hydra",
        "sudo pacman -S nmap",
        "sudo pacman -S john",
        "sudo pacman -S metasploit",
        "sudo pacman -S openssh",
        "sudo pacman -S aircrack-ng",
        "sudo pacman -S wireshark-qt",
        "sudo pacman -S gnu-netcat",
        "bundle install",

    ]
    ferramantas += ferramentasHackerYay.yay() 
    return ferramantas