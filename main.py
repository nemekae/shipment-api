# pyright: reportMissingImports=false


from typing import Any

from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference

from schemas import Shipment, ShipmentCreate, ShipmentStatus, ShipmentUpdate

app = FastAPI()

# Let add a mini db of 7 different data elements

shipments = {
    12700: {
        "content": "TV board",
        "weight": 12.5,
        "destination": 1001,
        "status": "available",
    },
    12701: {
            "content": "staircase",
            "weight": 12.7,
            "destination": 1002,
            "status": "delivered",
        },
    12702: {
            "content": "wooden table",
            "weight": 12.4,
            "destination": 1003,
            "status": "In-transit",
        },
    12703: {
            "content": "wooden chair",
            "weight": 12,
            "destination": 1004,
            "status": "delivered",
        },
    12704: {
            "content": "bedframe",
            "weight": 12.5,
            "destination": 1005,
            "status": "In-transit",
        },
    12705: {
            "content": "wooden locker",
            "weight": 12.5,
            "destination": 1006,
            "status": "placed",
        },
    12706: {
            "content": "cupboard",
            "weight": 12.5,
            "destination": 1007,
            "status": "available",
        },
    12707: {
            "content": "gold tiles",
            "weight": 10,
            "destination": 1008,
            "status": "In-transit",
        },
}

# Define query parameter
@app.get("/shipment", response_model=Shipment)
def get_shipment(id: int | None = None):
    # Get the latest shipment if no id is provided
    if not id:
        id = max(shipments.keys())
        return shipments[id]
    # Display an error if shipment id provided is not available
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Give id does not exist"
        )
    return shipments[id]

# Define an endpoint for adding new shipments order:
@app.post("/shipment")
def submit_shipment(shipment: ShipmentCreate) -> dict[str, Any]:
    content = shipment.content
    weight = shipment.weight
    destination = shipment.destination

    new_id = max(shipments.keys()) + 1
    shipments[new_id] = {
       "content": content,
        "weight": weight,
        "destination": destination,
        "status": "placed", 
    }
    return shipments[new_id]


@app.patch("/shipment", response_model=Shipment)
def update_shipments(id: int, body: ShipmentUpdate) -> dict[str, Any]:
    #Update the provided fields
    shipments[id].update(body)
    return shipments[id]


@app.delete("/shipment")
def delete_shipment(id: int) -> dict[str, str]:
     shipments.pop(id)
     return {"detail": f"Shipment with id #{id} is deleted!"}


# Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )


