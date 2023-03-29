import openai
import requests

openai.api_key = "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"

def get_exchange_rate(from_currency, to_currency):
    response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
    data = response.json()
    rate = data["rates"][to_currency]
    return rate

if __name__ == '__main__':
    from_currency = input("Digite a moeda base (por exemplo, USD): ")
    to_currency = input("Digite a moeda de destino (por exemplo, EUR): ")

    exchange_rate = get_exchange_rate(from_currency, to_currency)
    print(f"A taxa de câmbio de {from_currency} para {to_currency} é {exchange_rate:.2f}")
