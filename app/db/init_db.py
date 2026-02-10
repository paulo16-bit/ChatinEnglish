import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "memory.sqlite"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat_id TEXT NOT NULL,
        role TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
    """)

    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_memory_chat_id
    ON memory(chat_id);
    """)

    conn.commit()
    conn.close()

    print(f"Banco criado em: {DB_PATH}")

if __name__ == "__main__":
    init_db()
