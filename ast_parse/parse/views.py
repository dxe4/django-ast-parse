import json
from django.shortcuts import render
from django.http import HttpResponse
# from django.views.generic import View
from ast_parse.parse.utils import get_files


def all_modules(requset, is_json=None):
    code_base = get_files()
    data = dict(files=code_base.file_dict)

    if is_json:
        return HttpResponse(json.dumps(data),
                            content_type="application/json")
    else:
        return render(requset, 'all_modules.html', {})
