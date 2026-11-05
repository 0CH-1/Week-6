def export(file_path, num_items):
    print("Exporting...")
    with open(file_path, "a") as csv_file:
        for count in range(num_items):
            print("Please enter the item id: ")
            item_id = int(input())

            print("Please enter the item name: ")
            item_name = input()

            print("Please neter the item colour: ")
            item_colour = input()

            data = f"{item_id},{item_name},{item_colour}\n"
            csv_file.write(data)
    print("Done!")


def run_task3():
    export("exported_items.csv", 2)


if __name__ == "__main__":
    run_task3()

