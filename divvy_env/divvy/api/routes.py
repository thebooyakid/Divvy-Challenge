#  Using Flask, create a REST API endpoint (aka route)
#  that accepts 'starttime' and 'endtime' parameters 
#  and returns the average duration for that time span
#   in the response.
from flask import Blueprint
from divvy.models import db,RaceInfo,race_schema
import pandas as pd
import sqlalchemy

api = Blueprint('api',__name__, url_prefix='/api')

engine=sqlalchemy.create_engine('postgresql+psycopg2://postgres:bazinga17Q#@127.0.0.1:5432/divvy')

data=pd.read_csv('../DivvyChallenge.csv', sep = ',')

@api.route('/getdata')
def getData():
    return {'work': 'please'}

@api.route('/race', methods = ['GET'])
def get_info():
    
    info = RaceInfo.query.get(id)
    
    response = race_schema.dump(info)
    
    panda_response = response.mean().round(decimales = 2)[['starttime', 'stoptime']]
    
    return panda_response


@api.route('/postdata', methods = ['POST'])
def postData():
    data.to_sql('divvy3',engine)
    return 'posted'