#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import time
import itertools
import random
import os

# Cores ANSI
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
BOLD = "\033[1m"

BANNER = f"""{GREEN}{BOLD}
 ###     #######   ######    #####    ####   #######   ##  ##           #######   ##  ##  ######   #####      ####   #######   ######
 ###       ###     ######   ### ##   ######    ###     ### ##            ###       ####    ######   ###      ######    ###     ######
 #####     ###     # ## #   ###      ##  ##    ###     ######            #####      ##     ##  ##   ###      ##  ##    ###     # ## #
 ##  ##    ###       ##     ###      ##  ##    ###     ######            ###       ####    #####    ###      ##  ##    ###       ##
 ##  ##    ###       ##     ### ##   ######    ###     ## ###            ###      ######   ###      ### ##   ######    ###       ##
 #####   #######    ####     #####    ####   #######   ##  ##           #######   ##  ##  #####    #######    ####   #######    ####
{RESET}"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, color=RESET, delay=0.01, end="\n"):
    for ch in text:
        print(color + ch + RESET, end="", flush=True)
        time.sleep(delay)
    print(end, end="")

def spinner(label, color=CYAN, duration=2):
    spin = itertools.cycle("|/-\\")
    start = time.time()
    while time.time() - start < duration:
        sys.stdout.write(f"\r{color}{label} {next(spin)}{RESET}")
        sys.stdout.flush()
        time.sleep(0.07)
    sys.stdout.write("\r" + " " * (len(label) + 5) + "\r")

def progress_bar(label, color=YELLOW, total=40, min_delay=0.005, max_delay=0.03):
    sys.stdout.write(f"{color}{label} [{RESET}")
    sys.stdout.flush()
    for _ in range(total):
        time.sleep(random.uniform(min_delay, max_delay))
        sys.stdout.write(f"{GREEN}#{RESET}")
        sys.stdout.flush()
    sys.stdout.write(f"{color}] 100%{RESET}\n")

def chaotic_logs(lines=12):
    chars = "ABCDEF0123456789!@#$%&*"
    colors = [GREEN, CYAN, MAGENTA, YELLOW]
    for _ in range(lines):
        # 20% de chance de imprimir erro falso em vermelho
        if random.random() < 0.2:
            addr = hex(random.randint(0x100000, 0xFFFFFF))
            err = random.choice([
                "SegFault", "Memory access violation",
                "Critical buffer overflow", "Illegal opcode",
                "Kernel panic", "Heap corruption"
            ])
            print(f"{RED}[{time.strftime('%H:%M:%S')}] ERROR: {err} at {addr}{RESET}")
        else:
            log = "".join(random.choice(chars) for _ in range(random.randint(40, 80)))
            c = random.choice(colors)
            print(f"{c}[{time.strftime('%H:%M:%S')}] {log}{RESET}")
        time.sleep(random.uniform(0.03, 0.12))

def main():
    slow_print("Inicializando exploit engine...", CYAN, delay=0.02)
    time.sleep(5)

    clear_screen()
    print(BANNER)
    time.sleep(2)

    steps = [
        "Carregando módulos de injeção",
        "Bypass de firewalls",
        "Compilando chaves RSA",
        "Injetando payload",
        "Construindo backdoor persistente",
        "Validando hashes SHA256",
        "Gerando wallet temporária",
        "Escalando privilégios",
        "Estabelecendo túnel criptografado",
        "Finalizando ataque"
    ]

    for step in steps:
        spinner(step, color=random.choice([GREEN, CYAN, MAGENTA]), duration=random.uniform(1.5, 2.5))
        print(f"{GREEN}{step}... OK{RESET}")
        if random.random() < 0.5:
            chaotic_logs(random.randint(5, 10))
            time.sleep(0.5)
            clear_screen()
            print(BANNER)

    print("\n")
    progress_bar("Extraindo blocos de transação", color=YELLOW)
    progress_bar("Forjando credenciais seguras", color=CYAN, total=55)
    progress_bar("Sincronizando ledger fake", color=MAGENTA, total=30)

    chaotic_logs(15)
    clear_screen()
    print(BANNER)

    slow_print("\nConta gerada com sucesso:", GREEN, delay=0.01)
    slow_print("   usuário: admin", CYAN, delay=0.01)
    slow_print("   senha:   admin123", CYAN, delay=0.01)
    slow_print("   site:    https://renda-extra-on.github.io/Cashing/bitcoin.html", CYAN, delay=0.01)

    slow_print("\nProcesso concluído.", MAGENTA, delay=0.01)

if __name__ == "__main__":
    main()
