#!/usr/bin/python

from flask import Flask, request
import os, sys, logging, json

import objects_managers.nst_manager as nst_manager
import objects_managers.nsi_manager as nsi_manager


app = Flask(__name__)

# ----- NETSLICE TEMPLATE Actions -----
@app.route('/nst/v1/descriptors', methods=['POST'])
def postNST():
    receivedNSTd = request.json
    new_NSTid = nst_manager.createNST(receivedNSTd)
    
    return ('New NST created into the database with id: ' + str(new_NSTid))

@app.route('/nst/v1/descriptors', methods=['GET'])
def getAllNST():
    allNST = nst_manager.getAllNst()
    jsonNSTList = json.dumps(allNST, indent=4, sort_keys=True)
    logging.info('Returning all NST')
    
    return (jsonNSTList)

@app.route('/nst/v1/descriptors/<int:nstId>', methods=['GET'])
def getNST(nstId):
    returnedNST = nst_manager.getNST(nstId)
    jsonNST = json.dumps(returnedNST, indent=4, sort_keys=True)
    logging.info('Returning the desired NST')
    
    return jsonNST

@app.route('/nst/v1/descriptors/<int:nstId>', methods=['DELETE'])
def deleteNST(nstId):
    deleted_NSTid = nst_manager.deleteNST(nstId)
    
    return ('Deletes the specified NST with id: ' +str(deleted_NSTid))


## ----- NETSLICE INSTANCE Actions -----
#@app.route('/nsi', methods=['POST'])
#def createNSI():

#  return 'Creating a new NSI!'

@app.route('/nsilcm/v1/nsi', methods=['GET'])
def getALLNSI():
  allNSI = nsi_manager.getAllNsi()
  jsonNSIList = json.dumps(allNSI, indent=4, sort_keys=True)
  logging.info('Returning all existing NSIs (instantiated/terminated/etc.)')
  
  return (jsonNSIList)

@app.route('/nsilcm/v1/nsi/<int:nsiId>', methods=['GET'])
def getNSI(nsiId):
  returnedNSI = nsi_manager.getNSI(nsiId)
  jsonNSI = json.dumps(returnedNSI, indent=4, sort_keys=True)
  logging.info('Returning the desired NSI')
  
  return jsonNSI

#@app.route('/nsi/<int:nsiId>', methods=['DELETE'])
#def deleteNSI(nsiId):
#  #db.nsi_list.del[nsiId]

#  return 'Deletes the specific NSI'

@app.route('/nsilcm/v1/nsi/<int:nsiId>/instantiate', methods=['POST'])
def postNSIinstantiation(nsiId):
  receivedNSI = request.json
  new_NSI = nsi_manager.createNSI(receivedNSI)
  nsiId_instantiated = nsi_manager.instantiateNSI(new_NSI)
  
  return ("Instantiation done of NSI with ID: " + str(nsiId_instantiated))

@app.route('/nsilcm/v1/nsi/<int:nsiId>/terminate', methods=['POST'])
def postNSItermination(nsiId):
  terminationRx = request.json
  terminate_nsiId = nsi_manager.terminateNSI(nsiId, terminationRx)
  
  return terminate_nsiId

#MAIN FUNCTION OF THE SERVER
if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port='5998')
