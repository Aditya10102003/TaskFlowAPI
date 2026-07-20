from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "TaskFlow API is running successfully 🚀",
        "author": "Aditya Yadav",
        "endpoints": {
            "register": "/api/register/",
            "login": "/api/login/",
            "refresh": "/api/token/refresh/",
            "tasks": "/api/tasks/"
        }
    })