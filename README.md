For a detailed explanation of this project, please tap here: https://shaspachayan.super.site/projects/projects/retail-inventory-management-system

# Retail-Inventory-Management-System

We defined two classes `Product` and `Order`, using the implementation requirements detailed below:

# `Product`

- Constructor parameter(s): `self`, `product_id`, `name`, `category`, `quantity`, `price`, and `supplier`.
- Class-level variable(s): `inventory`.

## `Product` class method(s)

### `add_product()`
- Parameter(s): `cls`, `name`, `category`, `quantity`, `price`, and `supplier`.
- Behavior: 
    - Define the `product_id` assuming it's auto-generated incrementally, without any duplicate `product_id` values.
    - Define a `new_product` variable that will call the constructor of the Product class.
    - Return the message `"Product added successfully"` to know that the product was added successfully.

### `update_product()`
- Parameter(s): `cls`, `product_id`, `quantity`, `price`, and `supplier`.
    - `quantity`, `price`, and `supplier` should have default values of `None`. 
- Behavior: 
    - Check if the `product_id` already exists in the `inventory`.
    - If `product_id` exists, check for the given parameters in the method if they have a value and update accordingly the product.
    - Return either one of these messages: `"Product information updated successfully"` or `"Product not found"`.

### `delete_product()`
- Parameter(s): `cls`, `product_id`.
- Behavior: 
    - Check in the inventory list if the given `product_id` was passed as a parameter.
    - If `product_id` exists then remove the product from the list.
    - Return either one of these messages: `"Product deleted successfully"` or `"Product not found"`.


# `Order`

- Constructor parameter(s): `self`, `order_id`, `products`, and `customer_info`.
    - `customer_info` should have a default value of `None`. 

## `Order` method(s)

### `place_order()`
- Parameter(s): `self`, `product_id`, `quantity`, and `customer_info`.
    - `customer_info` should have a default value of `None`.
- Behavior: 
    - Append to the `products` list a tuple containing `product_id` and `quantity`.
    - Assume that each order can only take **one** product. 
    - Return the message: `"Order placed successfully. Order ID: {self.order_id}"`.
