##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
##python3 script created by tBarford on 20220203
##
##
##File Description: Firebase Firstore Service - CRUD functions for BG golf app MVP
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~## 

import firebase_admin
from firebase_admin import credentials, firestore

## Write Operations ##

def writeToDb(db, docRef, dictToWrite: dict):
    docRef.set(dictToWrite)

def updateDbEntry(db, docRef, dictToWrite: dict):
    docRef.update(dictToWrite)

def writeToolData(db, shaft: str, shaftEntry: int, measurement: int, toolData: list):
    docRef = db.collection(u'eiDb').document(shaft).collection(u'fq_measure_'+str(shaftEntry)).document(str(measurement))
    docRef.set({u'tool_data':
        toolData
    })

def updateFields(db):
    docRef = db.collection(u'title').document(u'field')
    docRef.update({

    })

def readFromDb(db, docRef):
    try:
        doc = docRef.get()
        docDict = doc.to_dict()
        print(docDict)

    except Exception as e:
        print(e)  

def deleteFromDb(db):
    try:
        docRef = db.collection(u'title').document(u'field')
        doc = docRef.delete()
        
    except Exception as e:
        print(e) 
        
def main():
    #instantiate firebase
    credential = credentials.Certificate('./barford-golf-firebase-adminsdk-spu44-3b8446b75d.json') #this has to get updated when you get the info from firebase web
    root = firebase_admin.initialize_app(credential)
    db = firestore.client()

    docRef = db.collection(u'eiDb').document('Shaft').collection(u'fq_measure_1').document(u'6')

    readFromDb(db, docRef)




    


if __name__ == '__main__':
    main()