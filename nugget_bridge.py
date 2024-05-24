import csv

def read_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = {int(row['serving_size']): float(row['price']) for row in reader}
    return data

def calculate_price(nuggets, price_data):
    serving_sizes = sorted(price_data.keys(), reverse=True)
    total_price = 0.0
    remaining_nuggets = nuggets

    for serving_size in serving_sizes:
        servings, remaining_nuggets = divmod(remaining_nuggets, serving_size)
        total_price += servings * price_data[serving_size]

    return total_price

def main():
    file_path = input("Please enter a file path: ")
    price_data = read_csv(file_path)

    nuggets = int(input("Please enter a number of chicken nuggets: "))
    total_price = calculate_price(nuggets, price_data)

    print(f"{nuggets} Chicken Nuggets costs ${round(total_price, 2)}")

if __name__ == "__main__":
    main()

