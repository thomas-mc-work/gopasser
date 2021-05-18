[client]
host=127.0.0.1
port=3306
user={{ gp('login', 'server/local/mysql') }}
password={{ gp('password', 'server/local/mysql') }}
