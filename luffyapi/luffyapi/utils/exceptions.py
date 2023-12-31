# 方法重写下面这个 加日志
# 'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
from rest_framework.views import exception_handler
# from luffyapi.utils import response
from .response import APIResponse

from .logger import log
def common_exception_handler(exc, context):
    # log.error('views是:%s:错误是%s'%((context['view']),str(exc)))
    log.error('views是:%s:错误是%s'%(str(context['view'].__class__.__name__),str(exc)))
    ret = exception_handler(exc, context)  # 是Response对象 内部的data

    if not ret:  # drf内置处理不了丢给django的自己处理
        # 可加更具体的捕获异常
        if isinstance(exc,KeyError):
            return APIResponse(code=0, msg='Key error', )
        return APIResponse(code=0, msg='error',result=str(exc))
    else:
        return APIResponse(code=0, msg='error', result=ret.data)
