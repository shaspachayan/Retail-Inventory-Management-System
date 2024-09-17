class Product:
    inventory = []
    def __init__(self, product_id,name,category,quantity,price,supplier):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier

    @classmethod
    def add_product(cls, name, category, quantity, price, supplier):
        product_id = cls.inventory[-1].product_id +1 if len(cls.inventory) > 0 else 0
        new_product = cls(product_id,name,category,quantity,price,supplier)
        return "New Product Added Successfully"
    
    @classmethod
    def update_product(cls, product_id, quantity= None, price= None, supplier= None):
        for product in cls.inventory:
            if product.product_id == product_id:
                if product.quantity is not None:
                    product.quantity = quantity
                if product.price is not None:
                    product.price = price
                if product.supplier is not None:
                    product.supplier = supplier
                return f"{cls.inventory.product_id} is Updated Successfully"
        return f"There is no product with product id : {product_id}"

    @classmethod
    def delete_product(cls, product_id):
        for index, product in enumerate(cls.inventory):
            if product.product_id == product_id:
                del cls.inventory[index]
                return f"{cls.inventory[index]} is Successfully Deleted"
        return f"There is no product with product id : {product_id}"


class Order:
    def __init__(self, order_id, products, customer_info =None):
        self.order_id = order_id
        self.products = products
        self.customer_info = customer_info

    def place_order(self,product_id, quantity, customer_info =None):
        for product in Product.inventory:
            if product.product_id == product_id and product.quantity >= quantity: 
                product.quantity -= quantity 
                self.products.append((product_id, quantity))  
                if customer_info: 
                    self.customer_info = customer_info
                return f"Order placed successfully. Order ID: {self.order_id}"  
        return "Order could not be placed. Product not found or insufficient quantity."



p1 = Product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A")
update_p1 = Product.update_product(1, quantity=45, price=950)
delete_p1 = Product.delete_product(1)
order = Order(order_id=1, products=[])
order_placement = order.place_order(1, 2, customer_info="John Doe")




