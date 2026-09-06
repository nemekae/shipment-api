from enum import Enum

from pydantic import BaseModel, Field  # pyright: ignore[reportMissingImports]


# enum is a class that inherits from the Enum class. It is used to define a set of named values that can be used as constants in the code. In this case, the ShipmentStatus enum defines the possible statuses of a shipment, such as "available", "placed", "In-transit", "Out-for-delivery", and "delivered". Each status is represented as a string value.
class ShipmentStatus(str, Enum):
    available = "available"
    placed = "placed"
    in_transit = "In-transit"
    out_for_delivery = "Out-for-delivery"
    delivered = "delivered"

class BaseShipment(BaseModel):
    content: str
    weight: float = Field(le=30, description="Weight of the shipment in kg")
    destination: int 
    status: ShipmentStatus


class ShipmentRead(BaseShipment):
    status: ShipmentStatus


class ShipmentCreate(BaseShipment):
    pass


class ShipmentUpdate(BaseModel):
    status: ShipmentStatus


