from django.shortcuts import render,get_object_or_404, redirect
from .models import Client , Ascenseur
from .forms import ClientForm
from .forms import AscenseurForm
from django.contrib import messages
from django.http import HttpResponse

#les vues pour la gestion des clients
# liste des clients
def liste_clients(request):
    clients = Client.objects.all()
    return render(request, 'gestion/liste_clients.html',{'clients': clients})


#Vue pour ajouter un client
#fonction : formulaire pour ajouter un client
def ajouter_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre le client dans la base de données
            messages.success(request, "Le client a été ajouté avec succès.")
            return redirect('liste_clients')  # Redirige vers la liste des clients
    else:
        form = ClientForm()
    return render(request, 'gestion/ajouter_client.html', {'form': form})

#Vue pour modifier un client
#fonction formulaie pour modifier un client
def modifier_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)  #instanciation de la variable client
        if form.is_valid():
            form.save()  #Enregistrer les modifications
            messages.success(request, "Le client a été modifié avec succès.")
            return redirect ('liste_clients')  #rediriger vers la page liste_clients aprés modifications
    else:
        form = ClientForm(instance=client)
    return render (request, 'gestion/modifier_client.html', {'form': form , 'client':client})
    
#vue pour supprimer un client
#fonction pour confirmer et effectuer la suppression

def supprimer_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == "POST":
        client.delete()  #supprimer le client
        messages.success(request, "Le client a été supprimé avec succès.")
        return redirect('liste_clients') #rediriger vers la liste des clients
    #  page pour confirmer la suppression
    return render(request, 'gestion/supprimer_client.html', {'client': client})



#les vues pour les ascenseurs

#la vue pour la liste des ascenseurs
def liste_ascenseurs(request):
    ascenseurs= Ascenseur.objects.all()
    return render( request, 'gestion/liste_ascenseurs.html', {'ascenseurs': ascenseurs})

#la vue pour ajouter un ascenseurs
def ajouter_ascenseur(request):
    if request.method == "POST":
        form = AscenseurForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "L'ascenseur a été ajouté avec succès.")
            return redirect('liste_ascenseurs')
    else:
        form=AscenseurForm()
    return render(request, 'gestion/ajouter_ascenseur.html', {'form': form})

#la vue pour modifier un ascenseurs
def modifier_ascenseur(request, id):
    ascenseur = get_object_or_404(Ascenseur, id=id)
    if request.method == "POST":
        form = AscenseurForm(request.POST, instance=ascenseur)
        if form.is_valid():
            form.save()
            messages.success(request, "L'ascenseur a été modifié avec succès.")
            return redirect( 'liste_ascenseurs')
    else:
        form=AscenseurForm()
    return render(request, 'gestion/modifier_ascenseur.html', {'form': form, 'ascenseur': ascenseur})

#la vue pour supprimer un ascenseurs
def supprimer_ascenseur(request, id):
    ascenseur =get_object_or_404(Ascenseur, id=id)
    if request.method == "POST":
        ascenseur.delete()
        messages.success(request, "L'ascenseur a été supprimé avec succès.")
        return redirect('liste_ascenseurs')
    else:
        form=AscenseurForm()
    return render (request, 'gestion/supprimer_ascenseur.html', {'form': form, 'ascenseur': ascenseur})
        
