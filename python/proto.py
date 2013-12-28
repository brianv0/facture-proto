import inspect
from types import FunctionType, MethodType, ClassType

class Process:
    deps = []

class Task:
    pass

def buildtree(task):
    task.processlist = [i for i in task.__dict__.values() if _isprocess(i)]
    task.tasklist = [i for i in task.__dict__.values() if _istask(i)]

def task(clz):
    clz.__protonode__ = Task()
    buildtree(clz)
    return clz

def process(fn):
    fn.__process__ = Process()
    fn.__protonode__ = 'process'
    return fn

def leads(fn, trailer, condition="QUEUQ"):
    dep = (trailer, condition)
    fn.__process__.deps.append(dep)
    return fn
    
def trails(fn, leader, condition="DONE"):
    dep = (leader, condition)
    fn.__process__.deps.append(dep)
    return fn

def _isprocess(m):
    if isinstance(m, FunctionType) or  isinstance(m, MethodType):
        return hasattr(m, "__protonode__") and isinstance(m.__protonode__, Process)
    return False

def _istask(clz):
    if isinstance(clz, ClassType):
        return hasattr(clz, "__protonode__") and isinstance(clz.__protonode__, Task)
    return False
