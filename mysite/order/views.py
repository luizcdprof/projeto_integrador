from django.shortcuts import render, HttpResponse
#Home
def home(request):
    return HttpResponse('Bem-vindo ao Orders')

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
