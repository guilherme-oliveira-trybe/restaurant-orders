from analyze_log import (
    most_order_plate_by_client,
    plates_never_ask_by_client,
    days_never_went_to_restaurant,
)


class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self) -> None:
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append({"cliente": customer, "pedido": order, "dia": day})

    def get_most_ordered_dish_per_customer(self, customer):
        return most_order_plate_by_client(customer, self.orders)

    def get_never_ordered_per_customer(self, customer):
        return plates_never_ask_by_client(customer, self.orders)

    def get_days_never_visited_per_customer(self, customer):
        return days_never_went_to_restaurant(customer, self.orders)

    def get_busiest_day(self):
        busiest_day = {}
        for order in self.orders:
            if order["dia"] not in busiest_day:
                busiest_day[order["dia"]] = 0
            else:
                busiest_day[order["dia"]] += 1
        return str(max(busiest_day, key=busiest_day.get))

    def get_least_busy_day(self):
        least_busy_day = {}
        for order in self.orders:
            if order["dia"] not in least_busy_day:
                least_busy_day[order["dia"]] = 0
            else:
                least_busy_day[order["dia"]] += 1
        return str(min(least_busy_day, key=least_busy_day.get))
