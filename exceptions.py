class InventoryError(Exception):
    pass

class DuplicateNameError(InventoryError):
    pass

class DuplicateIDError(InventoryError):
    pass

class InvalidFellowIDError(InventoryError):
    pass

class InvalidResourceIDError(InventoryError):
    pass

class InvalidQuantityError(InventoryError):
    pass

class ResourceNotFoundError(InventoryError):
    pass