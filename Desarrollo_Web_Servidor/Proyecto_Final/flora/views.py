import json
from django.shortcuts import render, redirect
from .models import Artist, Installation, Venue, Edition
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Creación de artista
def artist_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        country = request.POST.get('country')
        short_bio = request.POST.get('short_bio')
        website = request.POST.get('website')

        # Crear objeto Artist
        artist = Artist(
            name=name,
            country=country,
            short_bio=short_bio,
            website=website
        )
        artist.save()

        messages.success(request, 'Artista creado correctamente.')
        return redirect('artist_list')
    else:
        return render(request, 'artist_create.html')



# Artist: Listado de artistas
def artist_list(request):
    country = request.GET.get('country', '').strip()
    if country:
        artists = Artist.objects.filter(country__icontains=country)
    else:
        artists = Artist.objects.all()
    return render(request, 'artist_list.html', {'artists': artists, 'country': country})

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
        # Mensaje de éxito
        messages.success(request, 'Artista editado correctamente.')

        # Redirigir al listado de artistas
        return redirect('artist_list')
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
    data = []
    for inst in installations:
        data.append({
            "id": inst.id,
            "title": inst.title,
            "opening_date": inst.opening_date.strftime("%Y-%m-%d"),
            "short_description": inst.short_description,
            "materials": inst.materials,
            "artist": {
                "id": inst.artist.id,
                "name": inst.artist.name
            },
            "venue": {
                "id": inst.venue.id,
                "name": inst.venue.name
            },
            "edition": {
                "id": inst.edition.id,
                "year": inst.edition.year,
                "theme": inst.edition.theme
            }
        })

    return JsonResponse(data, safe=False)

#detalle incluyendo autor
def installation_detail(request, installation_id):
    installation = Installation.objects.get(id=installation_id)
    return render(request, 'installation_detail.html', {'installation': installation})

#creacion
@csrf_exempt
def installation_create(request):
    if request.method == 'POST':
        try:
            # Asumiendo que Bruno envía JSON
            data = json.loads(request.body)
            title = data.get('title')
            opening_date = data.get('opening_date')
            short_description = data.get('short_description')
            materials = data.get('materials')
            artist_id = data.get('artist')
            venue_id = data.get('venue')
            edition_id = data.get('edition')

            artist = Artist.objects.get(id=artist_id)
            venue = Venue.objects.get(id=venue_id)
            edition = Edition.objects.get(id=edition_id)

            installation = Installation(
                title=title,
                opening_date=opening_date,
                short_description=short_description,
                materials=materials,
                artist=artist,
                venue=venue,
                edition=edition
            )
            installation.save()

            # Devolver JSON con los datos creados
            return JsonResponse({
                "id": installation.id,
                "title": installation.title,
                "artist": installation.artist.name,
                "venue": installation.venue.name,
                "edition": {
                    "id": edition.id,
                    "year": edition.year,
                    "theme": edition.theme
                }
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)  
    
#filtrado por edicion
def installation_list_by_edition(request, edition_id):
    installations = Installation.objects.filter(edition_id=edition_id)
    data = []
    for inst in installations:
        data.append({
            "id": inst.id,
            "title": inst.title,
            "opening_date": inst.opening_date.strftime("%Y-%m-%d"),
            "short_description": inst.short_description,
            "materials": inst.materials,
            "artist": {
                "id": inst.artist.id,
                "name": inst.artist.name
            },
            "venue": {
                "id": inst.venue.id,
                "name": inst.venue.name
            },
            "edition": {
                "id": inst.edition.id,
                "year": inst.edition.year,
                "theme": inst.edition.theme
            }
        })

    return JsonResponse(data, safe=False)


#Ordenar por fecha de inauguración (de forma ascendente o descendente).
def installation_list_by_opening_date(request, order):
    installations = Installation.objects.order_by('opening_date' if order == 'asc' else '-opening_date')
    data = []
    for inst in installations:
        data.append({
            "id": inst.id,
            "title": inst.title,
            "opening_date": inst.opening_date.strftime("%Y-%m-%d"),
            "short_description": inst.short_description,
            "materials": inst.materials,
            "artist": {
                "id": inst.artist.id,
                "name": inst.artist.name
            },
            "venue": {
                "id": inst.venue.id,
                "name": inst.venue.name
            },
            "edition": {
                "id": inst.edition.id,
                "year": inst.edition.year,
                "theme": inst.edition.theme
            }
        })

    return JsonResponse(data, safe=False)


#VENUE

#listado
def venue_list(request):
    venues = Venue.objects.all()
    data = []
    for venue in venues:
        data.append({
            "id": venue.id,
            "name": venue.name,
            "address": venue.address,
            "description": venue.description,
            "max_capacity": venue.max_capacity
        })

    return JsonResponse(data, safe=False)


#detalle incluyendo obras
def venue_detail(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    try:
        venue = Venue.objects.get(id=venue_id)
        data = {
            "id": venue.id,
            "name": venue.name,
            "address": venue.address,
            "description": venue.description,
            "max_capacity": venue.max_capacity
        }
        return JsonResponse(data)
    except Venue.DoesNotExist:
        return JsonResponse({"error": "Venue not found"}, status=404)

@csrf_exempt
#creacion
def venue_create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        address = data.get('address')
        description = data.get('description')
        max_capacity = data.get('max_capacity')
        venue = Venue(name=name, address=address, description=description, max_capacity=max_capacity)
        venue.save()
        return JsonResponse({'id': venue.id, 'name': venue.name})
    
#EDICIÓN

#listado
def edition_list(request):
    editions = Edition.objects.all()
    data = []
    for edition in editions:
        data.append({
            "id": edition.id,
            "year": edition.year,
            "theme": edition.theme,
            "start_date": edition.start_date,
            "end_date": edition.end_date
        })

    return JsonResponse(data, safe=False)

#detalle incluyendo obras
def edition_detail(request, edition_id):
    try:
        edition = Edition.objects.get(id=edition_id)
        data = {
            "id": edition.id,
            "year": edition.year,
            "theme": edition.theme,
            "start_date": edition.start_date,
            "end_date": edition.end_date
        }
        return JsonResponse(data)
    except Edition.DoesNotExist:
        return JsonResponse({"error": "Edition not found"}, status=404)

#creacion
@csrf_exempt
def edition_create(request):
    if request.method == 'POST':
        try:
            # Leer JSON desde el body
            data = json.loads(request.body)
            year = data.get('year')
            theme = data.get('theme')
            start_date = data.get('start_date')
            end_date = data.get('end_date')

            edition = Edition(
                year=year,
                theme=theme,
                start_date=start_date,
                end_date=end_date
            )
            edition.save()

            return JsonResponse({
                "id": edition.id,
                "year": edition.year,
                "theme": edition.theme,
                "start_date": edition.start_date,
                "end_date": edition.end_date
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
        
#PAGINA DE INICIO

def home(request):
    return render(request, 'index.html')


