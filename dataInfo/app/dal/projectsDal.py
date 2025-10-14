from ..entities.clsProject import Project
from ..dal.files import *



projectsRoute = "dataInfo/app/data/projects.json"

def getAllProjects(lang):
    projectList = []
    try:
        projectList = readFile(projectsRoute)
        return projectList[lang]
    except FileNotFoundError:
        raise
    except KeyError:
        raise
    except Exception as e:
        raise Exception("Unexpected error while reading projects") from e
