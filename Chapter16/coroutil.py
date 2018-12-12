from functools import wraps

def coroutine(func):
    """装饰器：向前执行第一个‘yield’表达式"""
    @wraps(func)
    def primer(*args,**kwargs):
        gen = func(*args,**kwargs)
        next(gen)
        return gen
    return primer