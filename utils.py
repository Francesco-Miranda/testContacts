import re

phoneNumerRegex = re.compile(r"\d{10}")
emailRegex = re.compile(r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+")

contactsList = {"contacts": [], "nextID": 1}

def showContacts():
    pass
        
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

def deleteContact(contactID):
    pass

def findContact(contactName):
    pass