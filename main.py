import threading
from socket import PseudoSocket
from player import PseudoPlayer


"""
Q: Try to modify DataPool class so the expected code work
"""


class DataPool(object):
    """
    Data Pool is where data is stored. Data Pool support 2 main operators:
        - push(data): Add new data (number) to data pool
        - pop(): Return the smallest data (smallest number) in the pool

    Note that this code below does not work as the specs state
    """

    def __init__(self):
        self._data = []
        self._open = True

    def hasmore(self):
        return self._open or len(self._data) > 0

    def close(self):
        self._open = False

    def push(self, data):
        if not self.hasmore():
            raise Exception("Illegal push after data pool is closed")
        self._data.append(data)

    def pop(self):
        return self._data.pop(0)


class ReceiveThread(threading.Thread):
    """
    Receive Thread receives data through self.socket and then add these
    data to data pool
    """

    def __init__(self, pool):
        threading.Thread.__init__(self)
        self.socket = PseudoSocket()
        self.pool = pool

    def run(self):
        while True:
            try:
                data = self.socket.receive()
                self.pool.push(data)
            except Exception:
                # Connection died.
                break
        self.pool.close()

        print "[ReceiveThread] Receive all packets"


class PlayThread(threading.Thread):
    """
    Play Thread gets data from data pool and play it (it just prints them to screen).
    """

    def __init__(self, pool):
        threading.Thread.__init__(self)
        self.player = PseudoPlayer(pool)

    def run(self):
        curr = 0
        for packet in self.player.play():
            print "[PlayThread] Play {0}".format(packet)
            # Check if data is played in ascending order
            assert packet == curr
            curr += 1
        print "==================="
        print "Congrats! It works."
        print "==================="


pool = DataPool()

receive_thread = ReceiveThread(pool)
play_thread = PlayThread(pool)

receive_thread.start()
receive_thread.join()

play_thread.start()
play_thread.join()


# Expected code
# receive_thread.start()
# play_thread.start()

# receive_thread.join()
# play_thread.join()
