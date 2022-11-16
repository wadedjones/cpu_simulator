# CPU file

from memory import Memory
from cache import Cache

# Instruction list should be registers
# CPU counter should count up and be in sync with registers

class CPU:
    def __init__(self):
        self.memory_bus = Memory()
        self.cache = Cache()
        self.counter = 0
        self.register = ['' for i in range(32)]

    def read_instructions(self):
        with open(self.instruction_file, 'r') as file:
            for line in file.readlines():
                # insert data into register at [cpu_counter] index
                self.register.insert(self.counter, tuple(line.strip().split(',')))
                if self.counter > 32:
                    self.counter = 0
                else:
                    self.counter += 1
        return 

    def read_write_data(self):
        with open(self.data_file, 'r') as file:
            for line in file.readlines():
                address, value = line.strip().split(',')
                self.memory_bus.write_memory(address, value)

    def execute_instructions(self):
        pass

    def _ADD(self, dest, src_1, src_2):
        self.register[int(dest)] = src_1 + src_2

    def _ADDI(self, dest, src_1, const):
        self.register[int(dest)] = src_1 + const
        
    def _J(self, target):
        self.counter = int(target)

    def _CACHE(self, num):
        pass