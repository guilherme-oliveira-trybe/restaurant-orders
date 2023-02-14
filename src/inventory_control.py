# from analyze_log import read
from collections import Counter


class InventoryControl:
    INGREDIENTS = {
        "hamburguer": ["pao", "carne", "queijo"],
        "pizza": ["massa", "queijo", "molho"],
        "misto-quente": ["pao", "queijo", "presunto"],
        "coxinha": ["massa", "frango"],
    }
    MINIMUM_INVENTORY = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 50,
        "massa": 50,
        "frango": 50,
    }

    def __init__(self):
        self.orders = []

    def add_new_order(self, customer, order, day):
        self.orders.append({"cliente": customer, "pedido": order, "dia": day})

    def get_quantities_to_buy(self):
        ingredients_to_by = {}
        ingredients_used = self.count_ingredients_by_order()
        for key in self.MINIMUM_INVENTORY.keys():
            if key in ingredients_used:
                ingredients_to_by[key] = ingredients_used[key]
            else:
                ingredients_to_by[key] = 0
        return ingredients_to_by

    def count_ingredients_by_order(self):
        ingredients_used = []
        for order in self.orders:
            ingredients = self.INGREDIENTS[order["pedido"]]
            for i in ingredients:
                ingredients_used.append(i)
        return Counter(ingredients_used)
