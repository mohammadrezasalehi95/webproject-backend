# webproject-backend
must be installed before running
```bash
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
pip install python-decouple
pip install coverage
```
for seeing coverage of test run following commands:
```bash
coverage run --source='.' manage.py test
coverage html
coverage report
```
although you must create `.env` file for cofiguring some variable is for your own 
like google security, email,email password and so

**change you must apply to settings.py**
```
*ALLOWED_HOST* you must add your server hostname (or any ip you want to run this project over it)
```
