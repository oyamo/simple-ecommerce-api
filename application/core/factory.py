import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("creds.json")
firebase_admin.initialize_app(cred)
#Database for I/O stuff
_database = firestore.client()
#Factory class for exporting any Important Info
class AppFactory(object):
    #Firebase Database
    db = _database
    constants = {
        'base_fields' :{'category':list,'product_name':str, 'description': str ,'product_price':float,'img_urls':list,'currency':str, 'quantity':int}
    }

