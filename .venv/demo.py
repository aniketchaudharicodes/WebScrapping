from dotenv import load_dotenv,  find_dotenv
import os

load_dotenv(find_dotenv())

url: str = os.getenv('CRYPTO_URL')

print(url)