class PseudoPlayer(object):

    def __init__(self, pool):
        self.pool = pool

    def play(self):
        while self.pool.hasmore():
            yield self.pool.pop()
