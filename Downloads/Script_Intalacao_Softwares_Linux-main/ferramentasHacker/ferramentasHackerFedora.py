#ferramentas hacker para distros baseadas em fedora
def ferramentas():
    ferramantas = [
        "sudo dnf install hydra",
        "sudo dnf install nmap",
        "sudo dnf install john",
        "sudo dnf install openssh-server openssh-clients",
        "sudo systemctl start sshd",
        "sudo systemctl enable sshd",
        "sudo dnf install aircrack-ng",
        "sudo dnf install wireshark",
        "sudo dnf install postgresql-devel",
        "sudo dnf install libpcap-devel",
        "sudo dnf install gcc-c++ make",
        "sudo dnf install git curl gcc make ruby-devel",
        "git clone https://github.com/rapid7/metasploit-framework.git",
        "gem install bundler",
        "bundle install",
        #configura o mestasploit pra executar como msf
        "sudo ln -s ~/metasploit-framework/msfconsole /usr/local/bin/msf",

    ]
    return ferramantas
