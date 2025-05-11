from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

import os
import base64
import hashlib
app = Flask(__name__)
app.secret_key = 'Mat_em_roi'  # Dùng để bảo vệ session

def get_db_connection():
    conn = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST', 'db'),
        user=os.getenv('MYSQL_USER', 'admin'),
        password=os.getenv('MYSQL_PASSWORD', 'admin'),
        database=os.getenv('MYSQL_DB', 'blog_db')
    )
    return conn

def check_password(stored_password_base64, provided_password):
    hashed_password = provided_password.encode()
    encoded_password = base64.b64encode(hashed_password).decode('utf-8')
    # So sánh mật khẩu đã mã hóa với mật khẩu đã lưu trong cơ sở dữ liệu
    return stored_password_base64 == encoded_password



@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Truy vấn tất cả bài viết để hiển thị
    cursor.execute("SELECT id, title, content, image_url FROM posts")
    posts = cursor.fetchall()
    conn.close()

    return render_template('index.html', posts=posts)

@app.route('/post/<id>')
def post(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT title, content, image_url FROM posts WHERE id = " + str(id))
    post = cursor.fetchone()
    conn.close()
    if post is None:
        return "Post not found", 404
    return render_template('post.html', post=post)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user WHERE username = %s", (username,))
        admin = cursor.fetchone()
        conn.close()

        if admin and check_password(admin['password'], password):
            session['admin'] = True
            return redirect(url_for('index'))
        else:
            return "Invalid credentials", 401

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('index'))

@app.route('/admin', methods=['GET', 'POST'])
def admin_panel():
    if 'admin' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        image_url = request.form['image_url']

        if image_url:
            import requests
            try:
                response = requests.get(image_url)
                if response.status_code == 200:
                    content += f"\n\n[Image from: {image_url}]"
                else:
                    return "Failed to fetch image", 400
            except Exception as e:
                return f"Error occurred: {str(e)}", 500 

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO posts (title, content, image_url) VALUES (%s, %s, %s)",
                       (title, content, image_url))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    return render_template('admin_panel.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
