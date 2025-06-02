import uvicorn
from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from controllers.provinceroutes import router as province_router

config = dotenv_values(".env")

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(province_router, tags=["province"], prefix="/api/v1")





# Your application code here

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
