from fastapi import FastAPI
from pydantic import BaseModel
import os
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI(title="Simple FastAPI + PostgreSQL")

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://appuser:secretpass@db:5432/appdb")

class Health(BaseModel):
    status: str
    database: str

@app.get("/")
def root():
    return {"message": "Hello from FastAPI + PostgreSQL on Proxmox LXC!"}

@app.get("/health", response_model=Health)
def health():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        conn.close()
        db_status = "ok"
    except Exception as e:
        db_status = f"error: {str(e)}"
    return {"status": "ok", "database": db_status}

@app.get("/items")
def get_items():
    try:
        conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
        cur = conn.cursor()
        cur.execute("SELECT id, name FROM items ORDER BY id")
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return {"items": rows}
    except Exception as e:
        return {"error": str(e)}
