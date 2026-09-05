from enum import Enum

from pydantic import BaseModel, Field  # pyright: ignore[reportMissingImports]


class ShipmentStatus(str, Enum):
    available = "available"
    placed = "placed"
    in_transit = "In-transit"
    out_for_delivery = "Out-for-delivery"
    delivered = "delivered"
   
class Shipment(BaseModel):
    content: str
    weight: float = Field(le=30, description="Weight of the shipment in kg")
    destination: int 


class ShipmentRead(Shipment):
    status: ShipmentStatus


class ShipmentCreate(Shipment):
    status: ShipmentStatus


class ShipmentUpdate(BaseModel):
    status: ShipmentStatus


