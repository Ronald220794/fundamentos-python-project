from typing import Dict, List, Tuple
from module_catalog import exist_product, get_product

class Cart:

    def __init__(self):
        self.items: Dict[str, int] = {}

    def add_cart (self, code:str, quantity: int) -> Tuple[bool, str]:
        if not exist_product(code):
            return False, "The code isn't exist in Catalog"
        
        if quantity <= 0:
            return False, "The quantity must be greater than zero"
        
        self.items[code]= self.items.get(code,0) + quantity
        product = get_product(code)
        return True, f"✔ {product['name']} (x{quantity}) added to cart"
    
    def remove_form_cart(self, code:str, quantity:int = None) -> Tuple[bool, str]:
        if code not in self.items:
            return False, "Product isn't in the Cart"
        
        if quantity is None or quantity >= self.items[code]:
            del self.items[code]
            product = get_product(code)
            return True, f"Product {product['name']} removed from cart"        
    
    def get_cart (self) -> List[Dict[str, float]]:
        content = []
        for code, quantity in self.items.items():
            product = get_product(code)
            content.append({
                "code": code,
                "name": product["name"],
                "price" : product["price"],
                "quantity" : quantity,
                "subtotal" : product["price"] * quantity
            })
        return content
    
    def calculate_total (self) -> float:
        return sum(item["subtotal"] for item in self.get_cart())
    
    def it_is_empty (self) -> bool:
        return len(self.items) == 0
    
    def empty_cart_items(self) -> bool:
        self.items.clear()

    def empty_cart(self) -> Tuple[bool, str]:
        
        while True:
            try:
                confirmation = input("Are you sure you want to empty your cart? (Yes/No): ").strip().lower()

                if confirmation not in ['yes', 'no']:
                        raise ValueError("Please only enter 'yes' or 'no'")

                if confirmation == 'yes':
                        self.items.clear()
                        return True, "Cart emptied correctly\n"
                else:
                    return False, "Operation Cancelled\n" 
        
            except ValueError as e:
                print(f"\nError: {e}\n")    

