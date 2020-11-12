# Package Imports
import os
from flask import Flask, render_template

# Local Imports
from sliceofpy.components.database import initialize_tables as init_tables


def create_app(test_config=None):

    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    @app.route('/index')
    def index():
        init_tables()
        return render_template('index.html', title='SliceOfPy - Index')

    return app
