from django.shortcuts import render
import random
from sncf.models import Train

# Create your views here.
def acceuil(request):
    return render(request, "sncf/acceuil.html",{})

def aleatoire(request, train_id):
    listeTrain = Train.objects.all()
    premierTrain = random.choice(listeTrain) 

    print("ok")
    return render (request, "sncf/aleatoire.html", {
        "numero":premierTrain.number,
        "destination":premierTrain.destination,
        "heure":premierTrain.date,
        
    })

# Pour faire fonctionner cet fonction veiller à
# mettre n'importe quelle lettre ou chiffre après aleatoire/ dans l'URL