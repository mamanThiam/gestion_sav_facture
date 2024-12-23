from django.shortcuts import render,get_object_or_404, redirect
from .models import Client , Ascenseur
from .forms import ClientForm
from .forms import AscenseurForm
from django.contrib import messages
from django.db.models import Q
from reportlab.pdfgen import canvas
from django.http import HttpResponse
import openpyxl
#les vues pour la gestion des clients
# liste des clients
def liste_clients(request):
    query = request.GET.get ('q')  # Recuperation de la requete de recherche
    if query:
        clients = Client.objects.filter(
            Q(nom__icontains=query) | #rechercher par nom
            Q(email__icontains=query) #rechercher par email
        )
    else:
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

#Rapport en pdf
def rapport_clients_pdf(request):
# Création de la reponse http avec une en-tete pdf
    response = HttpResponse(content_type ='application/pdf')
    response['Content_Disposition'] = 'attachment; filename= "rapport_clients.pdf"'
#Génération du document pdf
    pdf_canvas = canvas.Canvas(response)
    pdf_canvas.setFont("Times New Roman", 12 )
    pdf_canvas.drawString(100,800,"Rapport des clients")
#Recupération des données des clients
    clients = Client.object.all()
    y_position = 750
    for client in clients:
        pdf_canvas.drawString(100,y_position, f"Nom:{client.nom}, Téléphone:{client.telephone}, Adresse:{client.adresse}")
        y_position -= 20

    pdf_canvas.save()
    return response



#les vues pour les ascenseurs

#la vue pour la liste des ascenseurs
def liste_ascenseurs(request):
    query = request.GET.get('q')
    if query:
        ascenseurs= Ascenseur.objet.filter(
            Q(client__nom__icontains=query) | #recherche par nom client
            Q(numero_serie__icontains=query) #recherche par numero serie
        )

    else:
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
    return render (request, 'gestion/supprimer_ascenseur.html', {'form': form, 'ascenseur': ascenseur})
        

#Rapport en excel
def rapport_ascenseurs_excel(request):
    #creation du fichier excel
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Rapport des ascenseurs"

    #En-tete
    headers = ["Client","Marque","Modèle","Numero de Série","Date d'installaion"]
    ws.append(headers)

    #données des ascenseurs
    ascenseurs = Ascenseur.object.all()
    for ascenseur in ascenseurs:
        ws.append([
            ascenseur.client.nom if ascenseur.client else "",
            ascenseur.marque,
            ascenseur.modele,
            ascenseur.numero_serie,
            ascenseur.date_installation.strftime('%d-%m-%Y') if ascenseur.date_installation else ""
        ])
    # Envoi de la reponse
    response =HttpResponse(content_type="application/vnd.openpyxmlformats-officedocument.spreadsheetml.sheet")
    response['Conten_Disposition']= 'attachment;filename="Rapport_ascenseur.xlsx"'
    wb.save(response)
    return response
