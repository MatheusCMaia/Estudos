import logging 

logger = logging.getLogger('SistemaDeLog')
logger.setLevel(logging.DEBUG)


file_handler = logging.FileHandler('sistema.log', mode='a', encoding='utf-8')
formato = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formato)
logger.addHandler(file_handler)

logger.debug('Debug')