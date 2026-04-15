from sales_analyzer import SalesAnalyzer
from menu import menu, chart_or_text

def main():
    file = input("Enter a your File path to analysis: ")

    try:
        analyzer = SalesAnalyzer(file)
    except FileNotFoundError:
        print("File not found.")
        return

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
                    analyzer.average_product_price()
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
            case '9':
                analyzer.export_data()
            case 'q' | 'quit' | 'exit':
                break
            case _:
                print("Invalid choice.")

if __name__ ==  "__main__":
    main()