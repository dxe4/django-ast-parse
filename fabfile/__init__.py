import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'ast_parse.settings'

from collections import defaultdict
from fabric.api import task, env
from ast_parse.parse.utils.django_files import get_files
from django.conf import settings
import redis

'''
State Machine A

start -> package -> package | module | end
start -> module -> class | function | end
start -> class -> function | end
start -> function -> end

State Machine B

start -> package -> package | module | class | function | end
start -> module -> class | function | end
start -> class -> function | end
start -> function -> end

for sm b if current_state == django.views you can go directly
to django.views.generic.View if the input is V


State Machine C

start -> class -> function | end
start -> function -> end

Search Rules:
    current_depth <= n/2
    len(_input) <= 2 -> n -> startswith
    len(_input) > 2 -> n -> startswith + any position

    # less possibilities here
    current_depth > n/2
    len(_input) <= 1 -> n -> startswith
    len(_input) > 1 -> n -> startswith + any position

    # case module
    current_depth=n-1
    len(_input) > 0 -> n -> any position

Score rules:
    startswith score = score * 5
    any position score = score * 2

    Score rules A (static)
    package score = score
    module score = score * 5
    class score = score * 10
    function score = score * 15

    Score rules B (the deeper you go the more score you get)
    score = score * (n - current_depth) * 5
'''


def tree():
    return defaultdict(tree)


@task
def populate_redis():
    _redis = redis.StrictRedis(host=settings.REDIS_HOST,
                               port=settings.REDIS_PORT,
                               db=settings.REDIS_CODEBASE_PORT)
    _redis.flushdb()
    code_base = get_files()
    _redis.lpush('packages', *code_base.sub_dirs)  # LRANGE packages 0 -1

    dirs = [i.replace("/django/", "") for i in code_base.sub_dirs]
    dirs = [(i, len(i.split('/')) - 1) for i in dirs]
