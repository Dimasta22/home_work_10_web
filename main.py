from model import Record


def add_contact(first_name, last_name, email, address, phone):
    record = Record(first_name=first_name, last_name=last_name, email=email, address=address, phone=phone).save()
    return record


def update_contact(_id, email):
    record = Record.objects(id=_id)
    record.update(email=email)
    return record


def delete_contact(_id):
    record = Record.objects(id=_id)
    return record.delete()


def all_contacts():
    all_record = Record.objects()
    for record in all_record:
        print(record.first_name)


if __name__ == '__main__':
    #print(add_contact('Vasyl', 'Teliga', 'dkdkm@jjj', 'Dnipro', '3333333'))
    #print(update_contact("63222db2bd47e064b79171f6", 'kskmdms@jjj'))
    #print(delete_contact("63222db2bd47e064b79171f6"))
    all_contacts()

