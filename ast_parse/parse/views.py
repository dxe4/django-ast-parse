# from django.shortcuts import render
import json
from django.http import HttpResponse
from ast_parse.utils import get_files


def all_modules(requset):
    files = list(get_files())
    data = {
        'files': files,
    }
    return HttpResponse(json.dumps(data),
                        content_type="application/json")
