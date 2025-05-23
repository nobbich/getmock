# -*- coding: utf-8 -*-

from flask import Flask, request, send_file, abort
import configparser
import os

app = Flask(__name__)

# load config
config = configparser.ConfigParser()
config.read('config.ini')

# Dictionary für Ressourcennamen und Pfade
resource_paths = {}
for section in config.sections():
    resource_name = config[section]['resource_name']
    file_path = config[section]['file_path']
    resource_paths[resource_name] = file_path

# Route to return xml
@app.route('/<path:resource_name>', methods=['GET'])
def get_xml(resource_name):
    if resource_name in resource_paths:
        file_path = resource_paths[resource_name]
        if os.path.exists(file_path):
            return send_file(file_path, mimetype='application/xml')
        else:
            abort(404, description="File not found.")
    else:
        abort(404, description="Resource not found.")

if __name__ == '__main__':
    app.run(host='subdn113', port=88)
