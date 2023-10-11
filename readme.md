# Blog Management System

**Blog Management System** is a Django web application designed to efficiently create, manage, and publish blog posts. It includes user registration, authentication, post creation and editing, commenting, tagging, category, password change, and search functionality. Users can choose to publish posts immediately or save them as drafts and user can create company and Managers can send requests to users to join their company as writers.

## Features

- **User Registration and Authentication**: Easily sign up and securely log in.
- **Create and Edit Blog Posts**: Quickly create and edit blog posts, including the option to save drafts.
- **Delete Blog Posts**: Safely delete your own posts with a confirmation step.
- **View and Search Blog Posts**: Discover and search posts with a user-friendly interface.
- **Add Comments**: Engage with readers by adding comments to blog posts.
- **Publish or Save as Draft**: Flexibly manage post publication.
- **Bootstrap Styling**: Utilize Bootstrap for an enhanced and responsive user interface.
- **permission**: permission and page for not_allowed.
- **Category Management**: Organize Your Content Effectively.
- **Managing Join Requests (joinRequest, approveRequest, rejectRequest)**: Users can send and manage join requests to join companies. Managers have the ability to approve       or reject these requests.
- **Creating Companies (createCompany)**: Users with the necessary permissions can create companies.
- **Viewing Company Information (myCompany)**: Users can view information about the company they belong to, such as the number of employees and company-specific blog posts.
- **Requesting Writer Access to a Company (requestWriter)**: Managers can send requests to users to join their company as writers.
- **Viewing Company Writers (companyWriters)**: Users can view a list of writers in their company.
- **Password Change**: Easily  change their passwords.



## Installation and Setup

1. **Clone the Repository**:
```shell
git clone 
```


2. **Create a Virtual Environment**:
```shell
python -m venv venv
```

3. **Activate the Virtual Environment**:

- **Windows**:
  ```shell
  venv\Scripts\activate
  ```

- **Linux/macOS**:
  ```shell
  source venv/bin/activate
  ```

4. **Install Dependencies**:

  ```shell
  pip install -r requirements.txt
  ```

5. **Apply Database Migrations**:
  ```shell
  python manage.py migrate
  ```


6. **Create a Superuser Account**:

  ```shell
  python manage.py createsuperuser
  ```

 7. **Start the Development Server**:

  ```shell
  python manage.py runserver
  ```


## API Endpoints

The Blog Management System provides a RESTful API that allows  interact with the application programmatically. Below, you'll find details about the available API endpoints and their functionalities.

### Blogs

- **List Blogs**: Retrieve a list of all blogs.
  - Endpoint: `/api/blogs/`
  - Method: GET

- **Create Blog**: Create a new blog post.
  - Endpoint: `/api/blogs/`
  - Method: POST

- **Retrieve Blog**: Get details of a specific blog post.
  - Endpoint: `/api/blogs/{blog_id}/`
  - Method: GET

- **Update Blog**: Update an existing blog post.
  - Endpoint: `/api/blogs/{blog_id}/`
  - Method: PUT

- **Delete Blog**: Delete a blog post.
  - Endpoint: `/api/blogs/{blog_id}/`
  - Method: DELETE

### Companies

- **List Companies**: Retrieve a list of all companies.
  - Endpoint: `/api/companies/`
  - Method: GET

- **Create Company**: Create a new company.
  - Endpoint: `/api/companies/`
  - Method: POST

- **Retrieve Company**: Get details of a specific company.
  - Endpoint: `/api/companies/{company_id}/`
  - Method: GET

- **Update Company**: Update an existing company.
  - Endpoint: `/api/companies/{company_id}/`
  - Method: PUT

- **Delete Company**: Delete a company.
  - Endpoint: `/api/companies/{company_id}/`
  - Method: DELETE

### Categories

- **List Categories**: Retrieve a list of all categories.
  - Endpoint: `/api/categories/`
  - Method: GET

- **Create Category**: Create a new category.
  - Endpoint: `/api/categories/`
  - Method: POST

- **Retrieve Category**: Get details of a specific category.
  - Endpoint: `/api/categories/{category_id}/`
  - Method: GET

- **Update Category**: Update an existing category.
  - Endpoint: `/api/categories/{category_id}/`
  - Method: PUT

- **Delete Category**: Delete a category.
  - Endpoint: `/api/categories/{category_id}/`
  - Method: DELETE

### Tags

- **List Tags**: Retrieve a list of all tags.
  - Endpoint: `/api/tags/`
  - Method: GET

- **Create Tag**: Create a new tag.
  - Endpoint: `/api/tags/`
  - Method: POST

- **Retrieve Tag**: Get details of a specific tag.
  - Endpoint: `/api/tags/{tag_id}/`
  - Method: GET

- **Update Tag**: Update an existing tag.
  - Endpoint: `/api/tags/{tag_id}/`
  - Method: PUT

- **Delete Tag**: Delete a tag.
  - Endpoint: `/api/tags/{tag_id}/`
  - Method: DELETE


## Directory Structure

- `myApp/`: The main Django application directory.
- `templates/`: HTML templates.
- `models.py`: Data models for blog posts and comments.
- `forms.py`: Forms for registration, login, and post creation/editing.
- `views.py`: View functions for user interactions.
- `urls.py`: URL patterns and routes.

## Dependencies

- **Django**: High-level Python web framework.
- **Bootstrap**: Front-end framework for UI styling.
- **SQLite**: Default database for data storage.






