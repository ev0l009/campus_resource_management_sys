from exceptions import DuplicateNameError
from exceptions import InvalidFellowIDError
from exceptions import InvalidResourceIDError
from exceptions import InvalidQuantityError
from exceptions import DuplicateIDError

def require_no_dupilcate_name(name: str, names_list: list[str]):
    if name in names_list:
        raise DuplicateNameError("Err: Resource with this name already exists.")

def require_no_dupilcate_id(id: str, ids_list: list[str]):
    if id in ids_list:
        raise DuplicateIDError("Err: Resource with this ID already exists.")

def validate_fellow_id(id: str, ids_list: list[str]):
    if id not in list(ids_list):
        raise InvalidFellowIDError("Err: Invalid Fellow ID")

def validate_resource_id(id: str, ids_list: list[str]):
    if id not in ids_list:
        raise InvalidResourceIDError("Err: Invalid Resource ID")

def validate_quantity(quantity: int, available: int):
    if quantity <= 0:
        raise InvalidQuantityError("Err: Borrow at least a unit of an item")
    if quantity > available:
        raise InvalidQuantityError("Err: Quantity exceeds available stocks.")