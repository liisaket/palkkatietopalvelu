import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

DATABASE_URL = os.getenv("DATABASE_URL")
TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL")
ENV = os.getenv("FLASK_ENV")

if DATABASE_URL is None:
    raise RuntimeError("Database URI is not defined with the DATABASE_URL environment variable.")
