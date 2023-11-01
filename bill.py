import os

def add_bill(bills, bill_id, product_id, date, reference, price, quantity):
    bills.append({'bill_id': bill_id, 'product_id': product_id, 'date': date, 'reference': reference, 'price': price, 'quantity': quantity})

def list_by_bill_id(bills, bill_id):
    filtered_bills = [bill for bill in bills if bill['bill_id'] == bill_id]
    return filtered_bills

def list_by_product_id(bills, product_id):
    filtered_products = [bill for bill in bills if bill['product_id'] == product_id]
    return filtered_products

def display_single_bill(bills, bill_id):
    filtered_bills = list_by_bill_id(bills, bill_id)
    if not filtered_bills:
        print("No bill found.")
    else:
        total = 0
        print("Bill ID\tProduct ID\tDate\tReference\tTotal Price")
        for bill in filtered_bills:
            total += bill['price'] * bill['quantity']
            print(f"{bill['bill_id']}\t{bill['product_id']}\t{bill['date']}\t{bill['reference']}\t{bill['price'] * bill['quantity']}")
        print(f"Total: {total}")

def display_single_product(bills, product_id):
    filtered_products = list_by_product_id(bills, product_id)
    if not filtered_products:
        print("No product found.")
    else:
        total = 0
        print("Product ID\tBill ID\tDate\tReference\tTotal Price")
        for product in filtered_products:
            total += product['price'] * product['quantity']
            print(f"{product['product_id']}\t{product['bill_id']}\t{product['date']}\t{product['reference']}\t{product['price'] * product['quantity']}")
        print(f"Total: {total}")

def save_to_file(bills):
    with open("bills_data.txt", 'w') as file:
        for bill in bills:
            file.write(f"{bill['bill_id']},{bill['product_id']},{bill['date']},{bill['reference']},{bill['price']},{bill['quantity']}\n")

def load_from_file():
    bills = []
    try:
        with open("bills_data.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(',')
                bills.append({
                    'bill_id': data[0],
                    'product_id': data[1],
                    'date': data[2],
                    'reference': data[3],
                    'price': float(data[4]),
                    'quantity': float(data[5])
                })
    except FileNotFoundError:
        pass
    return bills

def main():
    bills = load_from_file()

    while True:
        print("\nBILL MANAGEMENT MENU:")
        print("1. Add Bill")
        print("2. List by Bill ID")
        print("3. List by Product ID")
        print("4. Display Single Bill")
        print("5. Display Single Product")
        print("6. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            bill_id = input("Enter Bill ID: ")
            product_id = input("Enter Product ID: ")
            date = input("Enter Date: ")
            reference = input("Enter Reference: ")
            price = float(input("Enter Price: "))
            quantity = float(input("Enter Quantity: "))
            add_bill(bills, bill_id, product_id, date, reference, price, quantity)
            print("Bill added.")
        elif choice == '2':
            bill_id = input("Enter Bill ID: ")
            filtered_bills = list_by_bill_id(bills, bill_id)
            for bill in filtered_bills:
                print(f"Bill ID: {bill['bill_id']}, Product ID: {bill['product_id']}, Date: {bill['date']}, Reference: {bill['reference']}")
        elif choice == '3':
            product_id = input("Enter Product ID: ")
            filtered_products = list_by_product_id(bills, product_id)
            for product in filtered_products:
                print(f"Product ID: {product['product_id']}, Bill ID: {product['bill_id']}, Date: {product['date']}, Reference: {product['reference']}")
        elif choice == '4':
            bill_id = input("Enter Bill ID: ")
            display_single_bill(bills, bill_id)
        elif choice == '5':
            product_id = input("Enter Product ID: ")
            display_single_product(bills, product_id)
        elif choice == '6':
            save_to_file(bills)
            print("Bill data saved to file.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    print("\x1bc\x1b[43;30m")

    main()

