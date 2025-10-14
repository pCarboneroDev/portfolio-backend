from ..dal.files import *



contactRoute = "dataInfo/app/data/contact.json"

def getAllcontacts(lang):
    contactList = []
    try:
        contactList = readFile(contactRoute)
        return contactList[lang]
    except FileNotFoundError:
        raise
    except KeyError:
        raise
    except Exception as e:
        raise Exception("Unexpected error while reading contacts") from e