from fastapi import FastAPI,Request
from dtos import ProductDTO
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
def greet_user(request: Request):
    query_params = dict(request.query_params)
    print(query_params)
    return {
        "greet":f"Hello, {query_params.get('name')}! You are {query_params.get('age')}."
    }


# Different types of HTTP methods
# How to validate data -DTOS
# How to call different HTTP methos





# POST request example
@app.post("/create_product")
def create_product(product_data:ProductDTO):
#  pydentic
    product_data=product_data.model_dump()
    print(product_data)
    products.append(product_data)
    return {
        "status": "success",
        "message": "Product created successfully!",
        "data":products
    }

# body
# requiest_headers
# query_params


@app.put("/update_product/{product_id}")
def update_product(product_id:int,product_data:ProductDTO):
    for index,product in enumerate(products):
      if product.get("id") == product_id:
        product_data=product_data.model_dump()
        products[index].update(product_data)
        return {
            "status": "success",
            "message": f"Product with ID {product_id} updated successfully!",
            "data": products[index]
        }
    return {
        "error": f"Product with ID {product_id} not found!" 
    }       

# Delete request example

@app.delete("/delete_product/{product_id}")
def delete_product(product_id:int):
    for index,product in enumerate(products):
         if product.get("id") == product_id:
             deleted_product=products.pop(index)
             return {
                "status": "success",
                "message": f"Product with ID {product_id} deleted successfully!",
                "data":  deleted_product
            }
    return {
        "error": f"Product with ID {product_id} not found!"
    }