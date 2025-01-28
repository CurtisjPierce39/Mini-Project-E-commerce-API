from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields, validate
from marshmallow import ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Cjp007Cjp!@localhost/e_commerce_db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class CustomerSchema(ma.Schema):
    name = fields.String(required=True)
    email = fields.String(required=True)
    phone = fields.String(required=True)

    class Meta:
        fields = ("name", "email", "phone", "id")

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
#-----------------------------------------------------------------------------

class ProductsSchema(ma.Schema):
    name = fields.String(required=True, validate=validate.Length(min=1))
    price = fields.Float(required=True, validate=validate.Range(min=0))

    class Meta:
        fields = ("id", "name", "price")

product_schema = ProductsSchema()
products_schema = ProductsSchema(many=True)
#---------------------------------------------------------------------------------

class CustomerAccountSchema(ma.Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)

    class Meta:
        fields = ("id", "username", "password", "customer_id")

account_schema = CustomerAccountSchema()
accounts_schema = CustomerAccountSchema(many=True)
#------------------------------------------------------------------------------------

class OrderSchema(ma.Schema):
    date = fields.Date(required=True)
    product_id = fields.Integer(required=True)

    class Meta:
        fields = ("id", "date", "customer_id", "product_id")

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
#------------------------------------------------------------------------------------

class Customer(db.Model):
    __tablename__ = 'Customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(320))
    phone = db.Column(db.String(15))
    orders = db.relationship('Order', backref='customer')

#Many to Many
order_product = db.Table('Order_Product',
        db.Column('order_id', db.Integer, db.ForeignKey('Orders.id'), primary_key=True),
        db.Column('product_id', db.Integer, db.ForeignKey('Products.id'), primary_key=True)
)

class Order(db.Model):
    __tablename__ = 'Orders'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('Customers.id'), nullable=False)
    products = db.relationship('Product', secondary=order_product, back_populates="orders")

#One to One
class CustomerAccount(db.Model):
    __tablename__ = 'Customer_Account'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('Customers.id'))
    customer = db.relationship('Customer', backref='customer_account', uselist=False)

class Product(db.Model):
    __tablename__ = 'Products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    orders = db.relationship('Order', secondary=order_product, back_populates="products")

@app.route('/')
def home():
    return "Welcome"

#Customer Routes---------------------------------------------------------------------------------------------------

@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return customers_schema.jsonify(customers)

@app.route('/customers', methods=['POST'])
def add_customer():
    try:
        #Validate and deserialize
        customer_data = customer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_customer = Customer(name=customer_data['name'], email=customer_data['email'], phone=customer_data['phone'])
    db.session.add(new_customer)
    db.session.commit()
    return jsonify({"message": "New Customer Added Successfully!"}), 201

@app.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    customer = Customer.query.get_or_404(id)
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    customer.name = customer_data['name']
    customer.email = customer_data['email']
    customer.phone = customer_data['phone']
    db.session.commit()
    return jsonify({"message": "Customer details updated successfully!"})

@app.route('/customer/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.query.get_or_404(id)
    db.session.delete(customer)
    db.session.commit()
    return jsonify({"message": "Customer removed successfully"})

@app.route('/customers/<int:id>', methods=['GET'])
def get_customer(id):
    customer = Customer.query.get_or_404(id)
    return jsonify({"message": "Customer updated successfully"})

#Customer Account Routes---------------------------------------------------------------------------------------------------

@app.route('/customer_account', methods=['GET'])
def get_customer_accounts():
    customer_accounts = CustomerAccount.query.all()
    return accounts_schema.jsonify(customer_accounts)

@app.route('/customer_account', methods=['POST'])
def add_account():
    try:
        #Validate and deserialize
        account_data = account_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_account = CustomerAccount(username=account_data['username'], password=account_data['password'], customer_id=account_data['customer_id'])
    db.session.add(new_account)
    db.session.commit()
    return jsonify({"message": "New Account Added Successfully!"}), 201

@app.route('/customer_account/<int:id>', methods=['PUT'])
def update_account(id):
    account = CustomerAccount.query.get_or_404(id)
    try:
        account_data = account_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    account.username = account_data['username']
    account.email = account_data['password']
    db.session.commit()
    return jsonify({"message": "Account details updated successfully!"})

@app.route('/customer_account/<int:id>', methods=['DELETE'])
def delete_account(id):
    account = CustomerAccount.query.get_or_404(id)
    db.session.delete(account)
    db.session.commit()
    return jsonify({"message": "Customer Account removed successfully"})

# #Product Routes--------------------------------------------------------------------------------------

@app.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return products_schema.jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    try:
        #Validate and deserialize
        product_data = product_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_product = Product(name=product_data['name'], price=product_data['price'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "New Product Added Successfully!"}), 201

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    product.name = product_data['name']
    product.price = product_data['price']
    db.session.commit()
    return jsonify({"message": "Product details updated successfully!"})

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product removed successfully"})

# #Order Routes------------------------------------------------------------------------------------------------

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return orders_schema.jsonify(orders)

@app.route("/orders",methods=["POST"])
def create_order():
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages),400
    new_order = Order(customer_id = order_data["customer_id"])
    for product_id in order_data["products"]:
        product = Product.query.get_or_404(product_id)
        new_order.products.append(product)
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"message": "New Order Added Successfully!"}), 201

@app.route('/orders/<int:id>', methods=['PUT'])
def update_order(id):
    order = Order.query.get_or_404(id)
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    order.date = order_data['date']
    order.customer_id = order_data['customer_id']
    order.product_id = order_data['product_id']
    db.session.commit()
    return jsonify({"message": "Order details updated successfully!"})

@app.route('/orders/<int:id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get_or_404(id)
    db.session.delete(order)
    db.session.commit()
    return jsonify({"message": "Order removed successfully"})

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
