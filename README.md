# unchained
A web project for college. A project that for data sharing and forum discussion boards.
Allows users to create a user account. Users can use the forums and upload and share data on the forums

Requirements:
- django-crispy-forms (used for forms)
- pillow (library used for images in python)

To run project, run the following commands in the project's directory
```
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
```
if any error occurs during migrations, run the following commands after
```
py manage.py makemigrations forum
py manage.py migrate
```
