contactsList = {"contacts": [], "nextID": 1}

def showContacts():
    if not contactsList["contacts"]:
        return "La lista dei contatti è vuota."
    
    for contact in contactsList["contacts"]:
        print(f"ID: {contact.get('ID', 'N/A')}")
        print(f"Nome: {contact.get('Name', 'N/A')}")
        print(f"Telefono: {contact.get('Tel', 'N/A')}")
        print(f"Email: {contact.get('Email', 'N/A')}")
        print("-" * 20)
        
def addContact(contactName, contactTel, contactEmail):
    pass

def deleteContact(contactID):
    pass

def findContact(contactName):
    pass