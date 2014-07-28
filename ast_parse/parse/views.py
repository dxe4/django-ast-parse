'''
TODO refactor is_json to output to allow xml?
'''
import json
from django.shortcuts import render
from django.http import HttpResponse, Http404
# from django.views.generic import View
from ast_parse.parse.models import NotFound
from ast_parse.parse.utils import get_files


def all_modules(requset, is_json=None):
    code_base = get_files()
    data = dict(modules=code_base.sub_dirs)

    if is_json:
        return HttpResponse(json.dumps(data),
                            content_type="application/json")
    else:
        return render(requset, 'all_modules.html', data)


def module(request, path, is_json=None):
    '''
    path: example -> django/http
    '''
    code_base = get_files()
    try:
        files = code_base.list_files(path)
        print(files)
    except NotFound:
        raise Http404('Not found {}'.format(path))

    return render(request, 'module.html', {})
