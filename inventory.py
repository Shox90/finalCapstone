import tabulate


# ========The beginning of the class==========
class Shoes:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        # Add the code to return the cost of the shoe in this method.
        return self.cost

    def get_quantity(self):
        # Add the code to return the quantity of the shoes.
        return self.quantity

    def __str__(self):
        # Add a code to returns a string representation of a class.
        return f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"


# =============Shoe list===========

# The list will be used to store a list of objects of shoes.

shoe_list = []


# ==========Functions outside the class==============
def read_shoes_data():
    """
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    """
    try:
        with open('inventory.txt', 'r') as file:
            # Skip the first line. Hence, the index slice.
            lines = file.readlines()[1:]
            for line in lines:
                country, code, product, cost, quantity = line.split(",")
                shoe_list.append(Shoes(country, code, product, cost, quantity))
    except FileNotFoundError:
        print("File not found")
    for shoe in shoe_list:
        print(shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity)
    return shoe_list


def capture_shoes():
    """
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    """
    # create empty list object 'shoe' to update to
    shoe = []
    while True:
        country = input("Enter country of origin: ")
        code = input("Enter product code: ")
        product = input("Enter product name: ")
        cost = input("Enter cost of the shoe: ")
        quantity = input("Enter quantity: ")
        # update to shoe list
        shoe.append(Shoes(country, code, product, cost, quantity))
        repeat = input("Do you want to add another shoe? (yes/no)")
        if repeat.lower() == "no":
            break
    return shoe


def view_all():
    # TODO: need to install tabulate module
    """
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    """
    with open('inventory.txt', 'r') as file:
        # Skip the first line. Hence, the index slice.
        lines = file.readlines()[1:]
        shoes_table = [["Country", "Code", "Product", "Cost", "Quantity"]]
        for line in lines:
            country, code, product, cost, quantity = line.split(",")
            shoes_table.append([country, code, product, "£" + str(cost), str(quantity)])
    # TODO: Need to read https://pypi.org/project/tabulate/
    # If headers="firstrow", then the first row of data is used.
    # Argument named 'tablefmt' defines how the table is formatted.

    print(tabulate.tabulate(shoes_table, headers="firstrow", tablefmt="fancy_grid"))


def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

    with open('inventory.txt', 'r') as file:
        # Skip the first line. Hence, the index slice.
        lines = file.readlines()[1:]
        for line in lines:
            country, code, product, cost, quantity = line.split(",")
            shoe_list.append(Shoes(country, code, product, cost, quantity))

    # Use min function to find the lowest in a list
    min_quantity = min(shoe.quantity for shoe in shoe_list)
    # newlist = [expression for item in iterable if condition == True]
    shoes_to_restock = [shoe for shoe in shoe_list if shoe.quantity == min_quantity]

    for shoe in shoes_to_restock:
        add = input(f"Do you want to add quantity to {shoe.product}? (yes/no) ")
        if add.lower() == "yes":
            try:
                new_quantity = int(input("Enter new quantity: "))
                # increment on top of existing stock
                shoe.quantity += new_quantity

                with open("inventory.txt", "w") as file:
                    for s in shoe_list:
                        file.write(f"{s.country},{s.code},{s.product},{s.cost},{s.quantity}\n")
                print("Inventory updated.")
            except ValueError:
                print("Please enter a number to restock.")
                continue
        else:
            print("No shoes in the inventory.")


def search_shoe():
    """
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    """
    with open('inventory.txt', 'r') as file:
        # Skip the first line. Hence, the index slice.
        lines = file.readlines()[1:]
        for line in lines:
            country, code, product, cost, quantity = line.split(",")
            shoe_list.append(Shoes(country, code, product, cost, quantity))
    # Note: seems as if I have to keep opening file in each function

    # 'Search'...use for loop
    product_code = input("Enter product code: ")
    for shoe in shoe_list:
        if shoe.code == product_code:
            print(shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity)
            return
    print("No product found with code", product_code)


def value_per_item():
    """
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    """
    with open('inventory.txt', 'r') as file:
        # Skip the first line. Hence, the index slice.
        lines = file.readlines()[1:]
        for line in lines:
            country, code, product, cost, quantity = line.split(",")
            shoe_list.append(Shoes(country, code, product, cost, quantity))

    for shoe in shoe_list:
        value = int(shoe.cost) * int(shoe.quantity)
        print(f"Shoe code: {shoe.code} - Value: £{value}")


def highest_qty():
    """
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    """
    with open('inventory.txt', 'r') as file:
        # Skip the first line. Hence, the index slice.
        lines = file.readlines()[1:]
        for line in lines:
            country, code, product, cost, quantity = line.split(",")
            shoe_list.append(Shoes(country, code, product, cost, quantity))

    # Highest (i.e. max function)
    # cast shoe.quantity as an integer
    highest_quantity = max([int(shoe.quantity) for shoe in shoe_list])
    for shoe in shoe_list:
        if int(shoe.quantity) == highest_quantity:
            print(f"The shoe with highest quantity is {shoe}")
            break


# ==========Main Menu=============
"""
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
"""


def main_menu():
    while True:
        print("==========Shoe Inventory System=============")
        print("1. Read shoe data from file")
        print("2. Capture shoes")
        print("3. View all shoes")
        print("4. Re-stock shoes")
        print("5. Search for a shoe")
        print("6. Calculate value per item")
        print("7. Display the highest quantity shoes")
        print("8. Quit")
        option = int(input("Enter option (1-8): "))

        if option == 1:
            read_shoes_data()
        elif option == 2:
            capture_shoes()
        elif option == 3:
            view_all()
        elif option == 4:
            re_stock()
        elif option == 5:
            search_shoe()
        elif option == 6:
            value_per_item()
        elif option == 7:
            highest_qty()
        elif option == 8:
            break
        else:
            print("Invalid option, please try again")


if __name__ == '__main__':
    main_menu()