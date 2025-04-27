from typing import Dict, List

CATALOG: Dict[str, Dict[str,float]] = {
    "A001": {"name": "Pan", "price": 1.50},
    "B203": {"name": "Leche", "price": 3.80},
    "C002": {"name": "Jamonada", "price": 1.50},
    "D075": {"name": "Arroz (kg)", "price": 4.70},
}

def get_catalog() -> List[Dict[str, float]]:   
    list_catalog = []
    for code, details in CATALOG.items():
        product = {"code": code}
        product.update(details)
        list_catalog.append(product)
    return list_catalog

def exist_product(code: str) -> bool:
    return code in CATALOG

def get_product(code: str) -> Dict[str, float]:
    return CATALOG.get(code, {})
