from django.shortcuts import render, redirect
from .models import Artist, Installation, Venue, Edition






# Create your views here.

#creación
def artist_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        country = request.POST.get('country')
        short_bio = request.POST.get('short_bio')
        website = request.POST.get('website')
        #crear objeto
        artist = Artist(name=name, country=country, short_bio=short_bio, website=website)
        artist.save()
        
        #esto lo que permite es que si recargo la página, se vuelve a enviar el POST y se crea el artista otra vez.
        return redirect(request, 'artist_create.html', {'artist': artist})
    else:
        return render(request, 'artist_create.html')


# Artist: Listado de artistas
def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'artist_list.html', {'artists': artists})

#detalle incluyendo obras
def artist_detail(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    return render(request, 'artist_detail.html', {'artist': artist})

#edición
def artist_edit(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    if request.method == 'POST':
        artist.name = request.POST.get('name')
        artist.country = request.POST.get('country')
        artist.short_bio = request.POST.get('short_bio')
        artist.website = request.POST.get('website')
        artist.save()
        return redirect('artist_detail', artist_id=artist.id)
    else:
        return render(request, 'artist_edit.html', {'artist': artist})
    
#borrado
def artist_delete(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    artist.delete()
    return redirect('artist_list')

#filtrado por pais
def artist_list_by_country(request, country):
    artists = Artist.objects.filter(country=country)
    return render(request, 'artist_list.html', {'artists': artists})

#INSTALLATION

#listado
def installation_list(request):
    installations = Installation.objects.all()
    return render(request, 'installation_list.html', {'installations': installations})

#detalle incluyendo autor
def installation_detail(request, installation_id):
    installation = Installation.objects.get(id=installation_id)
    return render(request, 'installation_detail.html', {'installation': installation})

#creacion
def installation_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        opening_date = request.POST.get('opening_date')
        short_description = request.POST.get('short_description')
        materials = request.POST.get('materials')
        artist_id = request.POST.get('artist')
        venue_id = request.POST.get('venue')
        edition_id = request.POST.get('edition')
        artist = Artist.objects.get(id=artist_id)
        venue = Venue.objects.get(id=venue_id)
        edition = Edition.objects.get(id=edition_id)
        installation = Installation(title=title, opening_date=opening_date, short_description=short_description, materials=materials, artist=artist, venue=venue, edition=edition)
        installation.save()
        return redirect('installation_detail', installation_id=installation.id)
    else:
        artists = Artist.objects.all()
        venues = Venue.objects.all()
        editions = Edition.objects.all()
        return render(request, 'installation_create.html', {'artists': artists, 'venues': venues, 'editions': editions})    
    
#filtrado por edicion
def installation_list_by_edition(request, edition_id):
    installations = Installation.objects.filter(edition_id=edition_id)
    return render(request, 'installation_list.html', {'installations': installations})


#Ordenar por fecha de inauguración (de forma ascendente o descendente).
def installation_list_by_opening_date(request, order):
    installations = Installation.objects.order_by('opening_date' if order == 'asc' else '-opening_date')
    return render(request, 'installation_list.html', {'installations': installations})

#VENUE

#listado
def venue_list(request):
    venues = Venue.objects.all()
    return render(request, 'venue_list.html', {'venues': venues})

#detalle incluyendo obras
def venue_detail(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    return render(request, 'venue_detail.html', {'venue': venue})

#creacion
def venue_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        description = request.POST.get('description')
        max_capacity = request.POST.get('max_capacity')
        venue = Venue(name=name, address=address, description=description, max_capacity=max_capacity)
        venue.save()
        return redirect('venue_detail', venue_id=venue.id)
    else:
        return render(request, 'venue_create.html')
    
#EDICCIÓN

#listado
def edition_list(request):
    editions = Edition.objects.all()
    return render(request, 'edition_list.html', {'editions': editions})

#detalle incluyendo obras
def edition_detail(request, edition_id):
    edition = Edition.objects.get(id=edition_id)
    return render(request, 'edition_detail.html', {'edition': edition})

#creacion
def edition_create(request):
    if request.method == 'POST':
        year = request.POST.get('year')
        theme = request.POST.get('theme')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        edition = Edition(year=year, theme=theme, start_date=start_date, end_date=end_date)
        edition.save()
        return redirect('edition_detail', edition_id=edition.id)
    else:
        return render(request, 'edition_create.html')
    
    
#PAGINA DE INICIO

def home(request):
    return render(request, 'index.html')


