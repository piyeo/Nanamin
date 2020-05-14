import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CK = os.environ.get("CK")
CS = os.environ.get("CS")
AT = os.environ.get("AT")
AS = os.environ.get("AS")
CKL = os.environ.get("CKL")
CSL = os.environ.get("CSL")
ATL = os.environ.get("ATL")
ASL = os.environ.get("ASL")