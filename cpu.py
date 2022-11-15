# CPU file

from memory import Memory
from cache import Cache

class CPU:
    def __init__(self, data_file, instruction_file):
        self.data_file = data_file
        self.instruction_file = instruction_file
        self.memory_bus = Memory()
        self.cache = Cache()
        self.instructions = self.read_instructions()
        self.counter = 0
        self.register = [0 for x in range(8)]

    def read_instructions(self):
        instruction_list = []
        with open(self.instruction_file, 'r') as file:
            for line in file.readlines():
                instruction_list.append(tuple(line.strip().split(',')))
        return instruction_list

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