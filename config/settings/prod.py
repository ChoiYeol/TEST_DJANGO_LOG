from .base import *
from dotenv import load_dotenv

############## load dot env ##############
load_dotenv(verbose=True) #.env가 누락일경우 경고메시지 출력하는옵션

DB_NAME = os.environ.get("DB_NAME_PROD")
##########################################