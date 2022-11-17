# Main file for CPU simulator.

from cpu import CPU

def main():
    my_cpu = CPU()
    print("HERE WE GO I GUESS...\n")
    my_cpu.read_write_data('data_input.txt')
    print("\nData Loaded...\n")
    my_cpu.read_instructions('instruction_input.txt')
    print("\nInstructions Loaded...\n")
    my_cpu.execute_instructions()

if __name__ == '__main__':
    main()