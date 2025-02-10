import utils as u


print(u.contactsList)
u.addContact("Mario", "1234567890", "mario@gmail.it")
u.addContact("Luigi", "1234567899", "luigi@gmail.it")

u.showContacts()
print("\nfind")
u.findContact("Mario")

print("\ndelete")
u.deleteContact(1)

print("\nshow")
u.showContacts()

print("\nfind")

u.findContact("Mario")
