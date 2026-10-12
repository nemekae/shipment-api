# pyright: reportMissingImports=false

from typing import Any

from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference

from database import Database
from schemas import (
    ShipmentCore,
    ShipmentCreate,
    ShipmentRead,
    ShipmentUpdate,
)

app = FastAPI()
db = Database()

# Define query parameter
@app.get("/shipment", response_model=ShipmentCore)
def get_shipment(id: int | None = None):
    shipment = db.get(id)

    # Display an error if shipment id provided is not available
    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given id does not exist"
        )
    return shipment

# Define an endpoint for adding new shipments order:
@app.post("/shipment")
def submit_shipment(shipment: ShipmentCreate) -> dict[str, Any]:
    new_id = db.create(shipment)
    return {"id": new_id}

@app.patch("/shipment", response_model=ShipmentRead)
def update_shipments(id: int, shipment: ShipmentUpdate):
    shipment = db.update(id, shipment)
    return shipment

@app.delete("/shipment")
def delete_shipment(id: int) -> dict[str, str]:
    db.delete(id)

# Scalar API Documentation
@app.get("/scalar", include_in_schema=False)
def scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )


