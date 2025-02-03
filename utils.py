contactsList = {"contacts": [], "nextID": 1}

def showContacts():
    pass
        
def addContact(contactName, contactTel, contactEmail):
    pass

def deleteContact(contactID):
    pass

def findContact(contactName):
    find = False
    
    print("-" * 20)
    
    for contact in contactsList["contacts"]:
        if (contact["Name"] == contactName):
            showContactFromId(contact["ID"])
            find = True
    
    if(not find):
        print("Contatto non trovato")
        print("-" * 20)

def showContactFromId(id):
    for contact in contactsList["contacts"]:
        if(contact["ID"] == id):
            print(f"ID: {contact.get('ID', 'N/A')}")
            print(f"Nome: {contact.get('Name', 'N/A')}")
            print(f"Telefono: {contact.get('Tel', 'N/A')}")
            print(f"Email: {contact.get('Email', 'N/A')}")
            print("-" * 20)
            return
        
    print("Contatto non trovato")
    print("-" * 20)