from fastapi import FastAPI, APIRouter, Query

from app.recipe_data import RECIPES
from app.schemas import RecipeSearchResults, Recipe, RecipeCreate

from typing import Optional


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
@api_router.get("/recipe/{recipe_id}", status_code=200, response_model=Recipe)
def fetch_recipe(*, recipe_id: int) -> dict:
    """
    Fetch a single recipe by ID
    """

    result = [recipe for recipe in RECIPES if recipe["id"] == recipe_id]
    if result:
        return result[0]


# New addition, query parameter
# https://fastapi.tiangolo.com/tutorial/query-params/
@api_router.get("/search/", status_code=200, response_model=RecipeSearchResults)
def search_recipes(
    *,
    keyword: Optional[str] = Query(None, min_length=3, example="chicken"),  # 2
    max_results: Optional[int] = 10
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


# New addition, using Pydantic model `RecipeCreate` to define
# the POST request body
# 1
@api_router.post("/recipe/", status_code=201, response_model=Recipe)
def create_recipe(*, recipe_in: RecipeCreate) -> dict:  # 2
    """
    Create a new recipe (in memory only)
    """
    new_entry_id = len(RECIPES) + 1
    recipe_entry = Recipe(
        id=new_entry_id,
        label=recipe_in.label,
        source=recipe_in.source,
        url=recipe_in.url,
    )
    RECIPES.append(recipe_entry.dict())  # 3

    return recipe_entry


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
