# CPU file

from memory import Memory

class CPU:
    def __init__(self, data_file, instruction_file):
        self.data_file = data_file
        self.instruction_file = instruction_file
        self.memory_bus = Memory()
        self.memory_bus.data_input(self.data_file)
        self.instructions = self.read_instructions()

    def read_instructions(self):
        instruction_list = []
        with open(self.instruction_file, 'r') as file:
            for line in file.readlines():
                instruction_list.append(tuple(line.strip().split(',')))
        return instruction_list

    def execute_instructions(self):
        pass