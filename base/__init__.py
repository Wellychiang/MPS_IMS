import logging
from config.url import ImsUrl


log_path = 'log/log.log'
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')

console_log = logging.StreamHandler()  # sys.stdout
logger.addHandler(console_log)

file_handler = logging.FileHandler(log_path)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

log = lambda x: logger.info(str(x).encode('utf-8', 'replace').decode('cp950', 'ignore'))

ims =  ImsUrl()