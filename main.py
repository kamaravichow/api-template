from fastapi import FastAPI, WebSocket

app = FastAPI(debug=True)


@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}
