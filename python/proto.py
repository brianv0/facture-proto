class Task:
    __protonode__ = 'task'

def task(clz):
    clz.__protonode__ = 'task'
    
def process(fn):
    fn.__protonode__ = 'process'


