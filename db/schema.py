from .connection import conn

def main():

    conn.execute('''
        CREATE TABLE IF NOT EXISTS User (
        id TEXT PRIMARY KEY, 
        name TEXT NOT NULL, 
        email TEXT NOT NULL UNIQUE, 
        password TEXT NOT NULL, 
        role TEXT NOT NULL, 
        thumb TEXT, 
        content TEXT, 
        date TEXT NOT NULL
        );
    ''')
    
    conn.execute('''
        CREATE TABLE IF NOT EXISTS Post (
        id TEXT PRIMARY KEY, 
        title TEXT NOT NULL,
        content TEXT,
        categories TEXT NOT NULL,
        thumb TEXT,
        date TEXT NOT NULL,
        videos TEXT,
        author TEXT NOT NULL,
        expiration TEXT
        );
    ''')
    
    conn.execute('''
        CREATE TABLE IF NOT EXISTS Category (
        id TEXT PRIMARY KEY, 
        title TEXT NOT NULL,
        thumb TEXT NOT NULL,
        date TEXT NOT NULL
        );
    ''')
    
    conn.execute('''
        CREATE TABLE IF NOT EXISTS Page (
        id TEXT PRIMARY KEY, 
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        thumb TEXT,
        date TEXT NOT NULL
        );
    ''')
    
    conn.execute('''
        CREATE TABLE IF NOT EXISTS Setting (
        id TEXT PRIMARY KEY, 
        title TEXT NOT NULL,
        description TEXT,
        dashboard INTEGER NOT NULL,
        frontend INTEGER NOT NULL,
        category INTEGER NOT NULL,
        playlist INTEGER NOT NULL,
        thumb TEXT,
        date TEXT NOT NULL
        );
    ''')

main()