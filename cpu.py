# CPU file

from memory import Memory
from cache import Cache
import sys

# Instruction list should be registers
# CPU counter should count up and be in sync with registers

class CPU:
    def __init__(self):
        self.memory_bus = Memory()
        self.cache = Cache()
        self.counter = 1
        self.register = [None for i in range(32)]
        self.cache.set_cache(0)

    def read_instructions(self, instruction_file):
        with open(instruction_file, 'r') as file:
            for line in file.readlines():
                # insert data into register at [cpu_counter] index
                self.register.insert(self.counter, tuple(line.strip().split(',')))
                print("Adding new instruction to register...")
                if self.counter > 32:
                    self.counter = 1
                else:
                    self.counter += 1
        return 

    def read_write_data(self, data_file):
        with open(data_file, 'r') as file:
            for line in file.readlines():
                address, value = line.strip().split(',')
                self.memory_bus.write_memory(address, value)
        return

    def execute_instructions(self):
        """
        instruction[0] = ('CACHE', 'ADDI', 'ADD', 'J', 'HALT')
            new MIPS instructions to be added in the future.
            this function is way too long, I know
        instruction[1] = Destination Register OR Cache setting
        instruction[2] = Register to grab value
        instruction[3] = Register to grab value OR const
        """
        for instruction in self.register:
            if instruction is not None:
                # CACHE instruction turns cache on (1) or off (0)
                if instruction[0] == 'CACHE':
                    self.cache.set_cache(int(instruction[1]))

                elif instruction[0] == 'ADDI':
                    if self.cache.search_cache(instruction[2]):
                        src_1 = self.cache.search_cache(instruction[2])
                    else:
                        src_1 = self.memory_bus.search_memory(instruction[2])
                        self.cache.write_cache(instruction[2], src_1)
                    self._ADDI(instruction[1][1], src_1, instruction[3])
                    self.memory_bus.write_memory('{0:08b}'.format(int(instruction[1][1])), (int(src_1) + int(instruction[3])))

                elif instruction[0] == 'ADD':
                    if self.cache.search_cache(instruction[2]):
                        src_1 = self.cache.search_cache(instruction[2])
                    else:
                        src_1 = self.memory_bus.search_memory(instruction[2])
                        self.cache.write_cache(instruction[2], src_1)
                    if self.cache.search_cache(instruction[3]):
                        src_2 = self.cache.search_cache(instruction[3])
                    else:
                        src_2 = self.memory_bus.search_memory(instruction[3])
                        self.cache.write_cache(instruction[3], src_2)
                    self._ADD(instruction[1][1], src_1, src_2)
                    self.memory_bus.write_memory('{0:08b}'.format(int(instruction[1][1])), (int(src_1) + int(src_2)))

                elif instruction[0] == 'J':
                    self._J(instruction[1])

                elif instruction[0] == 'HALT':
                    self._HALT()

    def _write_back(self):
        for instruction in self.register:
            if instruction is not None:
                pass

    def _ADD(self, dest, src_1, src_2):
        """
        instruction[0] = ADD
        instruction[1] = dest -> Register Destination
        instruction[2] = src_1 -> First Register to get value
        instruction[3] = src_2 -> Second Register to get value
        """
        self.register[int(dest)] = int(src_1) + int(src_2)
        print(f"Adding {int(src_1)} and {int(src_2)} to register {int(dest)}")

    def _ADDI(self, dest, src_1, const):
        """
        instruction[0] = ADDI
        instruction[1] = dest -> Register Destination
        instruction[2] = src_1 -> Register to get value
        instruction[3] = const -> value to add to Register
        """
        self.register[int(dest)] = int(src_1) + int(const)
        print(f"Adding {int(src_1)} and {int(const)} to register {int(dest)}")
        
    def _J(self, target):
        self.counter = int(target)

    def _CACHE(self, num):
        pass

    def _HALT(self):
        sys.exit('Exit Code, instructions completed.')

