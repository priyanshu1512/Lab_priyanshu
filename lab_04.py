#my python code
class FlightTable:
    def init(self, data):
        self.data = data

    def sort_by_p_id(self):
        self.data.sort(key=lambda x: x[0])

    def sort_by_start_time(self):
        self.data.sort(key=lambda x: x[2])

    def sort_by_priority(self):
        priority_order = {"Low": 0, "MID": 1, "High": 2}
        self.data.sort(key=lambda x: priority_order[x[3]])

    def display_table(self):
        print("P_ID\tProcess\tStart Time (ms)\tPriority")
        for row in self.data:
            print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t\t{row[3]}")


def main():
    data = [
        ("P1", "VSCode", 100, "MID"),
        ("P23", "Eclipse", 234, "MID"),
        ("P93", "Chrome", 189, "High"),
        ("P42", "JDK", 9, "High"),
        ("P9", "CMD", 7, "High"),
        ("P87", "NotePad", 23, "Low")
    ]

    flight_table = FlightTable(data)

    while True:
        print("\nSelect sorting parameter:")
        print("1. Sort by P_ID")
        print("2. Sort by Start Time")
        print("3. Sort by Priority")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            flight_table.sort_by_p_id()
        elif choice == '2':
            flight_table.sort_by_start_time()
        elif choice == '3':
            flight_table.sort_by_priority()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

        flight_table.display_table()


if name == "main":
    main()