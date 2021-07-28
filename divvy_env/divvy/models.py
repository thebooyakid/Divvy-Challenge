from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

class RaceInfo(db.Model):
    # id = db.Column(db.Integer, primary_key = True)
    trip_id = db.Column(db.Numeric(20), primary_key = True)
    starttime = db.Column(db.String(20))
    stoptime = db.Column(db.String(20))
    bikeid = db.Column(db.Numeric(20))
    from_station_id = db.Column(db.Numeric(20))
    from_station_name = db.Column(db.String(100))
    to_station_id = db.Column(db.Numeric(20))
    to_station_name = db.Column(db.String(100))
    usertype = db.Column(db.String(20))
    gender = db.Column(db.String(20))
    birthday = db.Column(db.String(20))
    trip_duration = db.Column(db.Numeric(10))

    def __init__ (self,trip_id,starttime,stoptime,bikeid,from_station_id,from_station_name,to_station_id,to_station_name,usertype,gender,birthday,trip_duration):
        # self.id = self.set_id()
        self.trip_id = trip_id
        self.starttime = starttime
        self.stoptime = stoptime
        self.bikeid = bikeid
        self.from_station_id = from_station_id
        self.from_station_name = from_station_name
        self.to_station_id = to_station_id
        self.to_station_name = to_station_name
        self.usertype = usertype
        self.gender = gender
        self.birthday = birthday
        self.trip_duration = trip_duration

    # def set_id(self):
    #     return list(range(len(self.trip_id+1)))
    

class RaceSchema(ma.Schema):
    class Meta:
        fields = ['id','trip_id','starttime','stoptime','bikeid','from_station_id','from_station_name','to_station_id','to_station_name','usertype','gender','birthday','trip_duration']

race_schema = RaceSchema()