from urllib.request import urlopen


def add_sales_tax(original_amount, country, region):

    sales_tax_rate = urlopen(
        f'https://sales-tax-calculator.p.rapidapi.com/rates/Nigeria/lagos').read().decode()
    return original_amount * float(sales_tax_rate)
