# Bobo Yan
# 4/23/2022
# 3900 activity 7 Object Oriented Python Exercise

import csv
from Customer import Customer


def show_list(customerlist):
    with open("customers.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        cuslist = []
        for lines in csv_reader:
            cust = Customer(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5], lines[6], lines[7])
            print(lines[0], ":", lines[1], lines[2])
            cuslist.append(cust)

    return cuslist


def main():
    print("CUSTOMER VIEWER\n")
    print("ALL CUSTOMERS")
    print("-------------------------")
    list_of_customers = []
    list_of_customers = show_list(list_of_customers)

    while True:
        try:
            customerID = int(input("\nEnter Customer ID: "))
            for obj in list_of_customers:
              if customerID == obj.cust_ID:
                print()
                print(obj.fname, obj.lname)
                print(obj.company)
                print(obj.street)
                print(obj.city, obj.state, obj.zipcode)
                choice = input("\nWould you like to continue? y/n: ")
                if choice.lower() == "n":
                    exit()
                elif choice.lower() == "y":
                    continue
        except ValueError:
            print("Customer", customerID, "does not exist")
            choice = input("\nWould you like to continue? y/n: ")
            if choice.lower() == "n":
                exit()
            elif choice.lower() == "y":
                continue


if __name__ == "__main__":
    main()
