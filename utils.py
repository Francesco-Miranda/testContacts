import re

phoneNumerRegex = re.compile(r"\d{10}")
emailRegex = re.compile(r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+")

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
    if(not phoneNumerRegex.match(contactTel)):
        return "Numero di telefono non valido"
    
    if(not emailRegex.match(contactEmail)):
        return "Email non valida"
    
    for contact in contactsList["contacts"]:
        if(contact["Tel"] == contactTel):
            return "Numero di telefono già presente"
    
    contactsList["contacts"].append({"ID": contactsList["nextID"],
                                     "Name": contactName, "Tel": contactTel, "Email": contactEmail})
    contactsList["nextID"] += 1
    return "Contatto aggiunto!"

def deleteContact(contactID):
    if not contactsList["contacts"]:
        return "La lista dei contatti è vuota."
    
    for i in range(len(contactsList["contacts"])):
        if contactsList["contacts"][i]['ID'] == contactID:
            contattoEliminato = f"{contactsList['contacts'][i].get('Name', 'N/A')}: {contactsList['contacts'][i].get('Tel', 'N/A')}"
            contactsList["contacts"].pop(i)
            return f"Contatto [{contattoEliminato}] eliminato con successo!"
        
    return f"Contatto {contactID} non trovato"

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