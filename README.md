# EshopReviewAPI
REST api for eshop quality reviews - https://eshopreviewapi.herokuapp.com/
## URLs
* `admin/` - admin.
* `api/` - api root.
* `api/reviews/` - all reviews.
* `api/reviews/[review_id]` - get, edit or delete review.
* `api/reviews/by_user` - get group by user email reviews order by creating time.
* `api/shops/` - get shop list order by rating or review count, support search by domain name.
* `api/auth/register` - register new user.
* `api/auth/token` - get current user token.

## Usage example
1. `http://eshopreviewapi.herokuapp.com/api/shops?ordering=-review_count` - will return shop list order by review count
2. `http://eshopreviewapi.herokuapp.com/api/shops?search=rozetka` - will serach shop with damain 'rozetka'
3. you  can find more examples in EshopReviews_localhost.postman_collection.json
## How to run Local
1. `git clone` - clone repository
2. `pytohn -m venv venv` - craete virtual enviroment
3. `venv/scripts/activate` - activate virtual enviroment
4. `pip install -r requirements.txt` - install requirements
5. create `.env` file in `config` folder by followin example (you can use  Sqlite instead PostgreSQL in `DATABASE_URL`):
```
DEBUG=**any or delete for DEBUG=False**
SECRET_KEY=**your secret key here**
DATABASE_URL=***psql://login:password@127.0.0.1:5432/db_name***
```
8. `python manage.py migrate` - migrate models to database
9. `python manage.py createsuperuser` - create superuser
10. `pytohn manage.py test` - run unittests
11. `pytohn manage.py runserver` - run server
## Deploy
### Heroku Setup
[Sign up](https://signup.heroku.com/)  for Heroku account (if you don’t already have one), and then install the  [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)  (if you haven't already done so).

Create a new app:

```
$ heroku create
Creating app... done, ⬢ evening-tundra-50688
https://evening-tundra-50688.herokuapp.com/ | https://git.heroku.com/evening-tundra-50688.git
```

Add the  `SECRET_KEY`  environment variable:

```
$ heroku config:set SECRET_KEY=SOME_SECRET_VALUE -a evening-tundra-50688
```
> Change  `SOME_SECRET_VALUE`  to a randomly generated string that's at least 50 characters.

Add the above Heroku URL to the list of  `ALLOWED_HOSTS`  in  _hello_django/settings.py_  like so:

`ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'evening-tundra-50688.herokuapp.com']`

> Make sure to replace  `evening-tundra-50688`  in each of the above commands with the name of your app.

###  Heroku Docker Deployment
Log in to the  [Heroku Container Registry](https://devcenter.heroku.com/articles/container-registry-and-runtime), to indicate to Heroku that we want to use the Container Runtime:

`$ heroku container:login`

Re-build the Docker image and tag it with the following format:

`registry.heroku.com/<app>/<process-type>`

Make sure to replace  `<app>`  with the name of the Heroku app that you just created and  `<process-type>`  with  `web`  since this will be for a  [web process](https://devcenter.heroku.com/articles/procfile#the-web-process-type).

For example:

`$ docker build -t registry.heroku.com/evening-tundra-50688/web .`

Push the image to the registry:

`$ docker push registry.heroku.com/evening-tundra-50688/web`

Release the image:

`$ heroku container:release -a evening-tundra-50688 web`

This will run the container. You should be able to view the app at  [https://APP_NAME.herokuapp.com](https://app_name.herokuapp.com/).

> Try running  `heroku open -a evening-tundra-50688`  to open the app in your default browser.
