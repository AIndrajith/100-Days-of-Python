import json

def load_exchange_rates(file_path="exchange_rates.json"):
    try:
        with open(file_path, "r")as file:
            return json.load(file)
    except FileNotFoundError:
        print("Exchange rate file not found!")
        return {}
    
def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        return None
    base_amount = amount / rates[from_currency]
    return base_amount * rates[to_currency]

rates = load_exchange_rates()
amount = 100
converted = convert_currency(amount, "USD", "EUR", rates)
print(f"Converted {amount} USD to EUR: {converted: .2f}")