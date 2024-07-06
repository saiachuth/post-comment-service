from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import markdown2 #for RTS support
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)

# Function to validate if a user exists in the database, if it doesn't exist it creates 
def validate_user(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()
    if not user:
        cursor.execute("INSERT INTO users (username) VALUES (%s)", (username,))
        mysql.connection.commit()
    cursor.close()

# Route to create a new post
@app.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    username = data['username']
    title = data['title']
    content = data['content']
    validate_user(username)
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO posts (username, title, content) VALUES (%s, %s, %s)", (username, title, content))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Post created!'}), 201

# Route to create a new comment for a specific post mentioned by the <post_id>
@app.route('/posts/<int:post_id>/comments', methods=['POST'])
def create_comment(post_id):
    data = request.get_json()
    username = data['username']
    content = data['content']
    validate_user(username)
    html_content = markdown2.markdown(content) #RTS convrsion
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO comments (post_id, username, content) VALUES (%s, %s, %s)", (post_id, username, html_content))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Comment added!'}), 201

@app.route('/posts', methods=['GET'])
def get_posts():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT p.post_id, p.title, p.content, p.created_at, u.username FROM posts p JOIN users u ON p.username = u.username")
    posts = cursor.fetchall()
    cursor.close()
    return jsonify(posts), 200

# Route to retrieve comments for a specific post mentioned by the <post_id> tag
@app.route('/posts/<int:post_id>/comments', methods=['GET'])
def get_comments(post_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT c.comment_id, c.content, c.created_at, u.username FROM comments c JOIN users u ON c.username = u.username WHERE c.post_id = %s", (post_id,))
    comments = cursor.fetchall()
    cursor.close()
    return jsonify(comments), 200

if __name__ == '__main__':
    app.run(debug=True)
