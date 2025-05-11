from app import get_db_connection

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Tạo bảng admin
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
    ''')

    # Tạo bảng posts
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(150) NOT NULL,
        content TEXT NOT NULL,
        image_url VARCHAR(300)
    )
    ''')
    # cursor.execute('''
    # INSERT INTO user VALUES (1, 'admin','bXVhX3RodV9uYW1fYXlfZW1fcm9pX2Rp')
    # ''')

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    print("Initializing database....................................................")
    init_db()
