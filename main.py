from fastapi import FastAPI
import uvicorn

from api.products import router as product_router

app = FastAPI()


@app.get('/')
def hello():
    return {'message': 'Hello'}

app.include_router(product_router)

if __name__ == '__main__':
    uvicorn.run(
        app='main:app',
        host='127.0.0.1',
        port=5000,
        reload=True
    )
