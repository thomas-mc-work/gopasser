# Gopass template file resolver

… or whatever it could be called better.

With a given gopass store:

    $ echo "login: root" | gopass cat server/local/mysql
    $ gopass generate --lang=de server/local/mysql 24
    
    $ goapss ls
    gopass
    ├── …
    └── server/
        └── local/
            └── mysql

… and an example file like this:

    [client]
    host=127.0.0.1
    user={{ gp('login', 'server/local/mysql') }}
    password={{ gp('password', 'server/local/mysql') }}

The output shall look like that:

    [client]
    host=127.0.0.1
    user=root
    password=4osV5fLfJ94o1epLyBK4UPZe

## Usage

    curl -L "https://github.com/thomas-mc-work/gopasser/archive/refs/heads/master.tar.gz" | tar xz
    cd gopasser-master
    pip install -r requirements.txt
    python3 main.py my.cnf.gp

## Explanation

For the sake of a quick example I had to use the function feature of the jinja2 template engine. This is of course a bit ugly, but it does the job.

    {{ gp('password', 'server/local/mysql') }}

- `password`: The key of the field of a gopass entry
- `server/local/mysql`: The path of a gopass entry
