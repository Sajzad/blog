# blog

### How do I get set up? ###

* Please Clone the repo: ```git clone https://github.com/Sajzad/blog.git```.

* Install virtualenv on your system. For linux: ```pip install virtualenv```.

* Now, we go to blog dir. And create virtual environment with virtualenv: ```virtualenv -p /usr/bin/python3 .env```.

* Activate the virtual environment: source ```.env/bin/activate```.

* Install required dependencies: ```pip install -r requirements.txt```.

* Go to website dir where the manage.py file.

* Create migrations files: ```./manage.py makemigrations```.

* Update the database with migrations: ```./manage.py migrate```.

* We will create a superuser who is actually a manager for the system. Please type ```./manage.py createsuperuser``` and follow the shown process.

* Start the local server: ```./manage.py runserver```.

* Server can be accessed from this link ```http://127.0.0.1:8000/```.

* If you want superuser/manager access, please go ```http://127.0.0.1:8000/admin```.
