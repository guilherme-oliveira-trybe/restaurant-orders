import csv


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")

    try:
        write(read(path_to_file))
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


def read(path_to_file):
    with open(path_to_file, encoding="utf-8") as file:
        jobs_reader = csv.reader(file, delimiter=",", quotechar='"')
        orders_log = []
        for cliente, pedido, dia in jobs_reader:
            orders_log.append(
                {"cliente": cliente, "pedido": pedido, "dia": dia}
            )
        return orders_log


def write(orders):
    order_by_client = most_order_plate_by_client("maria", orders)
    times_order_by_client = times_order_by_client_and_plate(
        "arnaldo", "hamburguer", orders
    )
    plates_never_ask = plates_never_ask_by_client("joao", orders)
    days_never_went = days_never_went_to_restaurant("joao", orders)

    new_content = (
        f"{order_by_client}\n"
        f"{times_order_by_client}\n"
        f"{plates_never_ask}\n"
        f"{days_never_went}"
    )

    with open("data/mkt_campaign.txt", "w") as file:
        file.write(new_content)


def most_order_plate_by_client(client_name, orders):
    plates_orders = {}
    for order in orders:
        if order["cliente"] == client_name:
            if order["pedido"] not in plates_orders:
                plates_orders[order["pedido"]] = 0
            else:
                plates_orders[order["pedido"]] += 1
    return str(max(plates_orders, key=plates_orders.get))


def times_order_by_client_and_plate(client_name, plate, orders):
    plate_orders_time = 0
    for order in orders:
        if order["cliente"] == client_name and order["pedido"] == plate:
            plate_orders_time += 1
    return plate_orders_time


def plates_never_ask_by_client(client_name, orders):
    all_plates = set([order["pedido"] for order in orders])
    plates_by_client = set(
        [
            order["pedido"]
            for order in orders
            if order["cliente"] == client_name
        ]
    )
    return all_plates.difference(plates_by_client)


def days_never_went_to_restaurant(client_name, orders):
    all_days = set([order["dia"] for order in orders])
    days_by_client = set(
        [order["dia"] for order in orders if order["cliente"] == client_name]
    )
    return all_days.difference(days_by_client)
