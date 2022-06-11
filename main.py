from dataBase.dbFunctions import *

def ledVerification(id:str=""):
    db = dbRead("C:/Users/ian10/Documents/Biorreactor/RPi/API/dataBase/equipamentos.json")
    led = db["led"]
    
    if id:
        return(led[id])
    else:
        return(led)
    
def dbVerification(path:str,elemento:str,id:str=""):
    db = dbRead(path)
    dbElemento = db[elemento]
    
    if id:
        return(dbElemento[id])
    else:
        return(dbElemento)