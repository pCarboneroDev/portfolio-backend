from flask import *
import sys
import os
# sube al directorio raíz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dataInfo.app.dal.projectsDal import *


projectsBP = Blueprint('projects', __name__)


@projectsBP.get('/')
def get_all_projects():
    try:
        lang = request.args.get("lang", default="en")
        projects = getAllProjects(lang)
        return jsonify(projects), 200
    except FileNotFoundError:
        return jsonify({"error": "Projects file not found"}), 404
    except KeyError:
        return jsonify({"error": f"Language '{lang}' not available"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    