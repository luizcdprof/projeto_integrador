from django.shortcuts import render, HttpResponse
#home
def home(request):
    return HttpResponse('Bem-vindo ao Product')

#Product
def register_product(request):
    return HttpResponse('Mensagem: Registrar produto')

def list_product(request, id):
    return HttpResponse(f'Listar produto com ID: {id}')

def update_product(request, id):
    return HttpResponse(f'Atualizar produto com ID: {id}')

def delete_product(request, id):
    return HttpResponse(f'Excluir produto com ID: {id}')
