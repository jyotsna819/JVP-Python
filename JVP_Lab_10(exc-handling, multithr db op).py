import sqlite3
import threading
import time

# Exception Handling + Database Operations
def insert_into_db(name, age):
    try:
        conn = sqlite3.connect('people.db')
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS person (name TEXT, age INTEGER)')
        cursor.execute('INSERT INTO person (name, age) VALUES (?, ?)', (name, age))
        conn.commit()
        print(f"[{threading.current_thread().name}] Inserted: {name}, {age}")
    except Exception as e:
        print(f"[{threading.current_thread().name}] Error: {e}")
    finally:
        conn.close()

# Multithreaded Execution
def thread_function(name, age):
    time.sleep(1)
    insert_into_db(name, age)

if __name__ == "__main__":
    data = [("Alice", 25), ("Bob", 30), ("Charlie", 22)]
    threads = []

    for entry in data:
        t = threading.Thread(target=thread_function, args=(entry[0], entry[1]))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("All threads completed.")
