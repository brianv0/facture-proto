
import sys
import imp

clazz = sys.argv[1]
foo = imp.load_source("taskdef",clazz)


def walkTask(task):
    
