from pymongo import MongoClient

mongoclient = MongoClient('localhost', 27017)

db = mongoclient['atomgreens']
tray_data = db['data']