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

    def write_memory(self, address, value):
        self.bus[address] = value
        print(f"Adding value: {value} to memory bus: {address}")

    def search_memory(self, address):
        num = address[1]
        if self.bus.get('{0:08b}'.format(int(num))) is not None:
            return self.bus.get('{0:08b}'.format(int(num)))
        return 0

