import sae
import ts_controller
from flask import Flask, request, render_template

app = Flask(__name__)
app.debug = True

@app.route('/summary', methods=['GET'])
def get_summary():
    return ts_controller.get_summary()
    
@app.route('/tushuo', methods=['GET'])
def get_tushuo():
    args = request.args
    date = args['date']
    return ts_controller.get_content(date)

@app.route('/fetch', methods=['GET'])
def fetch_data():
#     args = request.args
#     url = args['url']
    return ts_controller.fetch()
    
application = sae.create_wsgi_app(app)
