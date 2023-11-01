
import tkinter as tk

def add_bill():
    bill_id = bill_id_entry.get()
    product_id = product_id_entry.get()
    date = date_entry.get()
    reference = reference_entry.get()
    price = float(price_entry.get())
    quantity = float(quantity_entry.get())

    bills.append({'bill_id': bill_id, 'product_id': product_id, 'date': date, 'reference': reference, 'price': price, 'quantity': quantity})
    update_display()

def list_by_bill_id():
    selected_bill_id = bill_id_list_entry.get()
    filtered_bills = [bill for bill in bills if bill['bill_id'] == selected_bill_id]
    display_filtered_bills(filtered_bills)

def list_by_product_id():
    selected_product_id = product_id_list_entry.get()
    filtered_products = [bill for bill in bills if bill['product_id'] == selected_product_id]
    display_filtered_bills(filtered_products)

def display_single_bill():
    selected_bill_id = bill_id_entry_display.get()
    filtered_bills = [bill for bill in bills if bill['bill_id'] == selected_bill_id]
    display_filtered_bills(filtered_bills)

def display_single_product():
    selected_product_id = product_id_entry_display.get()
    filtered_products = [bill for bill in bills if bill['product_id'] == selected_product_id]
    display_filtered_bills(filtered_products)

def display_filtered_bills(filtered_bills):
    bills_text.delete(1.0, tk.END)
    if not filtered_bills:
        bills_text.insert(tk.END, "No bills found.")
    else:
        bills_text.insert(tk.END, "Bill ID\tProduct ID\tDate\tReference\tTotal Price\n")
        total = 0
        for bill in filtered_bills:
            total += bill['price'] * bill['quantity']
            bills_text.insert(tk.END, f"{bill['bill_id']}\t{bill['product_id']}\t{bill['date']}\t{bill['reference']}\t{bill['price'] * bill['quantity']}\n")
        bills_text.insert(tk.END, f"Total: {total}")

def save_to_file():
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

def update_display():
    display_filtered_bills(bills)

bills = load_from_file()

root = tk.Tk()
root.title("Bill Management")
root.configure(bg="brown", width=800, height=600)  # Define a cor de 

# Adding Bill Section
bill_id_label = tk.Label(root, text="Bill ID:")
bill_id_label.grid(row=0, column=0)
bill_id_entry = tk.Entry(root)
bill_id_entry.grid(row=0, column=1)

product_id_label = tk.Label(root, text="Product ID:")
product_id_label.grid(row=1, column=0)
product_id_entry = tk.Entry(root)
product_id_entry.grid(row=1, column=1)

date_label = tk.Label(root, text="Date:")
date_label.grid(row=2, column=0)
date_entry = tk.Entry(root)
date_entry.grid(row=2, column=1)

reference_label = tk.Label(root, text="Reference:")
reference_label.grid(row=3, column=0)
reference_entry = tk.Entry(root)
reference_entry.grid(row=3, column=1)

price_label = tk.Label(root, text="Price:")
price_label.grid(row=4, column=0)
price_entry = tk.Entry(root)
price_entry.grid(row=4, column=1)

quantity_label = tk.Label(root, text="Quantity:")
quantity_label.grid(row=5, column=0)
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=5, column=1)

add_bill_button = tk.Button(root, text="Add Bill", command=add_bill)
add_bill_button.grid(row=6, columnspan=2)

# List by Bill ID Section
bill_id_list_label = tk.Label(root, text="List by Bill ID:")
bill_id_list_label.grid(row=7, column=0)
bill_id_list_entry = tk.Entry(root)
bill_id_list_entry.grid(row=7, column=1)

list_by_bill_id_button = tk.Button(root, text="List by Bill ID", command=list_by_bill_id)
list_by_bill_id_button.grid(row=8, columnspan=2)

# List by Product ID Section
product_id_list_label = tk.Label(root, text="List by Product ID:")
product_id_list_label.grid(row=9, column=0)
product_id_list_entry = tk.Entry(root)
product_id_list_entry.grid(row=9, column=1)

list_by_product_id_button = tk.Button(root, text="List by Product ID", command=list_by_product_id)
list_by_product_id_button.grid(row=10, columnspan=2)

# Display Single Bill Section
bill_id_display_label = tk.Label(root, text="Display Single Bill:")
bill_id_display_label.grid(row=11, column=0)
bill_id_entry_display = tk.Entry(root)
bill_id_entry_display.grid(row=11, column=1)

display_single_bill_button = tk.Button(root, text="Display Single Bill", command=display_single_bill)
display_single_bill_button.grid(row=12, columnspan=2)

# Display Single Product Section
product_id_display_label = tk.Label(root, text="Display Single Product:")
product_id_display_label.grid(row=13, column=0)
product_id_entry_display = tk.Entry(root)
product_id_entry_display.grid(row=13, column=1)

display_single_product_button = tk.Button(root, text="Display Single Product", command=display_single_product)
display_single_product_button.grid(row=14, columnspan=2)

# Bill Details Section
bills_text = tk.Text(root, height=15, width=50)
bills_text.grid(row=15, columnspan=2)

save_and_exit_button = tk.Button(root, text="Save and Exit", command=save_to_file)
save_and_exit_button.grid(row=16, columnspan=2)

root.mainloop()
