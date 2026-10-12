from __future__ import annotations

import sqlite3
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from models import ShipmentCreate, ShipmentUpdate


class Database:
    def __init__(self):
        self.con = sqlite3.connect("sqlite.db", check_same_thread=False)
        self.cur = self.con.cursor()
        self.create_table("shipments")

    def create_table(self, name: str):
        self.cur.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {name} (
                id INTEGER PRIMARY KEY,
                content TEXT,
                weight REAL,
                destination TEXT,
                status TEXT
            )
            """
        )
        self.con.commit()

    def create(self, shipment: ShipmentCreate) -> int:
        self.cur.execute("SELECT MAX(id) FROM shipments")
        result = self.cur.fetchone()
        new_id = result[0] + 1 if result[0] is not None else 1

        self.cur.execute(
            """
            INSERT INTO shipments (id, content, weight, destination, status)
            VALUES (?, ?, ?, ?, ?)
            """,
            (new_id, shipment.content, shipment.weight, shipment.destination, shipment.status),
        )
        self.con.commit()
        return new_id

    def get(self, id: int) -> dict[str, Any] | None:
        self.cur.execute(
            """
            SELECT id, content, weight, destination, status
            FROM shipments
            WHERE id = ?
            """,
            (id,),
        )
        row = self.cur.fetchone()

        if row is None:
            return None

        return {
            "id": row[0],
            "content": row[1],
            "weight": row[2],
            "destination": row[3],
            "status": row[4],
        }

    def update(self, id: int, shipment: ShipmentUpdate) -> dict[str, Any] | None:
        data = shipment.model_dump()
        sets = ", ".join(f"{key} = ?" for key in data)
        values = list(data.values()) + [id]

        self.cur.execute(
            f"""
            UPDATE shipments
            SET {sets}
            WHERE id = ?
            """,
            values,
        )
        self.con.commit()
        return self.get(id)

    def delete(self, id: int):
        self.cur.execute(
            """
            DELETE FROM shipments
            WHERE id = ?
            """,
            (id,),
        )
        self.con.commit()

    def close(self):
        self.con.close()


