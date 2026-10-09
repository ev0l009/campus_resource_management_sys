from inventory import Inventory

from exceptions import DuplicateNameError
from exceptions import DuplicateIDError
from exceptions import InvalidResourceIDError
from exceptions import InvalidFellowIDError
from exceptions import ResourceNotFoundError
from exceptions import InvalidQuantityError
from exceptions import DatabaseError

menu_options = (
    "===========================\n"
    "  Campus Inventory System\n"
    "===========================\n"
    "1. Add resource\n"
    "2. Borrow resource\n"
    "3. Return resource\n"
    "4. Get resource by ID\n"
    "5. Get resource by name\n"
    "6. List resources\n"
    "7. Show inventory logs\n"
    "8. Exit\n"
    "Select an option: "
)
inventory = Inventory()

def campus_inventory_sys():

    try:
        print("Attempting to load inventory...")
        inventory.load_data()
    except DatabaseError as err:
        print(f"\nOperation failed: {err}")
    else:
        print("\nLoading operation successful.\n")

    opt = "0"
    while opt != "8":

        if opt == "0":
            opt = input(menu_options)

        elif opt == "1":
            print(
                "\n        Add Resource\n"
                "===========================\n"
            )
            try:
                inventory.add_resource(
                    input("Enter resource ID: "),
                    input("Enter resource name: "),
                    input("Enter resource category: "),
                    int(input("Enter total units: ")),
                    int(input("Enter available units: "))
                )
            except DuplicateNameError as err:
                print(err)
            except DuplicateIDError as err:
                print(err)
            else:
                print("\nResource added successfully.\n")

            opt = "0"

        elif opt == "2":
            print(
                "\n     Borrow Resource\n"
                "===========================\n"
            )
            try:
                inventory.borrow_resource(
                    input("Fellow ID: "),
                    input("Resource ID: "),
                    int(input("Enter quantity: "))
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
                print("Operation successful.")

            opt = "0"

        elif opt == "3":
            print(
                "\n     Return Resource\n"
                "===========================\n"
            )
            try:
                inventory.return_resource(
                    input("Fellow ID: "),
                    input("Resource ID: "),
                    int(input("Enter quantity: "))
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
                print("Operation successful.")

            opt = "0"

        elif opt == "4":
            print(
                "\n   Get resource by ID\n"
                "===========================\n"
            )
            try:
                resource = inventory.get_resource_by_id("R004")
            except InvalidResourceIDError as err:
                print(err)
            except ResourceNotFoundError as err:
                print(err)
            else:
                print(
                    "--------------------------------------\n"
                    f"   {resource['name'].capitalize()}\n"
                    "--------------------------------------\n"
                    f"Resource name: {resource['name']}"
                    f"Resource id:   {resource['id']}"
                    f"Category: {resource['category']}"
                    f"Total units: {resource['total']}"
                    f"Available units: {resource['available']}"
                )

            opt = "0"

        elif opt == "5":
            print(
                "\n   Get resource by name\n"
                "===========================\n"
            )
            try:
                resource = inventory.get_resource_by_name("LAPtop")
            except ResourceNotFoundError as err:
                print(err)
            else:
                print(resource)

            opt = "0"

        elif opt == "6":
            print(inventory.list_resources())

            opt = "0"

        elif opt == "7":
            print(inventory.display_borrow_logs())

            opt = "0"
        elif opt not in ["0","1","2","3","4","5","6","7","8"]:
            print("Invalid option. Try again...")

            opt = "0"

    try:
        print("Attmepting database write...")
        inventory.save_data()
    except DatabaseError as err:
        print(err)
        print("\nDatabase write unsuccessful.\nSession not saved...")
    else:
        print("\nDatabase write successful.\nSession saved.")
    finally:
        print("\nExiting...")
        
campus_inventory_sys()