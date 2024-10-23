# Ferramentas hacker para distros baseadas em Debian
def ferramentas():
    ferramentas = [
        "sudo apt install hydra",
        "sudo apt install nmap",
        "sudo apt install john",
        "sudo apt install curl gpg apt-transport-https",
        "sudo apt install ruby-rubygems",
        "sudo apt install ruby-dev",
        "sudo apt install libpq-dev",
        "sudo apt install libpcap-dev",
        "sudo apt install git build-essential libssl-dev libreadline-dev zlib1g-dev libsqlite3-dev",
        "git clone https://github.com/rapid7/metasploit-framework.git",
        "cd metasploit-framework",
        "sudo gem install bundler",
        "sudo bundle install",
        "cd ~/metasploit-framework",
        "sudo ln -s $(pwd)/msfconsole /usr/local/bin/msf",
        "sudo apt install openssh-server",
        "sudo systemctl start ssh",
        "sudo systemctl enable ssh",
        "sudo apt install aircrack-ng",
        "sudo apt-get install wireshark",
        "sudo usermod -aG wireshark $USER",
        "sudo apt-get install netcat",
        "sudo apt install git python3 python3-pip",
        "git clone https://github.com/trustedsec/social-engineer-toolkit.git",
        "cd social-engineer-toolkit",
        "pip3 install -r requirements.txt",
        "sudo python3 setup.py",

    ]
    return ferramentas
