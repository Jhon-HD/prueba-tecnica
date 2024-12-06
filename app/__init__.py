import os
import requests

from flask import Flask, request, jsonify, render_template
from app.constants import HttpStatus
from flasgger import Swagger


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    app.config['SWAGGER'] = {
        'title': 'Flask API Project',
        'uiversion': 3
    }
    Swagger(app, template_file="swagger.yaml")

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/data', methods=['GET'])
    def data():
        url = "https://jsonplaceholder.typicode.com/posts/"
        try:
            title = request.args.get('title')
            params = {
                "title": title
            }
            response = requests.get(url, params=params)
            if response.status_code == HttpStatus.OK:
                if response.json():
                    return render_template('posts/index.html', posts=response.json())
                return jsonify({"error": "Failed to fetch data"}), HttpStatus.NOT_FOUND
            return jsonify({"error": f"Failed to fetch data, Status code: {response.status_code}"}), response.status_code
        except requests.exceptions.RequestException as e:
            return jsonify({'error': str(e)}), HttpStatus.SERVER_ERROR

    return app