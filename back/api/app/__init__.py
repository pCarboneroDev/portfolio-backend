from flask import *
from .projects.routes import projectsBP
from .experience.routes import experienceBP
from .contact.routes import contactBP
from .about.routes import aboutBP
from back.dataInfo.app.dal.files import readFile
from back.dataInfo.app.dal.projectsDal import *
from back.dataInfo.app.dal.experienceDal import *
from back.dataInfo.app.dal.contactDal import *

app = Flask(__name__)

app.register_blueprint(projectsBP, url_prefix='/projects')
app.register_blueprint(experienceBP, url_prefix='/experience')
app.register_blueprint(contactBP, url_prefix='/contact')
app.register_blueprint(aboutBP, url_prefix='/about')

# #get all
@app.get('/')
def get_all_():
    return jsonify(getAllProjects('en'), getAllExperience('en'), getAllcontacts('en'))