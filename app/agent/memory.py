import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parents[1] / "db" / "memory.sqlite"

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def get_memory(chat_id: str, limit: int = 10):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT role, content
        FROM memory
        WHERE chat_id = ?
        ORDER BY id DESC
        LIMIT ?
    """, (chat_id, limit))

    rows = cursor.fetchall()
    conn.close()

    # inverter para ordem cronológica
    return [{"role": r, "content": c} for r, c in reversed(rows)]


def save_message(chat_id: str, role: str, content: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO memory (chat_id, role, content)
        VALUES (?, ?, ?)
    """, (chat_id, role, content))

    conn.commit()
    conn.close()
