# Memory for the CPU


class Memory:
    def __init__(self):
        self.size = 128
        self.bus = {'{0:08b}'.format(x): 0 for x in range(self.size)}

    def write_memory(self, address, value):
        self.bus[address] = value
        print(f"Adding value: {value} to memory bus: {address}")

    def search_memory(self, address):
        # Address written as 'R2' or 'R3'
        bin_address = '{0:08b}'.format(int(address[1]))
        if self.bus.get(bin_address) is not None:
            return self.bus.get(bin_address)
        return 0

