# reads product IDs from text file and outputs CSV file with today's date, transaction ID, product ID, product name, and price

import csv
import datetime

# dict to store product IDs, name, and price
products = {
    'P001': {'Wireless Headphones': 100},
    'P002': {'Laptop Backpack': 60},
    'P003': {'Bluetooth Speaker': 50},
    'P004': {'USB Flashdrive': 20},
    'P005': {'Mobile Phone Case': 15},
    'P006': {'Wireless Mouse': 30},
    'P007': {'Laptop Stand': 40},
    'P008': {'HDMI Cable': 15},
    'P009': {'Smartphone': 600},
    'P010': {'Exeternal Hard Drive': 100}
}

# read product IDs from text file
with open('product_sales.txt', 'r') as file:
    product_ids = file.readlines()

# get today's date
today = datetime.date.today()

# create CSV file with today's date
with open(f'sales-{today}.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['current_date', 'sale_id', 'product_id', 'name', 'price'])

    # write current date, transaction ID, product ID, product name, and price to CSV file
    for i, product_id in enumerate(product_ids):
        product_id = product_id.strip()
        name = list(products[product_id].keys())[0]
        price = list(products[product_id].values())[0]
        writer.writerow([today, f'{i+1}', product_id, name, price])