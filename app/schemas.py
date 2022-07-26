from pydantic import BaseModel, HttpUrl

from typing import Sequence
# pydantic :
# It’s a tool which allows you to be much more precise with your data structures.
# For example, up until now we have been relying
# on a dictionary to define a typical recipe in our project.
# With Pydantic we can define a recipe like this:

class Recipe(BaseModel):
    id: int
    label: str
    source: str
    url: HttpUrl


class RecipeSearchResults(BaseModel):
    results: Sequence[Recipe]


class RecipeCreate(BaseModel):
    label: str
    source: str
    url: HttpUrl
    submitter_id: int
