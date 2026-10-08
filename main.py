from inventory import ResourceType
from inventory import LogType

from inventory import Inventory

from exceptions import DuplicateNameError
from exceptions import DuplicateIDError
from exceptions import InvalidResourceIDError
from exceptions import InvalidFellowIDError
from exceptions import ResourceNotFoundError
from exceptions import InvalidQuantityError

resources: list[ResourceType] = [
  {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
  {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
  {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
]
fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}
borrow_records: list[LogType] = []

inventory = Inventory(resources,fellows,borrow_records)

try:
    inventory.add_resource(
        "R004",
        "Mouse",
        "Accessories",
        12,
        12
    )
except DuplicateNameError as err:
    print(err)
except DuplicateIDError as err:
    print(err)
# else:
#     print(inventory.list_resources())

try:
    resource = inventory.get_resource("R004")
except InvalidResourceIDError as err:
    print(err)
except ResourceNotFoundError as err:
    print(err)
# else:
#     print(resource)

try:
    inventory.borrow_resource(
        "F001",
        "R001",
        2
    )
except InvalidFellowIDError as err:
    print(err)
except InvalidResourceIDError as err:
    print(err)
except ResourceNotFoundError as err:
    print(err)
except InvalidQuantityError as err:
    print(err)
else:
    print(inventory.list_resources())
    print(inventory.display_borrow_logs())