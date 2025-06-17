from django.shortcuts import render,redirect
from django.http import request 
from django.contrib.auth.models import User
from .models import Profiles




# Returns all profiles associated with the currently logged-in user's account
def get_user_profiles(request):
    return Profiles.objects.filter(account_id_id = request.user.id)


# Retrieves username, email, and avatar from the POST data if all are present
def get_user_data(request):
        username = request.POST.get('profile_name','').strip().upper()
        email = request.POST.get('profile_email','').strip().upper()
        avatar = request.POST.get('avatar_img','').strip()
        if username and email and avatar:
            return username,email,avatar
        else:
            return None


# Checks if the given username or email is already in use by another profile
def is_duplicated_profile(username,email):
    context = {}
    user_exists = Profiles.objects.filter(user = username).exists()
    email_exists = Profiles.objects.filter(email = email).exists()
    if user_exists or email_exists:
        if user_exists and email_exists:
            context['error_message'] = 'Username and email are already in use.'
            return True,context
        elif user_exists:
            context['error_message'] = 'Username is already in use.'
            return True,context
        else:
            context['error_message'] = 'Email is already in use.'
            return True,context
    else:
        return False, None


# Creates and saves a new profile linked to the given user account with username, email, and avatar
def create_profile(user_obj, username, email, avatar):
    profile = Profiles.objects.create(
        account_id=user_obj,
        user=username,
        email=email,
        avatar=avatar)
    return profile


# Handles GET requests by retrieving all profiles for the logged-in user and rendering the profiles page
def handle_get_request(request):
    profiles = get_user_profiles(request)
    return render(request,'profiles.html', {'profiles': profiles})


# Processes POST data to create a new profile, checking for duplicates and returning success or error messages
def handle_post_request(request):
    context = {}
    username,email,avatar = get_user_data(request)
    verify_duplicated_profile, context['error_message'] =  is_duplicated_profile(username,email)
    if verify_duplicated_profile:
        return render (request,'profiles.html',context)

    else:
        create_profile(user_obj = request.user, username = username,email = email, avatar = avatar)
        context['success_message'] = "Profile created successfully!"
        context['profiles'] = get_user_profiles(request)
        return render(request,'profiles.html',context)
    

def delete_profile(request):
    profile_id = request.POST.get('profile_id')

    if profile_id:
        Profiles.objects.filter(id=profile_id).delete()

    return redirect('profile')
    


# Routes GET and POST requests to their respective handlers for profile management
def profile(request):
    if request.method == 'GET':   
     return handle_get_request(request)
    
    elif request.method == 'POST':
        action = request.POST.get('action')
        if action == 'create':
            return handle_post_request(request)
        elif action == 'delete':
            return delete_profile(request)
        return handle_post_request(request)
    