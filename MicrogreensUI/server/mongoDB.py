from pymongo import MongoClient

mongoclient = MongoClient('localhost', 27017)

db = mongoclient['atomgreens']
tray_data = db['data']
status = db['TRAY_STATUS_view']


def view_create():
    db.command({
        "create": "TRAY_STATUS_view",
        "viewOn": "data",
        "pipeline": [
            {
                '$match': {
                    'tray': 1,
                    'time': {
                        '$exists': True
                    }

                }
            },
            {
                '$sort': {
                    'time': -1
                }
            },
            {
            '$group':
                {
                '_id': '$sensor',
                'doc': {
                    '$first': '$$ROOT'
                }
                }
            },
            {
            '$replaceRoot':
                {
                    'newRoot': '$doc'
                }
            }

        ]
    }
    )
