from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from fastapi.responses import JSONResponse

app = FastAPI()


class BookRequest(BaseModel):
    id: int
    title: str = Field(..., title="id not need")
    author: str = Field(..., title="author")
    description: str = Field(..., title="description", max_length=100)
    rating: float = Field(..., title="rating", gt=0, lt=11)  # 注意：这里lt=11是示例，实际应为lt=10


@app.post("/books/")
async def add_book(book: BookRequest):
    # 假设这里进行了书籍的添加逻辑
    # ...
    # 自定义响应体，包含类似字段标题的信息
    response_data = {
        "id": book.id,
        "title": book.title,
        "author": book.author,
        "description": book.description,
        "rating": book.rating
    }
    return JSONResponse(content=response_data)
