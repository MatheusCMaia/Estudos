import logging 


logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", encoding="utf-8",filename="monitor.log",filemode="a")

logging.info("Programa iniciado")
logging.warning("Mensagem de aviso")
logging.error("Esta é uma mensagem de erro")

