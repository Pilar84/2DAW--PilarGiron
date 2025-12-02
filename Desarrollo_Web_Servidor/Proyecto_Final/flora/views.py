from django.shortcuts import render, redirect
from django.http import Artist  




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
