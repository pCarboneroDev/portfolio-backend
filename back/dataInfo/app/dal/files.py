import json

def readFile(route):
    file = open(route, "r", encoding="utf-8")
    object = json.load(file)
    file.close()
    return object


def escribirFichero(route, object):
    file = open(route, "w")
    json.dump(object, file)
    file.close()