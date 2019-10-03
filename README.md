# unchained
A web project for college. A project that for data sharing and forum discussion boards.
Allows users to create a user account. Users can use the forums and upload and share data on the forums

Further project development moved to [CyrilSL's fork](https://github.com/CyrilSL/unchained)

Requirements:
- django-crispy-forms (used for forms)
- pillow (library used for images in python)

To run project, run the following commands in the project's directory to create the database
```
py manage.py makemigrations forum
py manage.py makemigrations files
py manage.py makemigrations users
py manage.py migrate
```
Use the following command to run the server
```
py manage.py runserver
```
To create an admin account, create a regular account using the website's register page. Open the shell using the following command
```
py manage.py shell
```
and run the following command on the shell replacing the username
```
from django.contrib.auth.models import User
user = User.objects.get(username="yourusername")
user.is_staff = True
user.is_admin = True
user.is_superuser = True
user.save()
```
If there are errors in the migrations, run the migration and migrate command for each individual app in the project
```
py manage.py makemigrations forum
py manage.py migrate forum
py manage.py makemigrations files
py manage.py migrate files
py manage.py makemigrations users
py manage.py migrate users
```
