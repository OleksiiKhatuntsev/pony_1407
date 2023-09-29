from pony.orm import Database, PrimaryKey, Required, Set, db_session

db = Database()
db.bind(provider='postgres', user='postgres', password='admin', host='127.0.0.1', database='group1407')


class Address(db.Entity):
    _table_ = "addresses"
    address_id = PrimaryKey(int, auto=True)
    city = Required(str, 300)
    country = Required(str, 300)
    users = Set("User")



class User(db.Entity):
    _table_ = "users"
    user_id = PrimaryKey(int, auto=True)
    email = Required(str, 300)
    password = Required(str, 300)
    age = Required(int)
    address = Required(Address, column="address_id")

    # def __str__(self):
    #     return f"{self.email}, {self.address.city}"
    # def __repr__(self):
    #     return f"{self.email}, {self.address.city}"


db.generate_mapping()
