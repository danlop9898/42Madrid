# pip install python-dotenv
import os
from dotenv import load_dotenv  # type: ignore

print("ORACLE STATUS: Reading the Matrix...")
print()

load_dotenv()
mode = os.getenv("MATRIX_MODE", "development")
db = os.getenv("DATABASE_URL", "local_db")
api_key = os.getenv("API_KEY", None)
log_level = os.getenv("LOG_LEVEL", "DEBUG")
zion = os.getenv("ZION_ENDPOINT", "offline")

print("Configuration loaded:")
print(f"Mode: {mode}")

if mode == "production":
    print("Database: Connected to production cluster")
else:
    print("Database: Connected to local instance")

if api_key:
    print("API Access: Authenticated")
else:
    print("API Access: WARNING - Missing API key")

print(f"Log Level: {log_level}")
print(f"Zion Network: {zion}")

print("\nEnvironment security check:")

if api_key:
    print("[OK] API key loaded from environment")
else:
    print("[WARNING] Missing API key")

print("[OK] Environment variables system active")
