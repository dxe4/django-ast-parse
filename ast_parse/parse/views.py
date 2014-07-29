'''
TODO refactor is_json to output to allow xml?
'''
import json
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import View
from django.conf import settings
from ast_parse.parse.models import NotFound
from ast_parse.parse.utils import get_files


class JsonOrHtmlView(View):

    def _response(self, request, context, is_json):
        if is_json:
            return HttpResponse(json.dumps(context),
                                content_type="application/json")
        else:
            return render(request, self.template_name, context)


class AllPackagesView(JsonOrHtmlView):
    template_name = 'all_packages.html'

    def get(self, request, is_json=None):
        redis_con = settings.REDIS_POOL.get_connection(
            self.__class__.__name__)

        packages = redis_con.smembers('packages')
        data = dict(packages=packages)
        return self._response(request, data, is_json)


class PackageView(JsonOrHtmlView):
    template_name = 'package.html'

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


class ModuleView(JsonOrHtmlView):
    template_name = 'module.html'

    def get(self, request, path, module, is_json=None):
        code_base = get_files()
        _file = code_base.get_file(path, module)
        data = dict(file=_file)
        return self._response(request, data, is_json)


all_packages_view = AllPackagesView.as_view()
package_view = PackageView.as_view()
module_view = ModuleView.as_view()
