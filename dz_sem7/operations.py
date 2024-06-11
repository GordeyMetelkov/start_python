import view, db
def add_op():
    with open ('base.txt', 'a') as file:
        file.write(f"{view.input_surname()} {view.input_name()}: {view.input_num()}\n")
def search():
    searching = view.input_name()
    with open ('base.txt', 'r') as file:
        contacts = file.read()
        contacts = contacts.split('\n')
        for i in range(len(contacts)):
            if searching in contacts[i]:
                phone = contacts[i].split(': ')[1]
        print (phone)
def delete():
    searching = view.input_name()
    with open ('base.txt', 'r') as file:
        contacts = file.read()
        contacts = contacts.split('\n')
    with open ('base.txt', 'w') as file:
        for i in range(len(contacts)):
            if searching not in contacts[i]:
                file.write(f'{contacts[i]}\n')

# add_op()
# search()
delete()
