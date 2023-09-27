# Agile Blog Module

This is a Django web application module designed with Agile principles to efficiently manage a blog. It includes user authentication, blog creation, editing, deletion, commenting on blog posts, and more. Below is a breakdown of the module's functionality and how to use it.

## Table of Contents

- [Agile Blog Module](#agile-blog-module)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Accessing the Application](#accessing-the-application)
  - [User Registration](#user-registration)
  - [User Login](#user-login)
  - [User Logout](#user-logout)
  - [Create a Blog](#create-a-blog)
  - [View Blogs](#view-blogs)
  - [View Individual Blog](#view-individual-blog)
  - [Add Comments](#add-comments)
  - [Edit Blog](#edit-blog)
  - [Delete Blog](#delete-blog)
  - [Publish Blog Post](#publish-blog-post)

## Installation<a name="installation"></a>

To use this module in your Django project, follow these Agile-inspired steps:

1. Copy the provided code into your Django project directory.

2. Ensure you have the necessary dependencies installed. You can use `pip` to install them:

   ```bash
    pip install django
    ```

    
### To create the database schema in a Django project, you need to run the following commands in your terminal or command prompt:

    ```bash
    python manage.py makemigrations
    ```

### This command is used to generate migration files based on changes made to your models.

 ``` bash
python manage.py migrate
```

## Accessing the Application
You can now access the application at [http://localhost:8000/](http://localhost:8000/).

## User Registration<a name="user-registration"></a>
- Visit the registration page at [http://localhost:8000/register/](http://localhost:8000/register/).
- Fill in the required information and submit the registration form.
- Upon successful registration, you will be automatically logged in and redirected to the home page.

## User Login<a name="user-login"></a>
- Visit the login page at [http://localhost:8000/login/](http://localhost:8000/login/).
- Enter your username and password.
- After a successful login, you will be redirected to the home page.

## User Logout<a name="user-logout"></a>
- To log out, click the "Logout" button or visit [http://localhost:8000/logout/](http://localhost:8000/logout/).
- You will receive a confirmation message and be logged out.

## Create a Blog<a name="create-a-blog"></a>
- To create a new blog post, make sure you are logged in.
- Visit the "Create Blog" page at [http://localhost:8000/create-blog/](http://localhost:8000/create-blog/).
- Fill in the blog details, including title, content, and choose whether to publish immediately or save as a draft.
- Click the "Create Blog" button to create the blog post.

## View Blogs<a name="view-blogs"></a>
- To view all the blogs, visit the home page at [http://localhost:8000/](http://localhost:8000/).
- You can use the search bar to filter blogs by title or content.

## View Individual Blog<a name="view-individual-blog"></a>
- Click on a blog title from the home page to view an individual blog post.
- You can see the blog content and any comments associated with it.

## Add Comments<a name="add-comments"></a>
- To add a comment to a blog post, make sure you are logged in.
- Visit an individual blog post.
- Scroll down to the comments section and enter your comment in the text field.
- Click the "Add Comment" button to submit your comment.

## Edit Blog<a name="edit-blog"></a>
- To edit a blog post, make sure you are logged in and the author of the blog.
- Visit the "Edit Blog" page at [http://localhost:8000/edit-blog/<blog_id>/](http://localhost:8000/edit-blog/<blog_id>/), where `<blog_id>` is the ID of the blog post you want to edit.
- Update the blog details as needed and click the "Save Changes" button.

## Delete Blog<a name="delete-blog"></a>
- To delete a blog post, make sure you are logged in and the author of the blog.
- Visit the "Delete Blog" page at [http://localhost:8000/delete-blog/<blog_id>/](http://localhost:8000/delete-blog/<blog_id>/), where `<blog_id>` is the ID of the blog post you want to delete.
- Confirm the deletion when prompted.

## Publish Blog Post<a name="publish-blog-post"></a>
- To view and publish draft blog posts, visit the "Publish Blog Post" page at [http://localhost:8000/publish-blog-post/](http://localhost:8000/publish-blog-post/).
- You can filter and search for draft posts and choose to publish them.


