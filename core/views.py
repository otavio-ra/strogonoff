# coding: utf-8
import json
from django.http.response import HttpResponse, JsonResponse
from django.contrib import auth
from commons.django_model_utils import get_or_none
from commons.django_views_utils import ajax_login_required
from core.service import log_svc, todo_svc, receita_svc
from django.views.decorators.csrf import csrf_exempt


def dapau(request):
    raise Exception('break on purpose')


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    user_dict = None
    if user is not None:
        if user.is_active:
            auth.login(request, user)
            log_svc.log_login(request.user)
            user_dict = _user2dict(user)
    return JsonResponse(user_dict, safe=False)


def logout(request):
    if request.method.lower() != 'post':
        raise Exception('Logout only via post')
    if request.user.is_authenticated():
        log_svc.log_logout(request.user)
    auth.logout(request)
    return HttpResponse('{}', content_type='application/json')


def whoami(request):
    i_am = {
        'user': _user2dict(request.user),
        'authenticated': True,
    } if request.user.is_authenticated() else {'authenticated': False}
    return JsonResponse(i_am)

def list_receita(request):
    lista = list(receita_svc.lista_receitas())
    lista_vazia = []
    for i in lista:
        lista_vazia.append(i.to_dict_json())
    return JsonResponse(lista_vazia, safe=False)

def receita(request, nome):
    lista = receita_svc.umareceita(nome)
    return JsonResponse(lista.to_dict_json(), safe=False)


@ajax_login_required
def add_todo(request):
    todo = todo_svc.add_todo(request.POST['new_task'])
    return JsonResponse(todo)


@ajax_login_required
def list_todos(request):
    todos = todo_svc.list_todos()
    return JsonResponse({'todos': todos})

def createReceita(request):
    receita = request.POST['receita']
    introducao = request.POST['introducao']
    ingredientes = request.POST['ingredientes']
    preparo = request.POST['preparo']
    autor = request.POST['autor']
    foto = request.FILES['foto']
    prato = receita_svc.add_receita(
        receita = receita,
        introducao = introducao,
        ingredientes=ingredientes,
        preparo=preparo,
        autor=autor,
        foto=foto)
    return JsonResponse(prato, safe=False)

def _user2dict(user):
    d = {
        'id': user.id,
        'name': user.get_full_name(),
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'permissions': {
            'ADMIN': user.is_superuser,
            'STAFF': user.is_staff,
        }
    }
    return d