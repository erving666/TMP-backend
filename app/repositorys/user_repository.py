from db import UserSQL


class UserRepository:
    # 用户注册添加新的用户
    def user_persist(self, entity):
        UserSQL.persist(entity=entity)

    def login(self, **key):
        try:
            user = UserSQL.get(**key)
        except Exception as e:
            return None
        return user
