# wb-task

The bulk of the app's logic (views, models) is in `wb_task/user_profiles/`.

Code formatted with [Black](https://black.readthedocs.io/en/stable/)


## Installation

```
$ git clone https://github.com/jams2/wb-task && cd wb-task
```

You can perform the installation manually;

```
$ python3 -m venv .venv
$ . .venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py loaddata fixtures/setup.json  # allauth SocialApp settings
$ python manage.py loaddata fixtures/geo.json  # cities_light City records
```

Or just `$ ./install`.


## Usage

Run the Django development server with `$ ./manage.py runserver`.

Visit [http://127.0.0.1:8000](http://127.0.0.1:8000). Please use the IP address instead of "localhost" as Github expects this for the redirect url.


## Testing

`$ ./manage.py test`
