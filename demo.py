from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

logging.info("welcome to logging")

try:
    a=20/0
except Exception as e:
    raise USvisaException(e,sys)    