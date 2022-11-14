# Memory for the CPU


class Memory:
    def __init__(self):
        self.bus = {'{0:08b}'.format(x): 0 for x in range(256)}
