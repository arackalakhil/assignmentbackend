### Django REST Framework Project

This project is a Django-based RESTful API that allows users to create an account, login, and view a home page. Admins can also add apps to the user's home page and users can download these apps to earn points.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Django 2.x
- React
- Times Ago
- Form Validation
Built With
Django - The web framework used
React - The JavaScript library used for the front-end
### Installing

1. Clone the repository to your local machine
```bash
git clone git@gitlab.com:makhil029/assignmentbackend.git
Install the required packages
Copy code
pip install -r requirements.txt
Run the migrations to create the necessary tables in the database
Copy code
python manage.py makemigrations
python manage.py migrate
Run the development server
Copy code
python manage.py runserver
Usage
Go to http://localhost:8000/ to access the login page.
Register a new account by clicking on the "Sign Up" button.
Once logged in, you will be directed to the home page where you can view the apps available for download.
As an admin, you can add new apps to the home page by going to http://localhost:8000/admin/ and logging in with your admin credentials.
Users can earn points by downloading apps.





