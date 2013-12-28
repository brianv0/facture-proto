from proto import Task, Process

class Hello(Task):

    @process
    def helloProcess():
        print "hello"

    class World(Task):
        @process
        def worldProcess():
            print "world"
