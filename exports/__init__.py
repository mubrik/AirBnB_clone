from typing import Dict, Union
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review

Model_Type = Union[BaseModel, Place, City, Review, Amenity]

valid_classes: Dict[str, Model_Type] = {
    "BaseModel": BaseModel,
    "Place": Place,
    "City": City,
    "Review": Review,
    "Amenity": Amenity,
}
