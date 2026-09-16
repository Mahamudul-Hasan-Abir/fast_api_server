from fastapi import FastAPI
from mockData import products
app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI server!"}



@app.get("/products")

def get_products():

    return products




# Path params
@app.get("/product/{product_id}")

def get_single_product(product_id:int):
    # if product available with the id return product,else return error message
  
    for product in products:
        if product.get("id") == product_id:
            return product
    return {"error": "Product not found!"}


# query params

@app.get("/greet")
def greet_user(name:str,age:int ):
    return {"message": f"Hello, {name}! You are {age}."}