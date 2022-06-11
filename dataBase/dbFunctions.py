import json
def dbRead(local:str):
    with open(local, encoding="utf-8") as json_read:
        dicionario = json.load(json_read)
    
    return(dicionario)


