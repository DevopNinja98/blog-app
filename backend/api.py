from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/posts')
def get_posts():
    conn = sqlite3.connect('blog.db')
    conn.execute('CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, title TEXT)')
    conn.execute('INSERT OR IGNORE INTO posts (id, title) VALUES (1, "Sample Post")')
    conn.commit()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return jsonify(posts)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)