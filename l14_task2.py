class Restaurant:
    def __init__(self, name, cuisine, menu):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu


class FastFood(Restaurant):
    def __init__(self, name, cuisine, menu, drive_thru: bool):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, dishname, qty):
        if not (
            dishname in self.menu
            and 'price' in self.menu[dishname] and
            'inventory' in self.menu[dishname]
        ):
            return 'Dish not available'

        price = self.menu[dishname]['price']
        inventory = self.menu[dishname]['inventory']

        if qty > inventory:
            return 'Order cannot be fulfilled'

        total_cost = qty * price
        self.menu[dishname]['inventory'] -= qty
        return total_cost


menu = {
    'burger': {'price': 5, 'inventory': 10},
    'pizza': {'price': 10, 'inventory': 20},
    'drink': {'price': 1, 'inventory': 15}
}

mc = FastFood('McDonalds', 'Fast Food', menu, True)

print(mc.order('burger', 5))  # 25
print(mc.order('burger', 15))  # Requested quantity not available
print(mc.order('soup', 5))  # Dish not available
