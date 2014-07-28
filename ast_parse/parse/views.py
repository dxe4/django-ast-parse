'''
TODO refactor is_json to output to allow xml?
'''
import json
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import View
from ast_parse.parse.models import NotFound
from ast_parse.parse.utils import get_files


class JsonOrHtmlView(View):

    def _response(self, request, context, is_json):
        if is_json:
            return HttpResponse(json.dumps(context),
                                content_type="application/json")
        else:
            return render(request, 'all_modules.html', context)


class AllModulesView(JsonOrHtmlView):
    template_name = 'all_modules.html'

    def get(self, request, is_json=None):
        code_base = get_files()
        data = dict(modules=code_base.sub_dirs)
        return self._response(request, data, is_json)


class ModuleView(JsonOrHtmlView):
    template_name = 'module.html'

    def get(self, request, path, is_json=None):
        '''
        path: example -> django/http
        '''
        code_base = get_files()
        try:
            files = code_base.list_files(path)
        except NotFound:
            raise Http404('Not found {}'.format(path))

        return self._response(request, {}, is_json)

all_modules = AllModulesView.as_view()
module = ModuleView.as_view()
