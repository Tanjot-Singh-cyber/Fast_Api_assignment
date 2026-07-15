from fastapi import FastAPI , HTTPException

app = FastAPI()

students = [
    {"id": 1, "name": "Akhil", "course": "Python",  "city": "Hyderabad"},
    {"id": 2, "name": "Sai",   "course": "FastAPI", "city": "Vijayawada"},
    {"id": 3, "name": "Ravi",  "course": "SQL",     "city": "Guntur"},
    {"id": 4, "name": "Kiran", "course": "Python",  "city": "Vizag"},
    {"id": 5, "name": "Meena", "course": "FastAPI", "city": "Chennai"}
]
products = [
    {"id": 1, "name": "Asus",         "category": "Electronics", "price": 50000},
    {"id": 2, "name": "Dell",         "category": "Electronics", "price": 60000},
    {"id": 3, "name": "iPhone",       "category": "Mobiles",     "price": 80000},
    {"id": 4, "name": "Samsung TV",   "category": "Electronics", "price": 45000},
    {"id": 5, "name": "Nike Shoes",   "category": "Fashion",     "price": 5000},
    {"id": 6, "name": "Office Chair", "category": "Furniture",   "price": 12000},
    {"id": 7, "name": "Water Bottle", "category": "Kitchen",     "price": 500},
    {"id": 8, "name": "Notebook",     "category": "Stationery",  "price": 100}
]
#/products
#/products?category=electronics

@app.get('/products')
def get_products(category : str | None = None):
    if category is not None :
        filtered_products = []
        for product in products :
            if product["category"].lower() == category.lower():
                filtered_products.append(product)
        return filtered_products
    return products


# @app.get('/students')
# def get_students(course : str | None = None):
#     if course is not None :
#         filtered_students = []
#         for student in students :
#             if student["course"].lower() == course.lower():
#                 filtered_students.append(student)
#         return filtered_students
#     return students 


@app.get('/students')
# http://127.0.0.1:8000/students?course=Pyhton&city=Hyderabad
def get_students(course : str | None = None , city : str | None = None ): 
        filtered_student = students 
        if course is not None :
            filtered_students = [
                student for student in students 
                if student["course"].lower() == course.lower()
            ]
        if city is not None :
            filtered_students = [
                student for student in students 
                if student["city"].lower() == city.lower()
            ]

        return filtered_students


# write fixed routes before dynamic routes
@app.get('/students/topper')
def get_student_topper():
    return {
        "name": " Tanjot Singh",
        "rank" : 1

    }

@app.get('/students/{student_id}')
def get_student_by_id(student_id: int):
    for student in students :
        if student["id"] == student_id :
            return student 
    # return {"error": " studnet not found"} 
    raise HTTPException(status_code= 404 , detail= "student not found")

# query parameters
# /students?course=python

