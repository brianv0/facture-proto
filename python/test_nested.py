from proto import task, process

@task
class Hello:
    @process
    def helloProcess():
        print "hello"

    @task
    class World:
        @process
        def worldProcess():
            print "world"
