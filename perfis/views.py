from django.shortcuts import render
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html')

def exibir(request, perfil_id):

	perfil = Perfil()

	if perfil_id == '1':
		perfil = Perfil('Flavio Almeida', 'flavio@flavio.com.br', '777777777', 'Caelum')

	if perfil_id == '2':
		perfil = Perfil('Romulo henrique', 'romulo@romulo.com.br', '88888888', 'Caelum')

	return render(request, 'perfil.html', {"perfil" : perfil})