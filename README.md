# heroku-deploy-geodjango
This is the code for the tutorial on deploying a Geodjango app to Heroku in 2019

Find the tutorial on Medium https://medium.com/@ochieng.grace/deploy-geodjango-application-on-heroku-in-2019-part-1-eb4406ee0cc4

To run it locally

#### Clone the repo

#### Change .envtest to .env and make changes to database credentials appropriately

#### Install requirements

```pip install -r requirements.txt```

#### Migrate Tables

```python manage.py makemigrations```

```python manage.py migrate```

#### Run the app

```python manage.py runserver```

Navigate to `127.0.0:8000` on your favorite browser.
