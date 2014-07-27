import json
from django.shortcuts import render
from django.http import HttpResponse
# from django.views.generic import View
from ast_parse.parse.utils import get_files


def all_modules(requset, is_json=None):
    files = list(get_files())
    data = dict(files=files)

    if is_json:
        return HttpResponse(json.dumps(data),
                            content_type="application/json")
    else:
        return render(requset, 'all_modules.html', {})
