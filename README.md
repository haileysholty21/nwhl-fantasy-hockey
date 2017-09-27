# nwhl-fantasy-hockey
## Running Locally

Make sure you have Python [installed properly](http://install.python-guide.org).  Also, install the [Heroku Toolbelt](https://toolbelt.heroku.com/) and [Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup).

If pip isnt installed (on a mac), run:
sudo easy_install pip
If django isn't installed, run: 
pip install django
```sh
$ heroku git:clone -a nwhl-fantasy-hockey
$ cd nwhl-fantasy-hockey

$ pipenv install
(if you don't have pipenv installed, run $ pip install pipenv and then run the above line)

$ source env/bin/activate
$ pip install -r requirements.txt

-- dont run this yet, I haven't tried it out, and you can run locally without it -- $ createdb nwhl_fantasy_hockey
(make sure postgresql is running before you do the above command, otherwise it will error)

$ python manage.py migrate
$ python manage.py collectstatic

If using unix (a mac, for example), run the following to run the app locally:
$ heroku local

If using Windows, run the following to run the app locally
$ heroku local web -f Procfile.windows
```

Your app should now be running on [localhost:5000](http://localhost:5000/).

## Pushing local changes 

```sh
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
