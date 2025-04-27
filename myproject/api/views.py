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


from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User  # 如果使用默认用户模型
# from api.models import User  # 如果使用自定义用户模型
import json

@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            email = data.get('email', '')
            
            # 检查用户名是否已存在
            if User.objects.filter(username=username).exists():
                return JsonResponse({'status': 'error', 'message': '用户名已存在'}, status=400)
            
            # 创建新用户
            user = User.objects.create_user(username=username, password=password, email=email)
            
            return JsonResponse({'status': 'success', 'message': '注册成功'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    
    return JsonResponse({'status': 'error', 'message': '仅支持 POST 请求'}, status=405)

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            
            # 验证用户
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return JsonResponse({'status': 'success', 'message': '登录成功'})
            else:
                return JsonResponse({'status': 'error', 'message': '用户名或密码错误'}, status=401)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    
    return JsonResponse({'status': 'error', 'message': '仅支持 POST 请求'}, status=405)
