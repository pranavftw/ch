import requests
from bs4 import BeautifulSoup
import pandas as pd


# Function to extract product details
def extract_product_info(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    print(response.text)

    # Check if request was successful
    if response.status_code != 200:
        print("Failed to retrieve the page")
        return []

    soup = BeautifulSoup(response.text, "html.parser")  # Use lxml if installed

    # Example selectors (adjust as per actual HTML structure)
    products = soup.find_all('div', class_='product-card')  # Update this selector
    print(products)

    if not products:
        print("No products found on the page. Check your HTML selectors.")
        return []

    product_info_list = []

    for product in products:

        name = product.find('div', class_='product-title').text if product.find('div', class_='product-title') else "N/A"
        price = product.find('div', class_='product-price').text if product.find('div', class_='product-price') else "N/A"
        product_link = product.find('a', class_='product-link')['href'] if product.find('a',class_='product-link') else "N/A"


        #print(f"Product Name: {name}, Price: {price}, Link: {product_link}")  # Debug info

        product_info_list.append({
            'Product Name': name,
            'Price': price,
            'Link': product_link
        })

    return product_info_list


# URL of the e-commerce website's product page (modify accordingly)
ecommerce_url = "http://localhost:8000/product.html"

product_data = extract_product_info(ecommerce_url)

# Check if product data is correctly extracted
for product in product_data:
    print(f"Product Name: {product['Product Name']}, Price: {product['Price']}, Link: {product['Link']}")

# Optionally save to CSV
if product_data:
    df = pd.DataFrame(product_data)
    df.to_csv('product_info.csv', index=False)
    print("Data saved to product_info.csv")
else:
    print("No product data found.")