from pony.orm import db_session, select

from models import User, Address

class UserRepo:
    def __init__(self):
        self.model = User

    @db_session
    def get_address(self):
        return Address.get(lambda a: a.address_id == 2)

    @db_session
    def get_by_id(self, id):
        user = self.model.get(lambda u: u.user_id == id)
        return user
    @db_session
    def get_all(self):
        users = self.model.select(lambda u: u).prefetch(Address).page(1).to_list()
        return users

    @db_session
    def get_user_by_email(self, expected_email):
        user = self.model.select(lambda u: u.email == expected_email).prefetch(Address).page(1).to_list()
        return user

    @db_session
    def get_user_by_email_2(self, expected_email):
        user = select(u for u in self.model if u.email == expected_email).prefetch(Address).page(1).to_list()
        return user

    @db_session
    def create(self, email, password, age, address):
        self.model(email=email, password=password, age=age, address=address)

    @db_session
    def update_email(self, id, email):
        user = self.get_by_id(id)
        user.email = email

    @db_session
    def delete_user(self, id):
        user = self.get_by_id(id)
        user.delete()

repo = UserRepo()
print(repo.get_all())
print(repo.get_user_by_email("firstemail@gmail.com"))
print(repo.get_user_by_email_2("firstemail@gmail.com"))
print(repo.get_by_id(2))
# a = repo.get_address()
# repo.create("test", "test", 20, 2)
repo.update_email(6, "new_mail")
print(repo.get_by_id(6).email)
repo.delete_user(6)
print(repo.get_all())


def remove_users(id_list):
    for id in range(0, 100500):
        repo.delete_user(id)