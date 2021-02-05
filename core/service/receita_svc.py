from core.models import Receita

def lista_receitas():
    receita = Receita.objects.all()
    return receita

def umareceita(nome):
    receita = Receita.objects.get(nome = nome)
    return receita

def add_receita(receita, introducao, ingredientes, preparo, autor, foto):
    receita = Receita.objects.create(receita=receita, introducao=introducao, ingredientes=ingredientes, preparo=preparo, autor=autor, foto=foto)
    return receita.to_dict_json()