# Memory for the CPU


class Memory:
    def __init__(self):
        self.size = 128
        self.bus = {'{0:08b}'.format(x): 0 for x in range(self.size)}

    def data_input(self, data):
        with open(data, 'r') as file:
            for line in file.readlines():
                memory_bus, value = line.strip().split(',')
                self.bus[memory_bus] = value
                print(f"Adding value: {value} to memory bus: {memory_bus}")

