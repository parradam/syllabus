from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/health")
def get_health() -> Response:
    return Response("ok")
