from fastapi import FastAPI

app = FastAPI()

 @app.get("/home")
 def home():
     return {
         "message" : "Welcome to my first FastAPi assignment"
     }

 @app.get("/about")
 def about():
     return {
         "student_name" : "Tanjot Singh",
         "Course" : "FastAPI",
         "Topic" : "Fast API assignment",
         "Status" : "Learning"
     }

 @app.get("/trainer")
 def about():
     return {
         "Name" : "John Doe",
         "Role" : "Trainer",
         "Subject" : "FastAPI"
     }

 @app.get("/courses")
 def about():
     return [
         {
             "id" : 1,
             "name" : "Python Basics",
             "duration" : "1 week"
         },

         {
             "id" : 2,
             "name" : "Cyber Security",
             "duration" : "1 week"
         },

         {
             "id" : 3,
             "name" : "Networking Fundamentals",
             "duration" : "1 week"
         }
     ]



 @app.get("/college")
 def about():
     return {
         "College name" : "MIET",
         "Location" : "Kot Bhalwal",
         "Department" : "Computer Science Engineering(Cybersecurity)",
         "Current_module" : "FastAPI Basics"
     }

 @app.get("/technologies")
 def about():
     return [
         "Python",
         "FastAPI",
         "JSON",
         "HTTP",
         "RestAPI" 
     ]
# Dynamic parameters 
 @app.get('/students/{student_id}')
 def get_students(student_id: int):
     return[ {
         "id" : 1,
         "name" : "Tanjot Singh",
         "age" : 21,
         "course" : "FastAPI"
     },
     {
         "id" : 2,
         "name" : "ayush",
         "age" : 22,
         "course" : "Cyber Security"
     },
     {
         "id" : 3,
         "name" : "Mahaal",
         "age" : 20,
         "course" : "Networking Fundamentals"
     }
     ]



#DYNAMIC PATH PARAMETERS
 @app.get('/courses/{course_id}')
 def get_course_by_id(course_id: str):
     return {
        
         "id" : course_id,  
         "name" : "Python Basics",
         "duration" : "1 week"
     }

 @app.get('/books/{book_id}/author/{author_id}')
def get_book_author(book_id: int, author_id: int):
     return {
         "book_id" : book_id,
         "author_id" : author_id,
         "book_name" : "Python Basics",
         "author_name" : "John Doe"
     }


 # /students/{student_id}/courses/{course_name}
 @app.get('/students/{student_id}/courses/{course_name}')
 def get_student_course(student_id: int, course_name: str):
    return {
         "student_id" : student_id,
        "course_name" : course_name
    }                                                                       
