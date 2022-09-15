from mongoengine import Document
from mongoengine.fields import StringField


class Record(Document):
    first_name = StringField(max_length=30, null=False)
    last_name = StringField(max_length=40, null=False)
    email = StringField(max_length=40, null=True)
    address = StringField(max_length=100, null=True)
    phone = StringField(max_length=20, null=True)

    def __repr__(self):
        print(f'{self.first_name} {self.last_name}: {self.phone}, {self.email}, {self.address}')
