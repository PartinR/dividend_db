import os
from supabase import create_client, Client

url: str = os.environ.get("https://egeilyeivfjqylffekal.supabase.co")
key: str = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVnZWlseWVpdmZqcXlsZmZla2FsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjA0NjA3NDMsImV4cCI6MjA3NjAzNjc0M30.WjeBmbIHE77k7djZbIy_cVpzaj1kQXzYQDtJSxNNHZg")
supabase: Client = create_client(url, key)