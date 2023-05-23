import pymongo
import certifi
from encryption import decrypt


def get_user_info():
    ca = certifi.where()


    client = pymongo.MongoClient("mongodb+srv://wsalpha:Pepapepa001025762@cluster.z2o7sex.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)

    db = client["wsAlpha"]
    collection = db["users"]

    cursor = collection.find({}, {"_id": 1, "email": 1, "name": 1, 'keyword1': 1, 'keyword2': 1, 'keyword3': 1, 'keyword4': 1, 'keyword5': 1})

    user_info = []

    counter = 0
    for i in cursor:
        user_info.append([i['_id'],'email'+i['email'], i['name'], i["keyword1"],i['keyword2'], i["keyword3"],i['keyword4'], i["keyword5"]])
        counter += 1


    return user_info


def get_users():
    x = get_user_info()
    for i in range(1, len(x)):
        if x[i][0][0:5] == 'email':
            x[i][0] = decrypt(x[i][0][5:])

    return x


def availability(new_email):
    info = get_user_info()
    emails = []
    for i in info:
        emails.append(decrypt(i[1][5:]))
    if new_email in emails:
        return True
    return False


