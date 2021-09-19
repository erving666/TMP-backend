# TMP-backend
Training management platform（ 培训管理平台 ）

## Start
1. pip install -r requirements.txt
2. npm run server

## 踩坑
mysql@8.0
SELECT user,host FROM mysql.user;
create user ervin identified by 'yeyuwei';
grant all privileges on *.* to 'ervin'@'%' identified by 'yeyuwei';  # mysql 5.7
GRANT ALL PRIVILEGES ON *.* TO 'ervin'@'%' WITH GRANT OPTION;    # mysql 8.0
flush privileges;

ALTER USER 'ervin'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password'; 
ALTER USER 'ervin'@'%' IDENTIFIED WITH mysql_native_password BY 'password'; # work!