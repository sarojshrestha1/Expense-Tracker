def main():
    while True:
        print("\n\t\t-------------------------------")
        print("\n\t\t\tExpence Tracker")
        print("\n\t\t-------------------------------")
        print("\n\t\t1. Add Expense")
        print("\n\t\t2. Veiw Expense")
        print("\n\t\t3. Delete Expense")
        print("\n\t\t4. Exit")
        #catching error
        try:
            choice=int(input("\n\t\t Please enter your choice: "))

        except ValueError:
            print("\n\t\tPlease enter the choice in number")
            continue

        if choice<1 or choice>4:
            print("\n\t\tPlease Enter the choice (1-4) not other!")
            continue
        # matching choice
        match choice:
            case 1:
                add_expense()

            case 2:
                view_expense()

            case 3:
                delete_expense()

            case 4:
                return

            case _:
                print("\n\t\tError")

#creating function to add expense
def add_expense():
    print("\n\t\t-------------------------------")
    print("\n\t\t\tAdd Expence")
    print("\n\t\t-------------------------------")

    try:
        amount= float(input("Enter Amount: "))

    except ValueError:
        print("Enter amount in numbers not in words!")
        return

    if amount <0:
        print("Please enter positive number ") 
        return
    

    category= input("Enter category: ")
    date= input("Enter date: ")
    description= input("Enter description: ")

    

#creating function to view expense
def view_expense():
    print("\n\t\t-------------------------------")
    print("\n\t\t\tView Expence")
    print("\n\t\t-------------------------------")     

#creating function to delete expense
def delete_expense():
    print("\n\t\t-------------------------------")
    print("\n\t\t\tDelete Expence")
    print("\n\t\t-------------------------------")

if __name__ == "__main__":
    main()