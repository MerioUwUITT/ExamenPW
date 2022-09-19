from django.shortcuts import render,redirect

from .forms import TeamForm
from .forms import PlayerForm
from .forms import StadiumForm
from .models import Player
from .models import Team
from .models import Stadium
# Create your views here.
def menu(request):
    return render(request, "player_register/menu.html")
def player_list(request):
    context = {'player_list': Player.objects.all()}
    return render(request, "player_register/player_list.html",context)


def player_form(request,id=0):
    if request.method == "GET":
        if id == 0:
             form = PlayerForm()
        else:
            player = Player.objects.get(pk=id)
            form = PlayerForm(instance=player)
        jls_extract_var = 'form'
        return render(request, "player_register/player_form.html", {jls_extract_var:form})
    else:
        if id == 0:
            form = PlayerForm(request.POST)
        else:
            player = Player.objects.get(pk=id)
            form = PlayerForm(request.POST,instance=player)
        if form.is_valid():
            form.save()
        return redirect('/PNLF/listP')



def player_delete(request,id):
    player = Player.objects.get(pk=id)
    player.delete()
    return redirect('/PNLF/listP')
 
def team_list(request):
    context = {'team_list': Team.objects.all()}
    return render(request, "player_register/team_list.html",context)
def team_form(request,id=0):
    if request.method == "GET":
        if id == 0:
             form = TeamForm()
        else:
            team = Team.objects.get(pk=id)
            form = TeamForm(instance=team)
        jls_extract_var = 'form'
        return render(request, "player_register/team_form.html", {jls_extract_var:form})
    else:
        if id == 0:
            form = TeamForm(request.POST)
        else:
            team = Team.objects.get(pk=id)
            form = TeamForm(request.POST,instance=team)
        if form.is_valid():
            form.save()
        return redirect('/PNLF/listT')
def team_delete(request,id):
    team = Team.objects.get(pk=id)
    team.delete()
    return redirect('/PNLF/listT')

def stadium_list(request):
    context = {'stadium_list': Stadium.objects.all()}
    return render(request, "player_register/stadium_list.html",context)

def stadium_form(request,id=0):
    if request.method == "GET":
        if id == 0:
             form = StadiumForm()
        else:
            stadium = Stadium.objects.get(pk=id)
            form = StadiumForm(instance=stadium)
        jls_extract_var = 'form'
        return render(request, "player_register/stadium_form.html", {jls_extract_var:form})
    else:
        if id == 0:
            form = StadiumForm(request.POST)
        else:
            stadium = Stadium.objects.get(pk=id)
            form = StadiumForm(request.POST,instance=stadium)
        if form.is_valid():
            form.save()
        return redirect('/PNLF/listS/')
    
def stadium_delete(request,id):
    stadium = Stadium.objects.get(pk=id)
    stadium.delete()
    return redirect('/PNLF/listS')
    
