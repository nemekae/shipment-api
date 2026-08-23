from typing import Any
temp: float = 0.0

number: int = 40

digits: list[int] = [1, 2, 3, 4, 5]

tables: tuple[str, int, float] = ("table", 1, 2.5)

shipments: dict[str, Any] = { 
    "id": 12701,
    "content": 'book',
    "weight": 0.98,
    "color": "black",
    "In-transit": True,
}

def speak(name: str) -> str:
    return f"Hello, {name}!"

