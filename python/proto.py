import inspect
from types import FunctionType, MethodType, ClassType

def _isprocess(m):
    if isinstance(m, FunctionType) or  isinstance(m, MethodType):
        return hasattr(m, "__protonode__") and m.__protonode__ == 'process'
    return False

def _istask(cls):
    if isinstance(cls, ClassType):
        return hasattr(cls, "__protonode__") and cls.__protonode__ == 'task'
    return False

def buildtree(task):
    task.__protonode__ = 'task'        
    task.processlist = [i for i in task.__dict__.values() if _isprocess(i)]
    task.tasklist = [i for i in task.__dict__.values() if _istask(i)]

def task(clz):
    buildtree(clz)
    clz.__protonode__ = 'task'
    return clz

def process(fn):
    print "h1"
    fn.__protonode__ = 'process'
    return fn

