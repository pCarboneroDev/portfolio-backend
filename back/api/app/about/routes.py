from flask import *
import sys
import os
# sube al directorio raíz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dataInfo.app.dal.aboutMeDal import *


aboutBP = Blueprint('about', __name__)

@aboutBP.get('/')
def get_about():
    try:
        lang = request.args.get("lang", default="en")
        about = getAllAbout(lang)
        return jsonify(about)
    except FileNotFoundError:
        return jsonify({"error": "Contacts file not found"}), 404
    except KeyError:
        return jsonify({"error": f"Language '{lang}' not available"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500