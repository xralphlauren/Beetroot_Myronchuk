class Product:
    def __init__(self, typ, name, price):
        self.type = typ
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.prod_dict = dict()     # Данные хранятся в формате {'Apple': [amount, price, type, discount]}
        self.income = 0

    def add(self, product, amount):
        if product.name in self.prod_dict:
            self.prod_dict[product.name][0] += amount
        else:
            count_price = product.price / 100 * 30
            self.prod_dict[product.name] = [amount, product.price + count_price, product.type, 0]

    def get_all_products(self):
        return self.prod_dict

    def get_product_info(self, name):
        if name not in self.prod_dict:
            return ValueError('Данного товара нет в магазине')
        else:
            out = (name, self.prod_dict[name][0])
            return out

    def set_discount(self, identifier, percent, identifier_type='name'):
        if identifier not in self.prod_dict:
            return ValueError('Данного товара нет в магазине')
        else:
            self.prod_dict[identifier][3] = percent

        if identifier_type != 'name':
            for k, v in self.prod_dict:
                if v[2] == identifier_type:
                    v[3] = percent

    def sell_product(self, product_name, amount):
        if product_name not in self.prod_dict:
            return ValueError('Данного товара нет в магазине')
        elif amount > self.prod_dict[product_name][0]:
            return ValueError('В магазине нет такого количества товара')
        else:
            if self.prod_dict[product_name][3] == 0:
                total_price = self.prod_dict[product_name][1]
            else:
                count_discount = (self.prod_dict[product_name][1] / 100) * self.prod_dict[product_name][3]
                total_price = self.prod_dict[product_name][1] - count_discount
            self.prod_dict[product_name][0] -= amount
            self.income = total_price * amount

    def get_income(self):   # возвращает сумму сколько заработанных экземпляром ProductStore.
        return self.income


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)
s.set_discount('Football T-Shirt', 7)
s.sell_product('Football T-Shirt', 5)
assert s.get_product_info('Ramen') == ('Ramen', 290)
assert s.get_product_info('Football T-Shirt') == ('Football T-Shirt', 5)
print(s.get_income())
