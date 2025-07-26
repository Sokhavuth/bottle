import os
import libsql

TURSO_DATABASE_URL = os.environ.get("TURSO_DATABASE_URL")
TURSO_AUTH_TOKEN = os.environ.get("TURSO_AUTH_TOKEN")

conn = libsql.connect("local.db", sync_url=TURSO_DATABASE_URL, auth_token=TURSO_AUTH_TOKEN)
conn.sync()