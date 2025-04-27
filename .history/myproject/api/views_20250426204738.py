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
