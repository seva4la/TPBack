import uvicorn
from fastapi import FastAPI
from api import router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Multitasker")
origins = ["*"]
app.include_router(router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)