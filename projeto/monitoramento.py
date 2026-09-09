import argparse
import subprocess
import logging

logging.basicConfig(level=logging.INFO,filename="monitoramento.log",filemode="a",encoding="utf-8",format="%(asctime)s - %(levelname)s - %(message)s")

parser = argparse.ArgumentParser(description="Programa simples de monitoramento")


parser.add_argument("--host", required=True, help="Endereço do host que será testado")


parser.add_argument("--tentativas", type=int, default=4, help="Quantidade de tentativas de ping")

args = parser.parse_args()


logging.info(f"Monitoramento iniciado para {args.host} com {args.tentativas} tentativa(s)")


resultado = subprocess.run(["ping", "-n", str(args.tentativas), args.host], capture_output=True, text=True)


if resultado.returncode == 0:
    print("Host Acessível!")
    logging.info(f"Host {args.host} acessível")
else:
    print("Host inacessível!")
    logging.warning(f"Host {args.host} inacessível")


print(resultado.stdout)