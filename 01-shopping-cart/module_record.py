import csv
from datetime import datetime
from typing import List, Dict

HISTORICAL_ARCHIVE = "purchase_history.csv"

def save_purchase(products: List[Dict[str, any]], total: float) -> None:
    purchase_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    products_str = "; ".join(
        f"{p['name']} (x{p['quantity']})" 
        for p in products
    )

    try:
        with open(HISTORICAL_ARCHIVE, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([purchase_date, products_str, f"S/{total:.2f}"])
        
    except FileNotFoundError:
        print("¡The file isn't found!")
    except Exception as e:
        print("An error occurred:", e)