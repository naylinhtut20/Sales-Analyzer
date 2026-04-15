import matplotlib.pyplot as plt
import pandas as pd


class SalesAnalyzer:
    def __init__(self, file: str):
        self.df = pd.read_csv(file)

        # Create revenue
        self.df['Revenue'] = self.df['Price'] * self.df['Sales']
        self.brand_revenue = self.df.groupby('Brand')['Revenue'].sum().sort_values(ascending=False)
        self.sum_category_revenue = self.df.groupby('Category')['Revenue'].sum()
        self.average_price = self.df.groupby('Brand')['Price'].mean().sort_values(ascending=False)

    # 1. Brand with most revenue
    def get_top_brand(self):
        top_brand = self.brand_revenue.idxmax()
        top_value = self.brand_revenue.max()
        print(f"\n{top_brand} generates the highest total revenue at ${top_value}.")
        print(f"This means {top_brand} performs best in total earnings among all brands in this dataset.")

    # Brand Bar chart
    def top_brand_chart(self):
        self.brand_revenue.plot(kind='bar')
        plt.title("Revenue by Brand")
        plt.xlabel("Brand")
        plt.ylabel("Revenue")
        plt.show()

    # 2. Category profitability
    def category_revenue(self):
        if self.sum_category_revenue['Laptop'] > self.sum_category_revenue['Phone']:
            print(f"\nLaptops generate more revenue (${self.sum_category_revenue['Laptop']}) than phones (${self.sum_category_revenue['Phone']}).")
            print("This means laptops are the more profitable category in this dataset.")
        else:
            print(f"\nPhones generate more revenue (${self.sum_category_revenue['Phone']}) than laptops (${self.sum_category_revenue['Laptop']}).")
            print("This means phones are the more profitable category in this dataset.")

    # Category revenue Pie chart
    def category_revenue_chart(self):
        self.sum_category_revenue.plot(kind='pie')
        plt.ylabel("")
        plt.title("Revenue by Category")
        plt.show()

    # 3. Average price
    def average_product_price(self):
        highest_avg_brand = self.average_price.idxmax()
        highest_avg_value = self.average_price.max()
        print(f"\n{highest_avg_brand} has the highest average product price at ${highest_avg_value:.2f}.")
        print("This suggests this brand focuses on more premium-priced products.")

    # Average price Bar chart
    def average_price_chart(self):
        self.average_price.plot(kind='bar')
        plt.title("Average Price")
        plt.xlabel("Brand")
        plt.ylabel("Price")
        plt.show()

    # 4. Most expensive product
    def most_expensive_product(self):
        most_expensive_products = self.df.loc[self.df['Price'].idxmax()]
        print(f"\n{most_expensive_products['Brand']} - {most_expensive_products['Model']} is most expensive product at ${most_expensive_products['Price']}.")
        print("This product is positioned at the top end of the price range in the dataset.")

    # Product Price Bar chart
    def product_price_chart(self):
        product_price = self.df.groupby('Brand')['Price'].max().sort_values(ascending=False)
        product_price.plot(kind='bar')
        plt.title("Product Price")
        plt.xlabel("Brand")
        plt.ylabel("Price")
        plt.show()

    # 5. Best selling product
    def best_selling_product(self):
        best_selling_products = self.df.loc[self.df['Sales'].idxmax()]
        print(f"\n{best_selling_products['Brand']} - {best_selling_products['Model']} is the best-selling product with {best_selling_products['Sales']} units sold.")
        print("This indicates it has the strongest sales volume in the dataset.")

    # Product sales Pie chart
    def product_sales_chart(self):
        product_sales = self.df.groupby('Brand')['Sales'].max().sort_values(ascending=False)
        product_sales.plot(kind='pie')
        plt.ylabel("")
        plt.title("Product Sales")
        plt.show()

    # 6. Correlation
    def correlation(self):
        correlation = self.df['Price'].corr(self.df['Sales'])

        if correlation > 0:
            print(f"\nThere is a positive correlation ({correlation:.2f}) between price and sales.")
            print("This suggests higher-priced products tend to sell more in this dataset.")
        elif correlation < 0:
            print(f"\nThere is a negative correlation ({correlation:.2f}) between price and sales.")
            print("This suggests higher-priced products tend to sell less in this dataset.")
        else:
            print("\nThere is no clear relationship between price and sales.")
    
    def top_three_brands(self):
        print("These are the Top 3 Brands:")
        print(self.brand_revenue.head(3))

    def lowest_revenue_brand(self):
        lowest_brand = self.brand_revenue.idxmin()
        print(f"{lowest_brand} has Lowest revenue.")

def menu():
    print("\n1. Which brand has the highest total revenue?")
    print("2. Which category has the highest revenue?")
    print("3. Which brand has the highest average price?")
    print("4. Which is the most expensive product?")
    print("5. Which is the best selling product?")
    print("6. Does higher price mean higher sales?")
    print("7. Which are the top 3 brands?")
    print("8. Which is the Lowest revenue brand?")
    print("q. exit.")

def chart_or_text():
    while True:
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
    # file = input("Enter a your File path to analysis: ")
    analyzer = SalesAnalyzer(file= "data.csv")
    while True:
        menu()
        index = input(": ")
        match index:
            case '1':
                selectioin = chart_or_text()
                if selectioin:
                    analyzer.top_brand_chart()
                else:
                    analyzer.get_top_brand()
            case '2':
                selectioin = chart_or_text()
                if selectioin:
                    analyzer.category_revenue_chart()
                else:
                    analyzer.category_revenue()
            case '3':
                selectioin = chart_or_text()
                if selectioin:
                    analyzer.average_price_chart()
                else:
                    analyzer.average_price()
            case '4':
                selectioin = chart_or_text()
                if selectioin:
                    analyzer.product_price_chart()
                else:
                    analyzer.most_expensive_product()
            case '5':
                selectioin = chart_or_text()
                if selectioin:
                    analyzer.product_sales_chart()
                else:
                    analyzer.best_selling_product()
            case '6':
                analyzer.correlation()
            case '7':
                analyzer.top_three_brands()
            case '8':
                analyzer.lowest_revenue_brand()
            case 'q' | 'quit' | 'exit':
                break
            case _:
                print("Invalid choice.")

if __name__ ==  "__main__":
    main()