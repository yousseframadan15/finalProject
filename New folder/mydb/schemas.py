from pydantic import BaseModel

class User(BaseModel):
   name : str
   email : str
   mobile : str

class ShowUser(BaseModel):
   name:str
   email:str   
   
class Book(BaseModel):
     title : str
     auther : str
     image : str
     discription : str
     publish_date : str

class ShowsBook(Book):
 pass
 class Config():
    Orm_mode=True



# from pydantic import BaseModel

# class Book(BaseModel):
#     title : str
#     auther : str
#     image : str
#     discription : str
#     publish_date : str
#     class Config():
#         orm_mode = True

# class User(BaseModel):
#     name : str
#     email : str
#     mobile : str

#     class Config():
#         orm_mode = True