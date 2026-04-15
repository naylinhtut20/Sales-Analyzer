import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data.csv")

# Create revenue
df['Revenue'] = df['Price'] * df['Sales']

# 1. Brand with most revenue
def get_top_brand():
    brand_revenue = df.groupby('Brand')['Revenue'].sum().sort_values(ascending=False)
    top_brand = brand_revenue.idxmax()
    top_value = brand_revenue.max()
    print(f"\n{top_brand} generates the highest total revenue at ${top_value}.")
    print(f"This means {top_brand} performs best in total earnings among all brands in this dataset.")

# Brand chart
def top_brand_chart():
    brand_revenue = df.groupby('Brand')['Revenue'].sum().sort_values(ascending=False)
    brand_revenue.plot(kind='bar')
    plt.title("Revenue by Brand")
    plt.xlabel("Brand")
    plt.ylabel("Revenue")
    plt.show()

# 2. Category profitability
def category_revenue():
    category_revenue = df.groupby('Category')['Revenue'].sum()
    if category_revenue['Laptop'] > category_revenue['Phone']:
        print(f"\nLaptops generate more revenue (${category_revenue['Laptop']}) than phones (${category_revenue['Phone']}).")
        print("This means laptops are the more profitable category in this dataset.")
    else:
        print(f"\nPhones generate more revenue (${category_revenue['Phone']}) than laptops (${category_revenue['Laptop']}).")
        print("This means phones are the more profitable category in this dataset.")

def category_revenue_chart():
    category_revenue = df.groupby('Category')['Revenue'].sum()
    category_revenue.plot(kind='pie')
    plt.title("Revenue by Category")
    plt.show()

# 3. Average price
def average_price():
    average_price = df.groupby('Brand')['Price'].mean().sort_values(ascending=False)
    highest_avg_brand = average_price.idxmax()
    highest_avg_value = average_price.max()
    print(f"\n{highest_avg_brand} has the highest average product price at ${highest_avg_value:.2f}.")
    print("This suggests this brand focuses on more premium-priced products.")

def average_price_chart():
    average_price = df.groupby('Brand')['Price'].mean().sort_values(ascending=False)
    average_price.plot(kind='bar')
    plt.title("Average Price")
    plt.xlabel("Brand")
    plt.ylabel("Price")
    plt.show()

# 4. Most expensive product
def most_expesnive():
    most_expensive_product = df.loc[df['Price'].idxmax()]
    print(f"\n{most_expensive_product['Brand']} - {most_expensive_product['Model']} is most expensive product at ${most_expensive_product['Price']}.")
    print("This product is positioned at the top end of the price range in the dataset.")

def product_price_chart():
    product_price = df.groupby('Brand')['Price'].max().sort_values(ascending=False)
    product_price.plot(kind='bar')
    plt.title("Product Price")
    plt.xlabel("Brand")
    plt.ylabel("Price")
    plt.show()

# 5. Best selling product
def best_sellin_product():
    best_selling_product = df.loc[df['Sales'].idxmax()]
    print(f"\n{best_selling_product['Brand']} - {best_selling_product['Model']} is the best-selling product with {best_selling['Sales']} units sold.")
    print("This indicates it has the strongest sales volume in the dataset.")

def product_sales_chart():
    product_sales = df.groupby('Brand')['Sales'].max().sort_values(ascending=False)
    product_sales.plot(kind='pie')
    plt.title("Product Sales")
    plt.show()

# 6. Correlation
def correlation():
    correlation = df['Price'].corr(df['Sales'])

    if correlation > 0:
        print(f"\nThere is a positive correlation ({correlation:.2f}) between price and sales.")
        print("This suggests higher-priced products tend to sell more in this dataset.")
    elif correlation < 0:
        print(f"\nThere is a negative correlation ({correlation:.2f}) between price and sales.")
        print("This suggests higher-priced products tend to sell less in this dataset.")
    else:
        print("\nThere is no clear relationship between price and sales.")


def menu():
    print("\n1. Which brand has the highest total revenue?")
    print("2. Which category has the highest revenue?")
    print("3. Which brand has the highest average price?")
    print("4. Which is the most expensive product?")
    print("5. Which is the best selling product?")
    print("6. Does higher price mean higher sales?")
    print("q. exit.")

def chart_or_text():
    print("\n1. Chart.")
    print("2. Text.")
    index = input(": ")
    if index == '1':
        return True
    elif index == '2':
        return False
    else:
        print("Invalid choice.")

def main():
    while True:
        menu()
        index = input(": ")
        match index:
            case '1':
                selectioin = chart_or_text()
                if selectioin:
                    top_brand_chart()
                else:
                    get_top_brand()
            case '2':
                selectioin = chart_or_text()
                if selectioin:
                    category_revenue_chart()
                else:
                    category_revenue()
            case '3':
                selectioin = chart_or_text()
                if selectioin:
                    average_price_chart
                else:
                    average_price()
            case '4':
                selectioin = chart_or_text()
                if selectioin:
                    product_price_chart()
                else:
                    most_expesnive()
            case '5':
                selectioin = chart_or_text()
                if selectioin:
                    product_sales_chart()
                else:
                    best_sellin_product()
            case '6':
                correlation()
            case 'q' | 'quit' | 'exit':
                break
            case _:
                print("Invalid choice.")

if __name__ ==  "__main__":
    main()