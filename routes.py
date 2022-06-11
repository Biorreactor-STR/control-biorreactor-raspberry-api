from flask import *
from main import *
from dataBase.dbFunctions import *

apiBiorreator = Flask("biorreator")

@apiBiorreator.route("/biorreator", methods=["GET"])
def biorreactorStatus():
    statusBiorreator = dbRead("C:/Users/ian10/Documents/Biorreactor/RPi/API/dataBase/status-biorreator.json")
    return(statusBiorreator)

@apiBiorreator.route("/biorreator/equipamentos", methods = ["GET"])
def getEquipsData():
    equipamentos = dbRead("C:/Users/ian10/Documents/Biorreactor/RPi/API/dataBase/equipamentos.json")
    return(equipamentos)

@apiBiorreator.route("/biorreator/equipamentos/led", methods = ["GET"])
def getLedData():
    header = request.headers["id"]
    return(str(ledVerification(header)))

@apiBiorreator.route("/biorreator/equipamentos/motor-dc-01", methods = ["GET"])
def getMotor1Data():
    header = request.headers["id"]
    return(str(ledVerification(header)))

@apiBiorreator.route("/biorreator/equipamentos/motor-dc-02", methods = ["GET"])
def getMotor2Data():
    header = request.headers["id"]
    return(str(ledVerification(header)))

apiBiorreator.run()


