"""
Autor: Cassio Maciel Lemos
E-mail: cassio.lemos@petrobras.com.br

##############################################################################
                            USO

##############################################################################
                            MOTIVAÇÃO

Esse programa foi feito para automaticamente instalar as dependências,
baixar os códigos atualizados do github, e fazer deixar o programa funcional.
"""
import subprocess

try:
    with open('requirements.txt', 'r') as arquivo:
        requisitos = arquivo.read().splitlines()

    subprocess.run(['pip', 'install'] + requisitos, check=True)
    print("Pacotes instalados com sucesso.")
except subprocess.CalledProcessError as e:
    print(f"Erro ao instalar pacotes: {e}")


#pip.main(["install", "-r", "requirements.txt"])
