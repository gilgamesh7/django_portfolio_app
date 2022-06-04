# django_portfolio_app

# Link to Real Python Course
[Real Python Django Portfolio Project](https://realpython.com/courses/django-portfolio-project/)  

# Set up for development
1. Install & activate venv (python3 -m venv venv --upgrade-deps)
2. Generate project : ./venv/bin/django-admin startproject portfolio .  
3. Generate application : python3 manage.py startapp projects

# To migrate after changing models
1. python manage.py makemigrations
2. python manage.py migrate

# Run server
python3 manage.py runserver  

