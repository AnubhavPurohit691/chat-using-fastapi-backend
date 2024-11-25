from fastapi import FastAPI
from router.userrouter import router as user_router
app = FastAPI()

# Include the user router under the /users path
app.include_router(user_router, prefix="/users", tags=["users"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI app!"}