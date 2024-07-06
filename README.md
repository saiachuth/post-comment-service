# Post-Comments Service

## Introduction
simple Post-Comments service using Flask and MySQL. It allows users to create text-based posts and comment on these posts. Each post can have multiple comments, and users are validated and stored in a MySQL database with RTS.

## Features
- **Create Posts**: Users can create new posts with a title and content.
- **Add Comments**: Users can comment on existing posts.
- **Fetch Posts and Comments**: APIs to retrieve all posts and comments for a specific post.
- **User Validation**: New users are validated and stored in the database when creating posts or comments.

## Technologies Used
- **Flask**: Python web framework for building APIs.
- **MySQL**: Relational database for storing posts, comments, and user data.
- **Markdown2**: Library for converting Markdown to HTML, used for comment formatting for the RTS implementation.

## Setup and Installation
To run this application locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/saiachuth/post-comment-service.git
   cd post-comment-service

## Setup and Installation

To run this application locally, follow these steps:

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

3. **Database Setup:**:
   Ensure MySQL is installed and running.
   Create a MySQL database and update the config.py file with your database credentials.

4. **Install Dependencies**:
   ```bash
   flask run


### API Endpoints

#### Create Post

- **Endpoint:** `POST /posts`
- **Description:** Creates a new post with a title and content. Requires a JSON payload with `username`, `title`, and `content` fields.

#### Create Comment

- **Endpoint:** `POST /posts/<post_id>/comments`
- **Description:** Adds a comment to a specific post identified by `<post_id>`. Requires a JSON payload with `username` and `content` fields.

#### Get All Posts

- **Endpoint:** `GET /posts`
- **Description:** Retrieves all posts with details including `post_id`, `title`, `content`, `created_at`, and `username`.

#### Get Comments for a Post

- **Endpoint:** `GET /posts/<post_id>/comments`
- **Description:** Retrieves all comments for a specific post identified by `<post_id>`. Returns details including `comment_id`, `content`, `created_at`, and `username`.


#### Sample Requests
- **Create Post** 
- **Request: POST http://localhost:5000/posts**
    ```json
   
   {
     "username": "john_doe",
     "title": "First Post",
     "content": "This is my first post!"
   }

- **Create Comment** 
- **Request: POST http://localhost:5000/posts/<post_id>/comments**
    ```json
   

   {
     "username": "jane_smith",
     "content": "Great post! Looking forward to more."
   }

- **Get All Post** 
- **Request: GET http://localhost:5000/posts**
    ```http
   
   http://localhost:5000/posts

- **Get All Post** 
- **Request: GET **
    ```http
   
   http://localhost:5000/posts/<post_id>/comments







