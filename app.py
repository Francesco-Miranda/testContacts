from utils import *

def main():
    print("Hello World!")

    while(True):
        print("Che vuoi fare?")

        print("0. Exit")
        print("1. Vedere i contatti")
        print("2. Aggiungere contatto")
        print("3. Cancellare un contatto")
        print("4. Trovare un contatto")

        choise = -1
        while(choise < 0 or choise > 4):
            try:
                choise = int(input("Inserisci scelta: "))
            except ValueError:
                print("Inserire un valore valido")
                
        print("----------------------------------------------------------------")

        match choise:
            case 0:
                exit(0)
            case 1:
                showContacts()
            case 2:
                while(True):
                    print("Inserisci i dati del contatto che vorresti aggiungere")
                    contactName = input("Nome: ")
                    contactTel = input("Tel: ")
                    contactEmail = input("Email: ")
                    print(addContact(contactName, contactTel, contactEmail))
                    
                    if(input("Aggiungere un altro contatto? Y/N: ").upper()[0] == "N"):
                        break
            case 3:
                while(True):
                    print("Quale contatto desideri eliminare?")
                    showContacts()
                    contactID = int(input("ID Contatto: "))
                    print(deleteContact(contactID))

                    if(input("Eliminare un altro contatto? Y/N: ").upper()[0] == "N"):
                        break
            case 4:
                print("Quale contatto desideri trovare?")
                contactName = input("Nome contatto: ")
                findContact(contactName)
                
        print("----------------------------------------------------------------")

if __name__ == "__main__":
    main()