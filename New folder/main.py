from fastapi import FastAPI , Depends,status,HTTPException
from mydb.database import engine,SessionLocal
from mydb import models,schemas
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def welcome():
    return 'hello'

@app.get("/books",tags=["Books"])
async def get_all(db: Session = Depends(get_db)):
    books = db.query(models.Books).all()
    return books

@app.get("/books/{title}",tags=["Books"])
async def search_by_title(title,db:Session = Depends(get_db)):
    book = db.query(models.Books).filter(models.Books.title == title).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f'Book with the title : [{title}] is not available')

    return book

@app.post('/books',status_code=status.HTTP_201_CREATED,tags=["Books"])
async def create(request:schemas.Book , db:Session = Depends(get_db)):
    new_book = models.Books(title = request.title ,auther = request.auther ,image = request.image ,discription = request.discription,publish_date = request.publish_date)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.put("/books/{id}",tags=["Books"])
async def update(id,request:schemas.Book,db:Session = Depends(get_db)):
    book = db.query(models.Books).filter(models.Books.id==id)
    my_book = models.Books

    if request.title != "string":
        book.update({'title' : request.title})
    else:
        book.update({'title' : my_book.title})
    
    if request.auther != "string":
        book.update({'auther' : request.auther})
    else:
        book.update({'auther' : my_book.auther})

    if request.image != "string":
        book.update({'image' : request.image})
    else:
        book.update({'image' : my_book.image})

    if request.discription != "string":
        book.update({'discription' : request.discription})
    else:
        book.update({'discription' : my_book.discription})

    if request.publish_date != "string":
        book.update({'publish_date' : request.publish_date})
    else:
        book.update({'publish_date' : my_book.publish_date})

    db.commit()
    return 'updated'


@app.delete('/books/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session = Depends(get_db)):
 book=db.query(models.Books).filter(models.Books.id==id).delete(synchronize_session=False)
 db.commit()
 return "done"

#--------------------Users------------------------

@app.get("/users",tags=["Users"])
async def get_all(db: Session = Depends(get_db)):
    Users = db.query(models.Users).all()
    return Users

@app.get("/users/{id}",tags=["Users"])
async def get_by_id(id,db:Session = Depends(get_db)):
    User = db.query(models.Users).filter(models.Users.id == id).first()
    
    if not User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f'User with the id : [{id}] is not in our database')
    
    return User

@app.post('/users', status_code=status.HTTP_201_CREATED, tags=["Users"])
async def create_user(request: schemas.User, db: Session = Depends(get_db)):
    existing_user = db.query(models.Users).filter_by(email=request.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail=f'User : [{request.name}] already exists')

    new_user = models.Users(name=request.name, email=request.email, mobile=request.mobile)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.put("/users/{id}",tags=["Users"])
async def update(id,request:schemas.User,db:Session = Depends(get_db)):
    user  = db.query(models.Users).filter(models.Users.id==id)
    my_user = models.Users

    if request.name != "string":
        user.update({'name' : request.name})
    else:
        user.update({'name' : my_user.name})
    
    if request.mobile != "string":
        user.update({'mobile' : request.mobile})
    else:
        user.update({'mobile' : my_user.mobile})

    if request.email != "string":
        user.update({'email' : request.email})
    else:
        user.update({'email' : my_user.email})

    db.commit()
    return 'updated'

@app.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT,tags=["Users"])
async def delete(id,db:Session = Depends(get_db)):
    User = db.query(models.Users).filter(models.Users.id == id)

    if not User:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f'User with the id : [{id}] is not in our database')
    
    User.delete()
    db.commit()
    return 'Done'


