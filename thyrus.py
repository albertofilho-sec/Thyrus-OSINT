"""
Thyrus OSINT & Attack Surface Framework

Uso exclusivo para:
- auditorias autorizadas
- validação defensiva
- análise passiva de exposição pública
- atividades de Blue Team e ASM

O uso indevido é de responsabilidade do operador.
"""

import os
import subprocess
import shutil
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

RESULT_DIR = "resultados"

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def create_results_dir():
    if not os.path.exists(RESULT_DIR):
        os.makedirs(RESULT_DIR)

def timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def safe_filename(name):
    return "".join(c for c in name if c.isalnum() or c in ('-', '_', '.'))

def check_tool(tool_name):
    return shutil.which(tool_name) is not None

def header():

    clear()

    logo = f"""
{Fore.CYAN}  ████████╗██╗  ██╗██╗   ██╗██████╗  ██╗   ██╗███████╗
{Fore.CYAN}  ╚══██╔══╝██║  ██║╚██╗ ██╔╝██╔══██╗ ██║   ██║██╔════╝
{Fore.CYAN}     ██║   ███████║ ╚████╔╝ ██████╔╝ ██║   ██║███████╗
{Fore.CYAN}     ██║   ██╔══██║  ╚██╔╝  ██╔══██╗ ██║   ██║╚════██║
{Fore.CYAN}     ██║   ██║  ██║   ██║   ██║  ██║ ╚██████╔╝███████║
{Fore.CYAN}     ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝  ╚═════╝ ╚══════╝

{Fore.GREEN} [ Thyrus OSINT & Attack Surface Framework ]
{Fore.WHITE} [ Multi-Distro Ready • Desenvolvido por: Alberto Filho ]
    """

    print(logo)

def menu():

    print(f"{Style.BRIGHT}{Fore.CYAN}--- IDENTIDADES & PRESENÇA PÚBLICA ---")
    print(f"{Fore.YELLOW}[ 1 ] {Fore.WHITE}Sherlock {Style.DIM}- Análise de presença pública")
    print(f"{Fore.YELLOW}[ 2 ] {Fore.WHITE}Maigret {Style.DIM}- Relatórios estruturados de perfis")

    print(f"\n{Style.BRIGHT}{Fore.CYAN}--- IDENTIDADES & EXPOSIÇÃO PASSIVA ---")
    print(f"{Fore.YELLOW}[ 3 ] {Fore.WHITE}Holehe {Style.DIM}- Validação passiva de identidades")
    print(f"{Fore.YELLOW}[ 4 ] {Fore.WHITE}SocialScan {Style.DIM}- Verificação pública de usernames e e-mails")

    print(f"\n{Style.BRIGHT}{Fore.CYAN}--- INFRAESTRUTURA & ATTACK SURFACE ---")
    print(f"{Fore.YELLOW}[ 5 ] {Fore.WHITE}theHarvester {Style.DIM}- Enumeração passiva de ativos públicos")
    print(f"{Fore.YELLOW}[ 6 ] {Fore.WHITE}Sublist3r {Style.DIM}- Análise passiva de subdomínios")
    print(f"{Fore.YELLOW}[ 7 ] {Fore.WHITE}Nmap (Defensivo) {Style.DIM}- Auditoria rápida de conformidade")

    print(f"\n{Style.BRIGHT}{Fore.CYAN}--- DOCUMENTOS & METADADOS ---")
    print(f"{Fore.YELLOW}[ 8 ] {Fore.WHITE}ExifTool {Style.DIM}- Extração e sanitização de metadados")

    print(f"\n{Fore.RED}[ 0 ] {Fore.WHITE}Sair")

def execute_command(command, output_file=None):

    try:

        if output_file:

            with open(output_file, "w") as file:

                subprocess.run(
                    command,
                    stdout=file,
                    stderr=subprocess.STDOUT,
                    text=True
                )

        else:

            subprocess.run(command)

    except Exception as e:

        print(f"{Fore.RED}[!] Erro durante execução: {e}")

def main():

    create_results_dir()

    while True:

        header()
        menu()

        opt = input(f"\n{Fore.GREEN}Thyrus > {Fore.WHITE}Selecione uma opção: ")

        if opt == '0':
            print(f"{Style.BRIGHT}{Fore.CYAN}Encerrando o framework...")
            break

        valid_opts = [str(i) for i in range(1, 9)]

        if opt not in valid_opts:
            print(f"{Fore.RED}[!] Opção inválida.")
            input(f"\n{Fore.YELLOW}Pressione Enter para continuar...")
            continue

        alvo = input(f"{Fore.GREEN}Thyrus > {Fore.WHITE}Insira o alvo correspondente: ")

        alvo_safe = safe_filename(alvo)
        ts = timestamp()

        if opt == '1':

            if not check_tool("sherlock"):
                print(f"{Fore.RED}[!] Sherlock não encontrado.")
                continue

            execute_command([
                "sherlock",
                alvo,
                "--folder",
                RESULT_DIR
            ])

        elif opt == '2':

            if not check_tool("maigret"):
                print(f"{Fore.RED}[!] Maigret não encontrado.")
                continue

            execute_command([
                "maigret",
                alvo,
                "--folder",
                RESULT_DIR
            ])

        elif opt == '3':

            if not check_tool("holehe"):
                print(f"{Fore.RED}[!] Holehe não encontrado.")
                continue

            execute_command([
                "holehe",
                alvo
            ])

        elif opt == '4':

            if not check_tool("socialscan"):
                print(f"{Fore.RED}[!] SocialScan não encontrado.")
                continue

            execute_command([
                "socialscan",
                alvo
            ])

        elif opt == '5':

            if not check_tool("theHarvester"):
                print(f"{Fore.RED}[!] theHarvester não encontrado.")
                continue

            output = f"{RESULT_DIR}/{alvo_safe}_{ts}.html"

            execute_command([
                "theHarvester",
                "-d",
                alvo,
                "-l",
                "500",
                "-b",
                "google",
                "-f",
                output
            ])

        elif opt == '6':

            if not check_tool("sublist3r"):
                print(f"{Fore.RED}[!] Sublist3r não encontrado.")
                continue

            output = f"{RESULT_DIR}/{alvo_safe}_subdominios_{ts}.txt"

            execute_command([
                "sublist3r",
                "-d",
                alvo,
                "-o",
                output
            ])

        elif opt == '7':

            if not check_tool("nmap"):
                print(f"{Fore.RED}[!] Nmap não encontrado.")
                continue

            output = f"{RESULT_DIR}/{alvo_safe}_nmap_{ts}.txt"

            execute_command(
                [
                    "nmap",
                    "-sV",
                    "-Pn",
                    "-F",
                    alvo
                ],
                output
            )

            print(f"{Fore.GREEN}[+] Resultado salvo em: {output}")

        elif opt == '8':

            if not check_tool("exiftool"):
                print(f"{Fore.RED}[!] ExifTool não encontrado.")
                continue

            execute_command([
                "exiftool",
                alvo
            ])

        input(f"\n{Fore.YELLOW}Pressione Enter para retornar ao menu principal...")

if __name__ == '__main__':
    main()

