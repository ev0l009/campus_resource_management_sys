from typing import Self

from typing import TypedDict

from exceptions import ResourceNotFoundError
from exceptions import InvalidQuantityError

from helpers import require_no_dupilcate_name
from helpers import require_no_dupilcate_id
from helpers import validate_resource_id
from helpers import validate_fellow_id
from helpers import  validate_quantity

class ResourceType(TypedDict):
    id: str
    name: str
    category: str
    total: int
    available: int

class LogType(TypedDict):
    fellow_name: str
    fellow_id: str
    item_name: str
    item_id: str
    units_borrowed: int
    action: str

class Inventory:
    def __init__(
        self, 
        resources: list[ResourceType],
        fellows: dict[str, str],
        borrow_records: list[LogType] 
    ) -> None:
        self.resources = resources
        self.resource_names = [res["name"].strip().lower() for res in resources]
        self.resource_ids = [res["id"] for res in resources]
        self.fellows = fellows
        self.borrow_records = borrow_records

    def add_resource(
        self, 
        id: str, 
        name: str, 
        category: str, 
        total: int, 
        available: int
    ) -> Self:
        
        require_no_dupilcate_name(name, self.resource_names)
        require_no_dupilcate_id(id, self.resource_ids)

        self.resources.append({
            "id": id,
            "name": name,
            "category": category,
            "total": total,
            "available": available
        })
        self.resource_ids.append(id)
        return self

    def get_resource_by_id(self, resource_id: str) -> ResourceType:
        validate_resource_id(resource_id, self.resource_ids)
        for resource in self.resources:
            if resource_id == resource["id"]:
                return resource
        raise ResourceNotFoundError("Err: Couldn't find resource.")

    def get_resource_by_name(self, resource_name: str) -> ResourceType:
        for resource in self.resources:
            if resource["name"].strip().lower() == resource_name.strip().lower():
                return resource
        raise ResourceNotFoundError("Err: Couldn't find resource.")

    def log_action(
        self,
        fellow_name: str,
        fellow_id: str,
        item_name: str,
        item_id: str,
        units_borrowed:int,
        action: str
    ) -> None:
        self.borrow_records.append({
            "fellow_name": fellow_name,
            "fellow_id": fellow_id,
            "item_name": item_name,
            "item_id": item_id,
            "units_borrowed": units_borrowed,
            "action": action
        })

    def display_borrow_logs(self) -> str:
        borrow_logs_str = ""

        for idx, log in enumerate(self.borrow_records):
            borrow_logs_str += (
                f"{idx+1}  {log['fellow_name']}  {log['fellow_id']}  {log['item_name']}  {log['item_id']}  {log['units_borrowed']}  {log['action']}\n"
            )

        return(
            "=========================\n"
            "     Inventory Logs\n"
            "=========================\n"
            f"{borrow_logs_str}"
        )

    def borrow_resource(
        self, 
        fellow_id: str, 
        resource_id: str, 
        quantity: int
    ) -> Self:
        validate_fellow_id(fellow_id, list(self.fellows))
        resource = self.get_resource_by_id(resource_id)
        validate_quantity(quantity)

        if quantity > resource["available"]:
            raise InvalidQuantityError("Err: Quantity exceeds available stocks.")

        resource["available"] -= quantity

        self.log_action(
            self.fellows[fellow_id],
            fellow_id,
            resource["name"],
            resource_id,
            quantity,
            "B"
        )

        return self

    def return_resource(
            self,
            fellow_id: str,
            resource_id: str,
            quantity: int
    ) -> Self:
        validate_fellow_id(fellow_id, list(self.fellows))
        validate_quantity(quantity)

        resource = self.get_resource_by_id(resource_id)

        resource["available"] += quantity

        self.log_action(
            self.fellows[fellow_id],
            fellow_id,
            resource["name"],
            resource_id,
            quantity,
            "R"
        )
        return self
    
    def list_resources(self) -> str:
        resource_list_str = ""

        for idx, res in enumerate(self.resources):
            resource_list_str += (
                f"{idx+1}  {res['id']}  {res['name']}  {res['category']}  {res['available']}  {res['total']}\n"
            )

        return(
            "=========================\n"
            "     Resource List\n"
            "=========================\n"
            f"{resource_list_str}"
        )