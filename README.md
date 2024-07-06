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

