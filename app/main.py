from fastapi import FastAPI, APIRouter


# https://christophergs.com/tutorials/ultimate-fastapi-tutorial-pt-1-hello-world/
# 1 We instantiate a FastAPI app object, which is a
# Python class that provides all the functionality for your API.
app = FastAPI(title="Recipe API", openapi_url="/openapi.json")

# 2 We instantiate an APIRouter which is how we can group our API endpoints (and specify versions and other config which we will look at later)
api_router = APIRouter()

# 3 By adding the @api_router.get("/", status_code=200)
# decorator to the root function, we define a basic GET endpoint for our API.
@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root Get
    """
    return {"msg": "Hello, World!"}


# 4 to register the router
app.include_router(api_router)


# 5 The __name__ == "__main__" conditional applies when a module is called directly,
# i.e. if we run python app/main.py. In this scenario, we need to import uvicorn since FastAPI
# depends on this web server (which we’ll talk more about later)
if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
    # by default, the framework is based on OpenAPI,
    # there are multiple options, 2 included by default
    # https://fastapi.tiangolo.com/features/:
    # - http://127.0.0.1:8000/redoc
    # - http://127.0.0.1:8000/docs
