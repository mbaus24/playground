from django.shortcuts import render, get_object_or_404, redirect
from .models import Character, Equipement
from .forms import MoveForm
from random import randint


# Create your views here.
def character_list(request):
        character = Character.objects.order_by('code')
        return render(request, 'blog/character_list.html', {'character': character})

def equipement_list(request):
        equipement = Equipement.objects.order_by('id_equip')
        occupants = Character.objects.filter(lieu="parc_aquatique")
        occupants_names = ", ".join([o.id_character for o in occupants])
        
        message = f"Le lieu est occupé par {occupants_names}"
        return render(request, 'blog/equipement_list.html', {'equipement': equipement, 'message': message})
    
def character_detail(request, id_character):
    character = get_object_or_404(Character, id_character=id_character)
    ancien_lieu = get_object_or_404(Equipement, id_equip=character.lieu.id_equip)
    
    characters_dans_lieu = Character.objects.filter(lieu=ancien_lieu)
    if request.method == "POST":
        form = MoveForm(request.POST, instance=character)
        if form.is_valid():
            form.save(commit="False")
            nouveau_lieu = get_object_or_404(Equipement, id_equip=character.lieu.id_equip)
            if nouveau_lieu == ancien_lieu:
                message = f"{character.id_character} est déjà dans ce lieu"
                return render(request, 'blog/character_detail.html', {'character': character, 'lieu': character.lieu, 'form': form, 'message': message, 'characters_dans_lieu': characters_dans_lieu})
            print("nouveau_lieu : ", nouveau_lieu)

            if nouveau_lieu.disponibilite == "libre":
                print("nouveau lieu est bien libre")
                nombre_lieu = Character.objects.filter(lieu=nouveau_lieu).count()
                
                

                
                
                # Recherche taille nouveau lieu
                if nombre_lieu > nouveau_lieu.taille_max - 1: # On regarde si le lieu se remplit (en comptant le nouveau personnage)
                    print("on est dans le if")
                    nouveau_lieu.disponibilite = "occupe"
                nouveau_lieu.save()
                ancien_lieu.disponibilite = "libre"
                ancien_lieu.save()

                # si il est normal et dans le parc aquatique
                print("nouveau_lieu : " + nouveau_lieu.id_equip)
                if nouveau_lieu.id_equip == "parc_aquatique" and character.etat == "normal":
                    if randint(0, 1):
                        character.etat = "fatigue"
                    else:
                        character.etat = "blesse"
                    character.save()
                    
                 # si il est affame et dans la mangeoire
                print("nouveau_lieu : " + nouveau_lieu.id_equip)
                if nouveau_lieu.id_equip == "mangeoire" and character.etat == "affame":
                    if randint(0, 1):
                        character.etat = "fatigue"
                    else:
                        character.etat = "blesse"
                    character.save()


                # si il est fatigué et dans le lit
                elif nouveau_lieu.id_equip == "lit" and character.etat == "fatigue":
                    character.etat = "affame"
                    character.save()

                # si il est blessé et dans l'infirmerie
                elif nouveau_lieu.id_equip == "infiermerie" and character.etat == "blesse":
                    character.etat = "affame"
                    character.save()
                elif nouveau_lieu.id_equip == "mangeoire" and character.etat == "affame":
                    character.etat = "normal"
                    character.save()

            else:
                character.lieu = ancien_lieu
                character.save()
                occupants = Character.objects.filter(lieu=nouveau_lieu)
                occupants_names = ", ".join([o.id_character for o in occupants])
                print(occupants_names)
                message = f"Le lieu est déjà occupé par {occupants_names}"
                return render(request, 'blog/character_detail.html', {'character': character, 'lieu': character.lieu, 'form': form, 'message': message, 'characters_dans_lieu': characters_dans_lieu})
                

                
            return redirect('character_detail', id_character=id_character)
    
    else:
        form = MoveForm()
        return render(request,
                    'blog/character_detail.html',
                    {'character': character, 'lieu': character.lieu, 'form': form, 'characters_dans_lieu': characters_dans_lieu})
    