from fastapi import FastAPI

app = FastAPI(
    title="One time secret"
)


@app.get("/")
def root():
    return {"message": "Hello! It's one time secret service"}
