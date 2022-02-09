##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
##python3 script created by tBarford on 20220203
##
##
##File Description: Firebase Firstore Service - CRUD functions for BG golf app MVP
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~## 

import firebase_admin
from firebase_admin import credentials, firestore
import streamlit as st
import json
#import asyncio as io
#import concurrent

class FirestoreService(): 
    def __init__(self):
        #instantiate firebase
        credentialJson = json.loads(st.secrets["textkey"])
        _credential = credentials.Certificate(credentialJson) 
        try:
            _root = firebase_admin.get_app()
        except ValueError:
            _root = firebase_admin.initialize_app(_credential)
        self.db=firestore.client()
        #self.db = firestore.AsyncClient(credentials=_root.credential.get_credential(), project=_root.project_id)

    ## Read Operations
    def getShaftList(self, shaftType: str):
        docRef = self.db.collection('demo_db').document(shaftType).collections()
        shaftList = [shaft.id for shaft in docRef]
        return shaftList

    def getStiffness(self, shaftType: str, shaft:str):
        docRef = self.db.collection('demo_db').document(shaftType).collection(shaft).stream()
        stiffness = [doc.id for doc in docRef]
        return stiffness

    def getEI(self, shaftType: str, shaft: str, stiffness: str):
        docRef = self.db.collection('demo_db').document(shaftType).collection(shaft).document(stiffness)
        eiDict = docRef.get().to_dict()
        return (eiDict['lengths'], eiDict['ei'])

    def getFq(self, shaftType: str, shaft: str, stiffness: str):
        docRef = self.db.collection('demo_db').document(shaftType).collection(shaft).document(stiffness)
        fqDict = docRef.get().to_dict()
        return (fqDict['lengths'], fqDict['measuredFq'])

    


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
    #wdict = db.efficientGet('wood').to_dict()
    idict = db.getShaftList('iron')
    print(idict)
    

if __name__ == '__main__':
    main()
    