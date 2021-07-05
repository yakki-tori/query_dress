from bottle import route, run, template
import pandas as pd

@route('/hello/<id>')
def index(id):
    datapath= "domodata.csv"
    data = pd.read_csv(datapath)
    d = data.loc[data['id']==int(id)]
    return template('<b>{{dress}}</b>', dress=d['dress'].values)

run(host='localhost', port=8080)