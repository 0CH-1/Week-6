

def display_chars(file_path, num_chars):
    with open(file_path) as file:
        data = file.read(num_chars)
        print(data)


def display_line(file_path):
    with open(file_path) as file:
        data = file.read().strip()
        print(data)


def display_text(file_path):
    with open(file_path) as file:
        data = file.read()
        print(data)


def run_task2():
    display_chars("Library.txt", 5)
    display_line("Library.txt")
    display_text("Library.txt")


if __name__ == "__main__":
    run_task2()

