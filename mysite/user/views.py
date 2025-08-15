from django.shortcuts import render, HttpResponse

#Profile
def register_profile(request):
    return HttpResponse('Mensagem: Registrar usuário e perfil')

def list_profile(request, id):
    return HttpResponse(f'perfil_id:  {id}')

def update_profile(request, id):
    return HttpResponse(f'Listar perfil com ID {id}')

def delete_profile(request, id):
    return HttpResponse(f'Excluir perfil com ID {id}')
