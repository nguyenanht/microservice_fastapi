from typing import Optional

from fastapi import FastAPI, APIRouter

RECIPES = [
    {
        "id": 1,
        "label": "Chicken Vesuvio",
        "source": "Serious Eats",
        "url": "http://www.seriouseats.com/recipes/2011/12/chicken-vesuvio-recipe.html",
    },
    {
        "id": 2,
        "label": "Chicken Paprikash",
        "source": "No Recipes",
        "url": "http://norecipes.com/recipe/chicken-paprikash/",
    },
    {
        "id": 3,
        "label": "Cauliflower and Tofu Curry Recipe",
        "source": "Serious Eats",
        "url": "http://www.seriouseats.com/recipes/2011/02/cauliflower-and-tofu-curry-recipe.html",
    },
]

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


# New addition, path parameter
# https://fastapi.tiangolo.com/tutorial/path-params/
# This is because FastAPI is coercing the input parameter type
# based on the function argument type hints. This is a handy way of preventing input errors.
@api_router.get("/recipe/{recipe_id}", status_code=200)
def fetch_recipe(*, recipe_id: int) -> dict:
    """
    Fetch a single recipe by ID
    """
    print(type(recipe_id))  # ADDED

    result = [recipe for recipe in RECIPES if recipe["id"] == recipe_id]
    if result:
        return result[0]


# New addition, query parameter
# https://fastapi.tiangolo.com/tutorial/query-params/
@api_router.get("/search/", status_code=200)
def search_recipes(
    keyword: Optional[str] = None, max_results: Optional[int] = 10
) -> dict:
    """
    Search for recipes based on label keyword
    """
    if not keyword:
        # we use Python list slicing to limit results
        # based on the max_results query parameter
        return {"results": RECIPES[:max_results]}

    results = filter(lambda recipe: keyword.lower() in recipe["label"].lower(), RECIPES)
    return {"results": list(results)[:max_results]}


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
