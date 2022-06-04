# django_portfolio_app

# Link to Real Python Courses
- [Real Python Django Portfolio Project](https://realpython.com/courses/django-portfolio-project/)  
- [Get Started With Django Part 1: Build a Portfolio App](https://realpython.com/get-started-with-django-1/)
# Set up for development
1. Install & activate venv (python3 -m venv venv --upgrade-deps)
2. Generate project : ./venv/bin/django-admin startproject portfolio .  
3. Generate application : python3 manage.py startapp projects

# To migrate after changing models
1. python manage.py makemigrations
2. python manage.py migrate

# Run shell & add to database
1. python3 manage.py shell
2. from projects.models import Project
3. p1 = Project(title="My First Project", description="Testing first project", technology="django", image="daily.png")
4. p1.save()
5. results = Project.objects.all()
6. p=results[0].title

# Run server
python3 manage.py runserver  

