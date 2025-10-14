from ..dal.files import *

expRoute = "dataInfo/app/data/experience.json"

def getAllExperience(lang):
    expList = []
    
    try:
        expList = readFile(expRoute)
    except Exception as e:
        print(e)
    
    return expList[lang]