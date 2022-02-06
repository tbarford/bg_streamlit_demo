##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
##python3 script created by tBarford on 20220203
##
##
##File Description: Firebase Firstore Service - CRUD functions for BG golf app MVP
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~## 

import firebase_admin
from firebase_admin import credentials, firestore

class FirestoreService(): 
    def __init__(self):
        #instantiate firebase
        _credential = credentials.Certificate('../barford-golf-firebase-adminsdk-spu44-3b8446b75d.json') 
        try:
            _root = firebase_admin.get_app()
        except ValueError:
            _root = firebase_admin.initialize_app(_credential)
        self.db = firestore.client()
    
    ## Read Operations
    def getShaftList(self, shaftType: str):
        collectionList = self.db.collection('eiDb').document(shaftType).collections()
        shaftList = [shaft.id for shaft in collectionList]
        return shaftList

    def getStiffness(self, shaftType: str, shaft:str):
        docRef = self.db.collection('eiDb').document(shaftType).collection(shaft).stream()
        stiffness = [doc.id for doc in docRef]
        return stiffness

        
    def getEI(self, shaftType: str, shaft: str, stiffness: str):
        docRef = self.db.collection('eiDb').document(shaftType).collection(shaft).document(stiffness)
        eiDict = docRef.get().to_dict()
        lengths = [int(key) for key in eiDict.keys()]
        lengths.sort()
        ei = [eiDict[str(length)] for length in lengths]
        return (lengths, ei)

    def readToolMeasure(self):
        collectionRef = self.db.collection('eiDb').document('Shaft').collection('fq_measure_1')
        docList = [doc.to_dict() for doc in collectionRef.get()]
        return  docList

         



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
    db = FirestoreService()
    print(db.getEI('Irons', 'Dynamic Gold', 'X100'))
    



    


if __name__ == '__main__':
    main()