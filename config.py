class Config(object):
    SECRET_KEY = "123456"
    mysql_db_username = 'ervin'
    mysql_db_password = 'yeyuwei'
    mysql_db_name = 'tmp_flask'
    mysql_db_hostname = '127.0.0.1:3306'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}".format(
        DB_USER=mysql_db_username,
        DB_PASS=mysql_db_password,
        DB_ADDR=mysql_db_hostname,
        DB_NAME=mysql_db_name)
