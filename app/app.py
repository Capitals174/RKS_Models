import os

from waitress import serve
from flask import Flask, request, render_template, abort
from flask_bootstrap import Bootstrap
from models import Form1, Form2, Form3, Form4
from config import BaseConfig

HOST = os.environ.get('HOST', '0.0.0.0')
PORT = int(os.environ.get('PORT', '8000'))

app = Flask(__name__)
app.config.from_object(BaseConfig)
Bootstrap(app)

forms = {
    '1 очередь, ОХА': (Form1, 'model_1.html'),
    '1 очередь, СА': (Form2, 'model_2.html'),
    '2 очередь, СА': (Form3, 'model_3.html'),
    '2 очередь, ОХА': (Form4, 'model_4.html')
}


@app.route('/', methods=['POST', 'GET'])
def index():
    result = None
    model_name = request.args.get('f') or next(iter(forms))

    if model_name not in forms:
        abort(404)

    cls_form, template = forms.get(model_name)
    form = cls_form(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        result = form.predict()

    return render_template(template, models=forms.keys(), form=form, result=result, active_page=model_name)


if __name__ == '__main__':
    if app.config["DEBUG"]:
        app.run(debug=True, host=HOST, port=PORT)
    else:
        serve(app, host=HOST, port=PORT)
