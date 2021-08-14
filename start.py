import os

from flask_script import Manager

from app import create_app  # 不指定模块名默认是__init__.py文件

app = create_app()
manager = Manager(app)
if __name__ == '__main__':
    manager.run()
