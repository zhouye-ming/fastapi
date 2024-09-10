from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {'标题': '标题 1', '作者': '作者1', '类别': '科学'},
    {'标题': '标题 2', '作者': '作者2', '类别': '科学'},
    {'标题': '标题 3', '作者': '作者3', '类别': '历史'},
    {'标题': '标题 4', '作者': '作者4', '类别': '数学'},
    {'标题': '标题 5', '作者': '作者5', '类别': '数学'},
    {'标题': '标题 6', '作者': '作者2', '类别': '历史'}
]


@app.get("/books")  # 获取全部书籍
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}")  # 动态函数传入书名dynamic_param
async def read_all_books(book_title: str):
    for book in BOOKS:
        if book.get('标题').casefold() == book_title.casefold():
            return book


@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('类别').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/by_author/")   #放在动态参数前面就没事
async def read_books_by_author_path(author: str):
    book_to_return = []
    for book in BOOKS:
        if book.get("作者").casefold() == author.casefold():
            book_to_return.append(book)
    return book_to_return


@app.get("/books/{book_author}/")
async def read_category_by_query(author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('类别').casefold() == category.casefold() \
                and book.get("作者").casefold() == author.casefold():
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book")
async def create_book(new_book=Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book=Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('标题').casefold() == updated_book.get('标题').casefold():
            BOOKS[i] = updated_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('标题').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break


'''使用路径或查询参数获取特定作者的所有书籍'''

'''
@app.get("/books/by_author/{author}")   此时如果把动态参数删除便无法查询，因为前面有一个动态参数，fastapi里面顺序十分重要
async def read_books_by_author_path(author: str):   
    book_to_return = []
    for book in BOOKS:
        if book.get("作者").casefold() == author.casefold():
            book_to_return.append(book)
    return book_to_return
'''

