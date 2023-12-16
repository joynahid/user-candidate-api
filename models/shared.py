from typing import Annotated
from bson import ObjectId
from pydantic import AfterValidator, BeforeValidator, ValidationError


def validate_object_id(id_str: str) -> ObjectId:
    try:
        ObjectId(id_str)
        return id_str
    except Exception as err:
        print(err)
        raise ValueError("Invalid ObjectId format")


PyObjectId = Annotated[str, BeforeValidator(str), AfterValidator(validate_object_id)]
