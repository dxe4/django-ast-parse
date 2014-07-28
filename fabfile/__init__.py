import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'ast_parse.settings'

from fabric.api import task, env
from ast_parse.parse.utils.django_files import get_files
from django.conf import settings
import redis


@task
def populate_redis():
    _redis = redis.StrictRedis(host=settings.REDIS_HOST,
                               port=settings.REDIS_PORT,
                               db=settings.REDIS_CODEBASE_PORT)
    code_base = get_files()
    _redis.sadd('packages', code_base.sub_dirs)
