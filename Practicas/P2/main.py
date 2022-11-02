import T1_parse_data
import T2_createBBB_container
import T3_resize_input
import T4_broadcasting_stds
import textwrap


class Practice2:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def get_input_path(self):
        return self.input_path

    def get_output_path(self):
        return self.output_path

    def set_input_path(self, input_path):
        self.input_path = input_path

    def set_output_path(self, output_path):
        self.output_path = output_path

    def task1(self):
        print("--- Task 1 - Parse video data ---")
        T1_parse_data.task1(self.input_path)

    def task2(self):
        print("--- Task 2 - Create BBB container ---")
        T2_createBBB_container.task2(self.input_path)

    def task3(self):
        print("--- Task 3 - Resize any input ---")
        T3_resize_input.task3(self.input_path, self.output_path)

    def task4(self):
        print("--- Task 4 - Check broadcasting standards ---")
        T4_broadcasting_stds.task4(self.input_path)


input_file = input("Write the path to your input file: ")
output_file = input("Write the name of the output file: ")
handler = Practice2(input_file, output_file)

option = ""
while not (option == "q" or option == "Q"):
    print(textwrap.dedent("""\
            Task 1: Parse video data (show lots of info about file)
            Task 2: Create BBB container
            Task 3: Resize any input
            Task 4: Check broadcasting standards"""))
    option = input("Choose 1, 2, 3, 4 for tasks, "
                   "'i' to change the name of your input file,"
                   " 'o' to change the name of your output file,"
                   " or 'q' to exit: ")
    print()
    if option == "1":
        handler.task1()
    elif option == "2":
        handler.task2()
    elif option == "3":
        handler.task3()
    elif option == "4":
        handler.task4()
    elif option == "i":
        print("Current input file: " + handler.get_input_path())
        handler.set_input_path(input("Write the path to your new input file: "))
    elif option == "o":
        print("Current output file: " + handler.get_output_path())
        handler.set_output_path(input("Write the name of a new output file: "))
    elif option != "q" and option != "Q":
        print("Invalid option")
    print()
print("Thanks! Bye!")
