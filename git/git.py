import os
def git():
    user = input("Digite seu nome git: ")
    os.system("cls")

    email = input("Digite seu email: ")
    git=[
        'git config --global user.name "'+user+'",
        'git config --global user.email "'+email+'",
        'git config --global color.ui auto'
    ]
    return git
