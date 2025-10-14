from flask import *
import sys
import os
# sube al directorio raíz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dataInfo.app.dal.experienceDal import *


experienceBP = Blueprint('experience', __name__)

@experienceBP.get('/')
def get_all_experience():
    lang = request.args.get("lang", default="en")
    

    exp = getAllExperience(lang)

    return exp