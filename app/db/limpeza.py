import sqlite3

conn = sqlite3.connect("app/db/memory.sqlite")
cursor = conn.cursor()

cursor.execute("DELETE FROM memory")
conn.commit()

conn.close()

print("🧹 Memória limpa")
