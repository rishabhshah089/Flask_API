import sqlite3
from flask import g

DATABASE="audio.db"

def executeQuery(query):
    try:
        cur,conn = get_db_conn()
        new_song = cur.execute(query)
        comm = conn.commit()
        conn.close()
        return 1
    except:
        return 0


def getQueryDate(query):
    try:
        cur,conn = get_db_conn()
        cur.execute(query)
        rows = cur.fetchall()
        conn.close()
        return rows
    except:
        return 0


def get_db_conn():
    db = getattr(g, '_database', None)
    if db is None:
        conn = g._database = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    return cur,conn

