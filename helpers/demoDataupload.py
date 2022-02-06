##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
##python3 script created by tBarford on 20220206
##
##
##File Description: Helper to write wishData.json to firestore demo
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~## 
import sys
sys.path.insert(0, 'C:/Users/TimBarford_prrhvu6/OneDrive - iXBlue Defense Systems, Inc/Desktop/beamVibrationFEM/bg_streamlit_demo')
import firestoreservice as firestore
import json


def main():
    fs = firestore.FirestoreService()

    with open('../wishDat.json', 'r') as file:
        data = json.load(file) 

    for each in data:
        name, stiffness = each.split(':')
        data[each]['name']=name.strip()
        data[each]['stiffness']=stiffness.strip()

    def writeDemoDb(data: dict):
        for each in data:
            docRef = fs.db.collection(u'demo_db').document(data[each]['type']).collection(data[each]['name']).document(data[each]['stiffness'])
            docRef.set({
                'lengths': data[each]['length'], 
                'ei': data[each]['ei'], 
                'measuredFq': data[each]['measuredFq']
            })

    writeDemoDb(data)

    
if __name__ == '__main__':
    main()