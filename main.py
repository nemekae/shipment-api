from fastapi import FastAPI, status, HTTPException
from typing import Any
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()


# Let add a mini db of 7 different data elements

shipments = {
    12700: {
        "content": "TV board",
        "weight": 12.5,
        "color": "brown",
        "status": "available",
    },
    12701: {
            "content": "staircase",
            "weight": 12.7,
            "color": "brown",
            "status": "delivered",
        },
    12702: {
            "content": "wooden table",
            "weight": 12.4,
            "color": "brown",
            "status": "In-transit",
        },
    12703: {
            "content": "wooden chair",
            "weight": 12,
            "color": "brown",
            "status": "delivered",
        },
    12704: {
            "content": "bedframe",
            "weight": 12.5,
            "color": "brown",
            "status": "In-transit",
        },
    12705: {
            "content": "wooden locker",
            "weight": 12.5,
            "color": "brown",
            "status": "placed",
        },
    12706: {
            "content": "cupboard",
            "weight": 12.5,
            "color": "black",
            "status": "available",
        },
    12707: {
            "content": "gold tiles",
            "weight": 10,
            "color": "ash",
            "status": "In-transit",
        },
}

# Define query parameter
@app.get("/shipment")
def shipment(id: int | None = None) -> dict[str, Any]:
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
def addshipment(weight: float, data: dict[str, Any]) -> dict[str, Any]:
    content = data["content"]
    color = data["color"]
    if weight > 25:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Max weight limit 25 is exceeded"
        )

    idx = max(shipments.keys()) + 1
    shipments[idx] = {
       "content": content,
        "weight": weight,
        "color": color,
        "status": "placed", 
    }

    return shipments[idx]


@app.put("/shipment")
def shipment_update(
    id: int, 
    content: str, 
    weight: float, 
    status: str
    ) -> dict[str, Any]:
    shipments[id] = {
        "content": content,
        "weight": weight,
        "status": "status", 
    }
    return shipments[id]

@app.patch("/shipment")
def update_shipment(id: int, body: dict[str, Any]) -> dict[str, Any]:
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


