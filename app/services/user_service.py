import inject
from app.repositorys.user_repository import UserRepository


class UserService:
    user_repository = inject.attr(UserRepository)

    def user_persist(self, entity):  # 创建用户
        self.user_repository.user_persist(entity=entity)

    def login(self, **key):
        return self.user_repository.login(**key)
