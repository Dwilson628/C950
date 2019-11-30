import algo
import Hashes


def interface():

    # Starts time at 8:00
    # Will continue to ask for user input until input = 'X'
    cycle = 1
    time = "8:00"

    # Converts time into a minute int value for comparison
    time_minutes = sum(x * int(t) for x, t in zip([60, 1], time.split(":")))

    while cycle != 0:
        print("\n'C' to check the packages' status.\n'E' to Edit an address.\n'L' to load trucks\n"
              "'T' to adjust the time\n'I' to initialize a truck from the hub.\n'X' to exit.\n")
        user_input = input()

        if user_input == 'C':

            checking = 1
            while checking == 1:

                # Searches hash table using user input as key
                package_id = input("\nEnter package ID# ('X' to cancel')\n")
                if package_id == 'X':
                    checking = 0
                else:
                    package = Hashes.hashtable.search(int(package_id))

                # If package is found, will provide all info
                    if package != 0:
                        print("\nPackage ID: %d\nShipping Address: %s, %s, %s, %s\nDelivery By: %s\nWeight: %s\nNotes: "
                              "%s\n"
                              % (package[0], package[1], package[2], package[3], package[4], package[5],
                                 package[6], package[7]))
                        print("Status: %s" % package[8])
                    else:
                        print("Package not found.")

        elif user_input == 'E':

            # Searches hash table using input as key
            package_id = input("\nEnter package ID#\n")
            package = Hashes.hashtable.search(int(package_id))

            if package != 0:

                # If package is found, gives address and asks for confirmation to edit
                print("Current Address: %s, %s, %s, %s\nWould you like to edit this address?"
                      % (package[1], package[2], package[3], package[4]))
                confirm_input = input("'Y' for Yes, 'N' for No\n")
                if confirm_input == 'Y':

                    # removes package from the the old address in our graph
                    if package[1] != '':
                        algo.distance_graph.address_list[package[1]].remove(package)

                    # For this program, only the street address is important
                    # Other info would be useful for upscaling
                    package[1] = input("Enter new street address.\n")
                    package[2] = input("Enter city.\n")
                    package[3] = input("Enter state.\n")
                    package[4] = input("Enter ZIP code.\n")

                    if package[1] != '':

                        # if package is given an address, adds it to new address in graph
                        algo.distance_graph.address_list[package[1]].append(package)

                if len(algo.truck3.packages) > 0:

                    # If the trucks are already loaded, this will remove the package from truck
                    # and put updated package into truck3, also running greed algorithm
                    if package in algo.truck1.packages:
                        algo.truck1.packages.remove(package)
                    elif package in algo.truck2.packages:
                        algo.truck2.packages.remove(package)
                    elif package in algo.truck3.packages:
                        algo.truck3.packages.remove(package)
                    algo.truck3.individual_insert(package)
            else:
                print("Package not found.")

        elif user_input == 'L':

            # Calls function to load trucks, should optimally be done first
            algo.load_trucks()

        elif user_input == 'T':

            # user will input a time which is converted into minutes
            print("It is currently %s.\nWhat time would you like to jump to?\n" % time)
            time = input()
            time_minutes = sum(x * int(t) for x, t in zip([60, 1], time.split(":")))

            # time in minutes is used to check if packages have been delivered
            algo.truck1.passed_time(time_minutes)
            algo.truck2.passed_time(time_minutes)
            algo.truck3.passed_time(time_minutes)

        elif user_input == 'I':

            # gets truck to 'leave the hub' storing current time for future distance comparisons
            print("Which truck would you like to initialize? (1, 2, 3)\n")
            truck = input()
            if truck == '1':
                algo.truck1.leave_hub(time_minutes)
            elif truck == '2':
                algo.truck2.leave_hub(time_minutes)
            elif truck == '3':
                algo.truck3.leave_hub(time_minutes)

        elif user_input == 'X':

            # Exits the program
            cycle = 0


interface()

print('\nTotal distance traveled: %.1f miles' % (algo.truck1.length + algo.truck2.length + algo.truck3.length))
