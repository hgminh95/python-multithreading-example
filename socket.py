import random
import time
import config

data = [i for i in xrange(config.MAX_N)]

if config.SWAP_DATA:
    for i in xrange(20):
        first = random.randrange(config.MAX_N)
        second = random.randrange(config.MAX_N)

        data[first], data[second] = data[second], data[first]


class PseudoSocket(object):

    def __init__(self):
        self.cnt = -1

    def receive(self):
        if random.randrange(10) > 8:
            time.sleep(1)
        time.sleep(1.0 / random.randint(20, 30))
        self.cnt += 1

        if self.cnt >= config.MAX_N:
            raise Exception("Connection died.")

        return data[self.cnt]
