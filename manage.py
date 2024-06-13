from flask import Flask, render_template

from scr.views import  DTServerSide

import os

template_dir = os.path.abspath('scr/templates')
app = Flask(__name__, template_folder=template_dir)


@app.route('/')
def principal():
    return render_template("index.html")


if __name__ == '__main__':

    app.register_blueprint(DTServerSide.main, url_pregfix='/')

    app.run(debug=True)
