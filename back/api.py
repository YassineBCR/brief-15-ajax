import fastapi as fastapi
import uvicorn as uvicorn

app = fastapi.FastAPI()

if __name__ == "__main__":
    uvicorn.run(app)


