from typing import Optional
import fastapi_cdn_host
from fastapi import FastAPI
from pydantic import Field,BaseModel

app = FastAPI()

fastapi_cdn_host.patch_docs(app)


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int] = Field(...,title='id not needed')
    title: str = Field(...,min_length=1)
    author: str = Field(...,min_length=1)
    description: str = Field(...,min_length=1, max_length=100)
    rating: int = Field(...,gt=-1, lt=10)

    class Config:
        schema_extra = {
            'example': {
                'title': '一本新书',
                'author': '夜冥',
                'description': '这是一本新书介绍',
                'rating': 5
            }
        }


BOOKS = [
    Book(1, '如何原神起号', '米孝子', '米孝子专武', 6),
    Book(2, '如何当赛博皇帝', '龙图', '典，孝,乐，急，蚌', 5),
    Book(4, '抽象是怎么养成的', '孙笑川', '坏事干尽', 1),
    Book(5, '如何名利双收', '顶针', '雪豹闭嘴', 7),
    Book(6, '如何喝迎宾酒', '野兽先辈', '十分甚至九分美味', 1),
    Book(7, '论道', '三清', '悟道', 0)
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.post("/create_book")
async def crete_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id + 1
    # else:
    #     book.id = 1
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1  # 三元运算符
    return book
