from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

URL = os.getenv("URL")
KEY = os.getenv("KEY")

supabase: Client = create_client(URL, KEY)


response = (
  supabase.table("posts")
  .select("*")
  .execute()
)

for data in response.data:
  print("----------------------------")
  for col, data in data.copy().items():
    print(col, data)
