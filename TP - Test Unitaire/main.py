from fastapi import FastAPI
from mongoengine import connect
from models import Perso
# from models import Test
import json




app = FastAPI()
connect(db="perso", host="localhost", port=27017)




# READ #
@app.get("/get-perso")
def perso():
    persos = json.loads(Perso.objects().to_json())
    return {"élèves": persos}





# READ EN CHERCHANT LE PRENOM PRECIS #
@app.get("/get-by-name")
def perso_name(Name: str):
    return json.loads(Perso.objects(Name = n).to_json())







# CREATE #
@app.post("/createperso")
# async def perso_create(test: Test):
#     Perso(name=test.name, age=test.age, teams=test.teams).save()
#     return {"message":test}

async def perso_create(Name: str, Age: int, Teams: str):
    Perso(name=Name, age=Age, teams=Teams).save()
    return {"Création réussie"}





# SUPPRIMER #
@app.delete("/deleteperso")
async def perso_delete(NameExistant:str):
    Perso.objects(name = NameExistant).delete()
    return {"Suppression réussie"}




# UPDATE #
@app.put("/updateperso")
async def perso_update(NameExistant: str, NameModify: str, AgeModify: int, TeamsModify: str ):
    Perso.objects(name = NameExistant).modify(name = NameModify, age = AgeModify, teams = TeamsModify)
    return {"Modification réussie"}




