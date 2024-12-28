import calendar

def print_month_calendar():
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    if 1 <= month <= 12:
        print("\n", calendar.month(year, month))
    else:
        print("Invalid month! Please enter a value between 1 and 12.")

def print_year_calendar():
    year = int(input("Enter year: "))
    print("\n", calendar.calendar(year))

def main():
    while True:
        print("\nMenu:")
        print("1. Print specific month calendar")
        print("2. Print specific year calendar")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print_month_calendar()
        elif choice == 2:
            print_year_calendar()
        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please select a valid option.")
main()
        
            
        
        
    
    
       
    
    
    
    
        
       