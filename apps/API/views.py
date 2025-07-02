from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from apps.users import models
from .models import del_token, validate_token

# Create your views here.
@csrf_exempt
def new_user(request):
    """
        Endpoint to create a new user in the database
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError as e:
            return JsonResponse({'message': str(e)})
        
        username = data.get('username')
        name = data.get('name')
        last_name = data.get('last_name')
        email = data.get("email")
        passw = data.get("pass")
        position = data.get("position")
        result = models.insert_users(username, name, last_name, email, passw, position)
        
        # if other user exists returns 409
        if not result['success']:
            return JsonResponse({'message': 'Existing user'}, status=409)
        
        # Return 201 if the user if succesfully created and inmediatly validates him
        context = JsonResponse({'message': 'User created succesfully'}, status=201)
        validate_user(request)
        
        return context
    
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)

@csrf_exempt
def validate_user(request):
    """
        Endpoint to validate if the user exist in the database
        and allow sign in
    """
    if request.method != "POST":
        return JsonResponse({"message": "Method not allowed"}, status=405)
    
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"message": "Invalid JSON"})

    username = data.get("username")
    passw = data.get("pass")

    # Get the user ID
    user_id = models.get_id(username)
    if not user_id or not user_id.get("user_id"):
        return JsonResponse({"message": "User does not exist"}, status=404)

    # Validates if the user has already a token
    signed = validate_token(user_id["user_id"])
    if signed["success"] == True:
        return JsonResponse({"message": "User already logged"}, status=409)
    
    # Validates the credentials of the user
    result = models.valid_user(username, passw)
    if result.get("error"):
        return JsonResponse({"message": result["error"]}, status=500)
    elif not result["success"]:
        return JsonResponse({"message": "Invalid credentials"}, status=401)
    

    return JsonResponse({"success": True, "message": "valid credentials", "token": result["token"]}, status=200)

@csrf_exempt
def logout_user(request):
    """
        Endpoint to close the active session
    """
    if request.method != 'DELETE':
        return JsonResponse({"message": "Method not allowed"}, status=405)
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError as e:
        return {"message": e}

    if not "token" in data:
        return JsonResponse({"message": "JSON body error"})

    token = data.get("token")
    result = del_token(token)
    
    if result.get("error"):
        return JsonResponse({"message": result["error"]}, status=500)
    
    elif not result["success"]:
        return JsonResponse({"message": result["message"]}, status=400)
    
    return JsonResponse({"message": result["message"]}, status=200)

@csrf_exempt
def del_user(request):
    """
        Endpoint to delete a user of the database
    """
    if request.method != 'DELETE':
        return JsonResponse({"message": "method not allowed"}, status=405)

    try:
        data = json.loads(request.body)
    except json.JSONDecodeError as e:
        return JsonResponse({"message": str(e)}, status=400)
    
    user_id = data.get("user_id")
    result = models.del_user(user_id)
    if result.get("error") == True:
        return JsonResponse({"message": result["error"]}, status=500)
    
    elif not result["success"]:
        return JsonResponse({"message": result["message"]}, status=400)
    
    return JsonResponse({"message": result["message"]}, status=200)
