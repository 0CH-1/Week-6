import csv

recordings = []
headings = []

def load_data(file_path):
    print("Loading data...", end="")

    with open(file_path) as csvfile:
        csv_reader = csv.reader(csv_file)
        headings = next(csv_reader)

        for line in csv_reader:
            recordings.append(line)
    print("Done!")


def display_menu():
    print(
    """
    Please select one of the following options:
    [1] Display the names of all passengers
    [2] Display the number of passengers that survived
    [3] Display the number of passengers per gender
    [4] Display the number of passengers per age group
    
    """)


    return int(input())

def display_passengers_names():
    print("The names of the passengers are...\n")

    for record in recordings:
        passenger_name = record[3]
        print(passenger_name)


def display_num_survivors():
    num_survived = 0

    for record in recordings:
        survival_status = int(record[1])
        if survival_status == 1:
            survival_status += 1
    print(f"{num_survived} passengers survived"
          f"")





