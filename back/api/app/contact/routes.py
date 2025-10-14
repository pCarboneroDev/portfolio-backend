from flask import *
import sys
import os
# sube al directorio raíz
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from back.dataInfo.app.dal.contactDal import *


contactBP = Blueprint('contact', __name__)

@contactBP.get('/')
def get_all_contacts():
    try:
        lang = request.args.get("lang", default="en")
        contacts = getAllcontacts(lang)
        return jsonify(contacts)
    except FileNotFoundError:
        return jsonify({"error": "Contacts file not found"}), 404
    except KeyError:
        return jsonify({"error": f"Language '{lang}' not available"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500