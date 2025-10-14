from ..dal.files import *



contactRoute = "dataInfo/app/data/about.json"

def getAllAbout(lang):
    try:
        aboutList = readFile(contactRoute)
        return aboutList[lang]
    except FileNotFoundError:
        raise
    except KeyError:
        raise
    except Exception as e:
        raise Exception("Unexpected error while reading contacts") from e