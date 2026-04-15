def menu():
    print("\n1. Which brand has the highest total revenue?")
    print("2. Which category has the highest revenue?")
    print("3. Which brand has the highest average price?")
    print("4. Which is the most expensive product?")
    print("5. Which is the best selling product?")
    print("6. Does higher price mean higher sales?")
    print("7. Which are the top 3 brands?")
    print("8. Which is the Lowest revenue brand?")
    print("9. Export data.")
    print("q. exit.")

def chart_or_text():
    while True:
        print("\n1. Chart.")
        print("2. Text.")
        index = input(": ")
        if index == '1':
            return True
        elif index == '2':
            return False
        else:
            print("Invalid choice.")