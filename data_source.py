import time
# data_source.py
import pyodbc

def fetch_data():
    
    conn_str = (
        "DRIVER={SQL Server};"
        "SERVER=LAPTOP-S8HL2J8D\\SQLEXPRESS;"
        "DATABASE=webCachingserver;"
        "Trusted_Connection=yes;"
    )

    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        print("Connected successfully!")
        time.sleep(2)
        cursor.execute("SELECT * FROM emp")
        data = [dict(zip([column[0] for column in cursor.description], row)) for row in cursor.fetchall()]
        
        return {"message": "Connected successfully!", "rows": data}

    except Exception as e:
        print("Connection failed:", e)
        return {"error": str(e)}



