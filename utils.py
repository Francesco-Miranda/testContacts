contactsList = {"contacts": [], "nextID": 1}

def showContacts():
    pass
        
def addContact(contactName, contactTel, contactEmail):
    pass

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
    pass