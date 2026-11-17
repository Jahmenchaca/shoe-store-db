import os
import psycopg
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()
database_url = os.getenv("DATABASE_URL")


with psycopg.connect(database_url) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM customer")
        print(cur.fetchone())