from injecta.mocks.Bar import Bar

class Foo:

    def __init__(self, bar: Bar):
        self.__bar = bar
