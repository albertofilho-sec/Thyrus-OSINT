#!/bin/bash

# -------------------------------------------------------------------------
# Thyrus OSINT & Attack Surface Framework
# Desenvolvedor: Alberto Filho
# Versão: 2.7
# -------------------------------------------------------------------------

set -e

clear

echo -e "\e[1;36m[ Thyrus Installer ] Provisionando ambiente...\e[0m"

if ! command -v python3 &> /dev/null; then
    echo -e "\e[1;31m[-] Python3 não encontrado no sistema.\e[0m"
    exit 1
fi

if command -v dnf &> /dev/null; then
    PKG_MGR="sudo dnf install -y"
    DEPS="python3-pip git perl-Image-ExifTool nmap"

elif command -v apt &> /dev/null; then
    PKG_MGR="sudo apt install -y"

    if [ -d "/data/data/com.termux" ]; then
        PKG_MGR="apt install -y"
    fi

    DEPS="python3-pip python3-venv git exiftool nmap"

elif command -v pacman &> /dev/null; then
    PKG_MGR="sudo pacman -S --noconfirm"
    DEPS="python-pip git perl-image-exiftool nmap"

else
    echo -e "\e[1;31m[-] Gerenciador de pacotes não suportado.\e[0m"
    exit 1
fi

echo -e "\e[1;32m[*] Instalando dependências do sistema...\e[0m"
$PKG_MGR $DEPS

if [ ! -d ".venv" ]; then
    echo -e "\e[1;32m[*] Criando ambiente virtual Python...\e[0m"
    python3 -m venv .venv
fi

source .venv/bin/activate

echo -e "\e[1;32m[*] Atualizando pip...\e[0m"
pip install --upgrade pip

echo -e "\e[1;32m[*] Instalando dependências Python...\e[0m"
pip install -r requirements.txt

mkdir -p resultados

echo -e "\e[1;32m[+] Ambiente provisionado com sucesso!\e[0m"
echo -e "\e[1;36m[+] Execute: source .venv/bin/activate && python3 thyrus.py\e[0m"
