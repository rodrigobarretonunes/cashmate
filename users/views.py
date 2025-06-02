from django.shortcuts import render,redirect
from django.http import request 
from django.contrib.auth.models import User
from .models import Profiles



#Renderiza pagina de perfis e responsavel pela logica de redirecionar pra rota de criação de perfil 
def profile (request):
    context = {}
    
    if request.method == 'GET':
        profiles = Profiles.objects.filter(account_id_id=request.user.id)
        print("Perfis encontrados:", list(profiles.values('user', 'email', 'avatar','id')))
        print("ID do usuário logado:", request.user.id)

        return render(request, 'profiles.html', {'profiles': profiles})
        


       
    elif request.method == 'POST':
        user = request.POST.get('profile_name','').strip().upper()
        email = request.POST.get('profile_email','').strip().upper()
        avatar = request.POST.get('avatar_img','').strip()

        user_exists = Profiles.objects.filter(user = user).exists()
        email_exists = Profiles.objects.filter(email = email).exists()
        empty_post = [user,email,avatar]
        
        if user_exists or email_exists:
            if email_exists and user_exists:
                context['error message'] = 'Username and email are already in use.'
            elif email_exists:
                context['error message'] = 'Username is already in use.'
                    
            else:
                context['error message'] = 'Email is already in use.'
            profiles = Profiles.objects.filter(account_id_id = request.user.id)
            context['profiles'] = Profiles.objects.filter(account_id_id = request.user.id)
            return render (request,'profiles.html',context)
        
        else:
            profile = Profiles(account_id = request.user,user = user, email = email,avatar = avatar)
            profile.save()
            context['success_message'] = "Perfil criado com sucesso!"
            context['profiles'] = Profiles.objects.filter(account_id_id = request.user.id)
            return render (request,'profiles.html',context)



        




        
