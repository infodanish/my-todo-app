# define custom function and should have 2 new line after function.
import os

FILE_PATH = "todo.txt"


def get_todos(filepath=FILE_PATH):
    abs_path = os.path.join(os.path.dirname(__file__), filepath)
    with open(abs_path, 'r') as file:
        return file.readlines()


def write_todos(todos, filepath=FILE_PATH):
    abs_path = os.path.join(os.path.dirname(__file__), filepath)
    with open(abs_path, 'w') as file:
        file.writelines(todos)


# print(__name__)

if __name__ == "__main__":
    print(get_todos())
    # print("hello")
# else:
    # print("here")

