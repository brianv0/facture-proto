from proto import process, task

@task
class HelloWorld:
    
    @process
    def helloWorldProcess():
        print "hello world"
