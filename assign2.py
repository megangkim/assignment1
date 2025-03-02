"""
CS 1026B - Assignment #2 – Movie Ticket and Concession Ordering System
Author: mkim945
Date Created: February 25, 2025
"""
This file is used to calculate monthly principal and interest amounts for a given mortgage total. It must calculate these values over X years using projected variations in interest rates. The final function prints out all the results in a structured table.


import random  # Importing random module for daily special selection

# Constants for pricing
REGULAR_TICKET = 14.99
THREE_D_TICKET = 17.99
IMAX_TICKET = 19.99
CHILDREN_TICKET = 8.99
SENIOR_TICKET = 10.99

SMALL_POPCORN = 6.99
MEDIUM_POPCORN = 8.99
LARGE_POPCORN = 10.99
SMALL_DRINK = 4.99
MEDIUM_DRINK = 5.99
LARGE_DRINK = 6.99
CANDY = 4.50
NACHOS = 7.99
HOT_DOG = 6.99

MEMBER_DISCOUNT = 0.15  # 15% discount for members
FAMILY_PACKAGE_DISCOUNT = 0.10  # 10% discount for orders with 4+ tickets
ONLINE_BOOKING_FEE = 1.50  # Flat booking fee
TAX_RATE = 0.13  # 13% tax rate


def validate_input(category, type_value):
    """ Validates if the user input for category and type is correct """
    valid_tickets = {"regular", "3d", "imax", "children", "senior"}
    valid_concessions = {"popcorn", "drinks", "candy", "nachos", "hot dog", "daily special"}
    type_value = type_value.lower().strip()
    category = category.lower().strip()
    
    if category == "movie tickets" and type_value in valid_tickets:
        return True
    elif category == "concessions" and type_value in valid_concessions:
        return True
    return False


def calculate_ticket_cost(ticket_type, quantity):
    """ Computes the total cost of selected movie tickets based on type and quantity """
    ticket_prices = {
        "regular": REGULAR_TICKET,
        "3d": THREE_D_TICKET,
        "imax": IMAX_TICKET,
        "children": CHILDREN_TICKET,
        "senior": SENIOR_TICKET,
    }
    ticket_type = ticket_type.lower().strip()
    return ticket_prices.get(ticket_type, -1) * quantity if ticket_type in ticket_prices else -1


def calculate_concession_cost(concession_type, quantity, size=None):
    """ Computes the total cost of selected concessions based on type, quantity, and size """
    concession_prices = {
        "popcorn": {"small": SMALL_POPCORN, "medium": MEDIUM_POPCORN, "large": LARGE_POPCORN},
        "drinks": {"small": SMALL_DRINK, "medium": MEDIUM_DRINK, "large": LARGE_DRINK},
        "candy": CANDY,
        "nachos": NACHOS,
        "hot dog": HOT_DOG,
    }
    concession_type = concession_type.lower().strip()
    if concession_type in ["popcorn", "drinks"]:
        size = size.lower().strip()
        return concession_prices[concession_type].get(size, -1) * quantity if size in concession_prices[concession_type] else -1
    return concession_prices.get(concession_type, -1) * quantity if concession_type in concession_prices else -1


def apply_discount(subtotal, number_of_tickets):
    """ Applies the best discount available based on membership and ticket quantity """
    membership = input("Are you a member? (y/n): ").strip().lower()
    if membership == 'y':
        return subtotal * (1 - MEMBER_DISCOUNT)
    elif number_of_tickets >= 4:
        return subtotal * (1 - FAMILY_PACKAGE_DISCOUNT)
    return subtotal


def calculate_tax(subtotal):
    """ Computes tax amount based on subtotal """
    return subtotal * TAX_RATE


def get_daily_special():
    """ Randomly selects a daily special from the available options """
    return random.choice(["candy", "nachos", "hot dog"])


def ticket_option():
    """ Handles movie ticket selection and ensures valid input """
    while True:
        ticket_type = input("Select a ticket type (Regular, 3D, IMAX, Children, Senior): ").strip()
        if validate_input("movie tickets", ticket_type):
            break
        print("Invalid Movie Ticket type. Please try again.")
    while True:
        try:
            quantity = int(input("Enter quantity (greater than 0): "))
            if quantity > 0:
                break
            print("Quantity must be greater than zero.")
        except ValueError:
            print("Please enter a valid integer.")
    return ticket_type.lower(), quantity


def concessions_option():
    """ Handles concession selection, validates input, and determines the daily special if selected """
    while True:
        concession_type = input("Select concession type (Popcorn, Drinks, Candy, Nachos, Hot Dog, Daily Special): ").strip()
        if validate_input("concessions", concession_type):
            break
        print("Invalid Concession type. Please try again.")
    size = None
    if concession_type.lower() in ["popcorn", "drinks"]:
        while True:
            size = input("Select size (small, medium, large): ").strip().lower()
            if size in ["small", "medium", "large"]:
                break
            print("Invalid size. Please select 'small', 'medium', or 'large'.")
    elif concession_type.lower() == "daily special":
        concession_type = get_daily_special()
        print(f"You have selected the daily special: {concession_type}")
    while True:
        try:
            quantity = int(input("Enter quantity (greater than 0): "))
            if quantity > 0:
                break
            print("Quantity must be greater than zero.")
        except ValueError:
            print("Please enter a valid integer.")
    return concession_type.lower(), quantity, size


def main():
    """ Main function to process movie ticket and concession orders """
    subtotal = 0
    total_tickets = 0
    while True:
        choice = input("Would you like to order Movie Tickets, Concessions, or type 'done' to finish?: ").strip().lower()
        if choice == "done":
            break
        elif choice == "movie tickets":
            ticket_type, quantity = ticket_option()
            subtotal += calculate_ticket_cost(ticket_type, quantity)
            total_tickets += quantity
        elif choice == "concessions":
            concession_type, quantity, size = concessions_option()
            subtotal += calculate_concession_cost(concession_type, quantity, size)
        else:
            print("Invalid category type. Please try again.")
    if subtotal == 0:
        print("You don't seem to have ordered anything.")
        return
    subtotal = apply_discount(subtotal, total_tickets)
    tax = calculate_tax(subtotal)
    total = subtotal + tax + ONLINE_BOOKING_FEE
    print(f"Subtotal: ${subtotal:.2f}\nTax: ${tax:.2f}\nBooking Fee: ${ONLINE_BOOKING_FEE:.2f}\nTotal: ${total:.2f}")


if __name__ == "__main__":
    main()
