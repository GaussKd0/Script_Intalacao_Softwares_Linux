import time
import os
from  pacotes import flatpaks
from  pacotes import snaps
from  ferramentasHacker import ferramentasHackerArch
from  ferramentasHacker import ferramentasHackerFedora
from  ferramentasHacker import ferramentasHackerDebian
from  sistemas import debian
from  sistemas import arch
from  sistemas import fedora


#pacotes
flatpaks = flatpaks.flatpaks()
snaps = snaps.snaps()
ferramentasHackerArch = ferramentasHackerArch.ferramentas()
ferramentasHackerFedora = ferramentasHackerFedora.ferramentas()
ferramentasHackerDebian = ferramentasHackerDebian.ferramentas()

#sistemas  
debian = debian.debian()
arch = arch.arch()
fedora = fedora.fedora()

#arrays de inclusao
array = []
inclusao = []
sistema = []

#funcao limpar terminal        
def Limpar():
    os.system("clear");

#funcao incluir dependencias
def IncluirDependencias(array, sistema):
    
    array += sistema

    res = input("Deseja Incluir Flatpaks? Digite S: ").strip().lower()

    if res == "s":
        array += flatpaks
        
    Limpar()   
    res = input("Deseja Incluir Snaps? Digite S: ").strip().lower()

    if res == "s":
        array+=snaps     

#loop do menu, enquanto for verdadeiro, mostra as informações para que não ocorra nenhum problema na instalação
while(True):
    res = input("Distro baseada em A(Arcsh Linux) D(Debian) F(Fedora) C(Cancelar): ").strip().lower()
    if res == "a":
        Limpar()
        res = input("Deseja Incluir Ferramentas Hackeres? se deseja incluir digite S: ").strip().lower()
        if res == "s":
            array += ferramentasHackerArch
        IncluirDependencias(array, arch)
        break

    elif res == "d":
        Limpar()
        res = input("Deseja Incluir Ferramentas Hackeres? se deseja incluir digite S: ").strip().lower()
        if res == "s":
            time.sleep(2)
            print("mestasploit sera configurado pra executar como msf")
            array += ferramentasHackerDebian
        IncluirDependencias(array, debian)
        break

    elif res == "f":
        Limpar()
        res = input("Deseja Incluir Ferramentas Hackeres? se deseja incluir digite S: ").strip().lower()
        if res == "s":
            time.sleep(2)
            print("mestasploit sera configurado pra executar como msf")
            array += ferramentasHackerFedora
        IncluirDependencias(array, fedora)
        break
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




