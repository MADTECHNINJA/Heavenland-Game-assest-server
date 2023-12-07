import os
from flask import Blueprint, Response, send_file,send_from_directory,abort

filepath_static = 'src/static_content'

controller = Blueprint("controller",__name__)

@controller.route("/root")
def indexControl():
    return Response("Root of Controller",200)

@controller.route("/<file_name>",methods=['GET'])
def getFirst(file_name):
    try :
        # root_dir = os.path.dirname(os.getcwd())
        root_dir = os.getcwd()
        print(f"Static file path : {root_dir}")
        print(f"WIth path join {os.path.join(root_dir,filepath_static)}")
        return send_from_directory(os.path.join(root_dir,filepath_static),file_name,as_attachment=True)
    except FileNotFoundError:
        abort(404)