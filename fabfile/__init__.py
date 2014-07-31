import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'ast_parse.settings'

from fabric.api import task, env
from ast_parse.parse.utils.django_files import get_files
from django.conf import settings
import redis

'''
State Machine A

package -> package | module | end
module -> class | function | end
class -> function | end
function -> end

State Machine B

package -> package | module | class | function | end
module -> class | function | end
class -> function | end
function -> end

for sm b if current_state == django.views you can go directly
to django.views.generic.View if the input is V
'''


@task
def populate_redis():
    _redis = redis.StrictRedis(host=settings.REDIS_HOST,
                               port=settings.REDIS_PORT,
                               db=settings.REDIS_CODEBASE_PORT)
    _redis.flushdb()
    code_base = get_files()
    _redis.lpush('packages', *code_base.sub_dirs)  # LRANGE packages 0 -1
