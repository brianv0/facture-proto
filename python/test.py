from proto import Task, process

class HelloWorld(Task):

    @process
    def helloWorldProcess():
        print "hello world"
