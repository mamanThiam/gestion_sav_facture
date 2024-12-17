from django.shortcuts import render,get_object_or_404, redirect
from .models import Client
from .forms import ClientForm
from django.http import HttpResponse

# liste des clients
def liste_clients(request):
    clients = Client.objects.all()
    return render (request, 'gestion/liste_clients.html')



# Formulaire pour ajouter ou modifier clients

def formulaire_client(request, id=None):
    if id:
        client = get_object_or_404(Client, id=id)
    else:
        client = None
    

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('liste_clients')
    else:
       form = ClientForm(instance = client)

    return render(request, 'gestion/formulaire_client.html', {'form': form})

    