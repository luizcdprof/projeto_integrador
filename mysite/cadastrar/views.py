from django.shortcuts import render, HttpResponse
#Home
def home(request):
    return HttpResponse('Bem-vindo ao Cadastro')

#Profile
def register_profile(request):
    return HttpResponse('Mensagem: Registrar usuário e perfil')

def list_profile(request, id):
    return HttpResponse(f'perfil_id:  {id}')

def update_profile(request, id):
    return HttpResponse(f'Listar perfil com ID {id}')

def delete_profile(request, id):
    return HttpResponse(f'Excluir perfil com ID {id}')

#Product
def register_product(request):
    return HttpResponse('Mensagem: Registrar produto')

def list_product(request, id):
    return HttpResponse(f'Listar produto com ID: {id}')

def update_product(request, id):
    return HttpResponse(f'Atualizar produto com ID: {id}')

def delete_product(request, id):
    return HttpResponse(f'Excluir produto com ID: {id}')

#Order

def register_order(request):
    return HttpResponse('Mensagem: Registrar pedido')

def create_order(request):
    return HttpResponse('Mensagem: Criar pedido')

def list_order_by_id(request, id):
    return HttpResponse(f'Listar pedido com ID: {id}')

def list_order(request):
    return HttpResponse('Listar todos os pedidos')

def update_order(request, id):
    return HttpResponse(f'Atualizar pedido com ID: {id}')

def delete_order(request, id):
    return HttpResponse(f'Excluir pedido com ID: {id}')

def add_item_order(request, id):
    return HttpResponse(f'Adicionar item ao pedido com ID: {id}')

def remove_item_order(request, id):
    return HttpResponse(f'Remover item do pedido com ID: {id}')