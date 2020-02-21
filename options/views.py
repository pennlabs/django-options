from django.http import JsonResponse

from options.models import Option


def option_json(request):
    if request.method == "GET":
        options = Option.objects.all()
        option_list = []
        for o in options:
            option_list.append({"key": o.key, "value": o.value})
        return JsonResponse({"Status": 200, "Options": option_list})

    else:
        return JsonResponse({"Status": 405, "Error": "Only GET requests allowed."}, status=405)
