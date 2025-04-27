from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Tree
import json


@csrf_exempt
def tree_list(request):
    if request.method == "GET":
        trees = Tree.objects.all()
        data = list(trees.values())
        return JsonResponse({"trees": data})

    elif request.method == "POST":
        data = json.loads(request.body)
        tree = Tree.objects.create(**data)
        return JsonResponse({"message": "Tree created successfully"}, status=201)


@csrf_exempt
def tree_detail(request, pk):
    try:
        tree = Tree.objects.get(pk=pk)
    except Tree.DoesNotExist:
        return JsonResponse({"error": "Tree not found"}, status=404)

    if request.method == "GET":
        data = {
            "id": tree.id,
            "name": tree.name,
            "species": tree.species,
            "location": tree.location,
            "planted_date": tree.planted_date,
            "height": tree.height,
            "health_status": tree.health_status,
        }
        return JsonResponse(data)


from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile
import json


@csrf_exempt
def register(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_form = UserCreationForm(
                {
                    "username": data.get("username"),
                    "password1": data.get("password"),
                    "password2": data.get("password"),
                }
            )

            if user_form.is_valid():
                user = user_form.save()
                # 创建用户档案
                UserProfile.objects.create(
                    user=user,
                    phone=data.get("phone", ""),
                    address=data.get("address", ""),
                )
                return JsonResponse({"status": "success", "message": "注册成功"})
            else:
                return JsonResponse(
                    {"status": "error", "message": user_form.errors}, status=400
                )
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)


@csrf_exempt
def login_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return JsonResponse({"status": "success", "message": "登录成功"})
            else:
                return JsonResponse(
                    {"status": "error", "message": "用户名或密码错误"}, status=400
                )
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
