# 注文フォーム

## How to install
```shell
# in your local environment
$ pip install virtualenv
$ pip install virtualenvwrapper
# I recommend you check the official documents of virtualenv and virtualenvwrapperr

# then clone this repository and do
$ mkvirtualenv apply_form -p python3.7
$ workon apply_form
$ cd apply_form
$ pip install -r requirements.txt
$ ./manage.py runserver
# move localhost:8000/apply then you can see the form
