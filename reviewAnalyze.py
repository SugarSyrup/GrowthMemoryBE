import schedule
import time
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app

cred = credentials.Certificate("authentication/firebase_auth.json")
default_app = initialize_app(cred)
db = firestore.client()

def review_analyze() :
    reivews_ref = db.collection('review')
    reviews = reivews_ref.stream()

    for review in reviews:
        #uid
        print(review.id)

        for key in review.to_dict().keys():
            if not review.to_dict()[key]['isAnalyze'] :
                update_data = review.to_dict()[key]
                update_data['isUpdate'] = True
                reivews_ref.document(review.id).update({'24-02-17': update_data})
                print(review.to_dict())


review_analyze()
#schedule.every(1).days.at("01:00").do(review_analyze)