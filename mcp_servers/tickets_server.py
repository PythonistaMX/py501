"""Servidor MCP simulado de tickets de soporte (laboratorio del módulo 4).

Guarda los tickets en SQLite para que persistan entre llamadas: el cliente
MCP puede abrir una sesión nueva para cada llamada a una herramienta.

Ejecución directa (transporte stdio):
    python mcp_servers/tickets_server.py
"""

import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal

from mcp.server.fastmcp import FastMCP

RUTA_DB = Path(
    os.environ.get(
        "TICKETS_DB", Path(__file__).resolve().parent.parent / "data" / "tickets.db"
    )
)

Categoria = Literal["hardware", "software", "seguridad", "rrhh", "otro"]
Prioridad = Literal["baja", "normal", "urgente"]

mcp = FastMCP("tickets")


def _conexion() -> sqlite3.Connection:
    RUTA_DB.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(RUTA_DB)
    con.row_factory = sqlite3.Row
    con.execute(
        """CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            titulo TEXT NOT NULL,
            descripcion TEXT NOT NULL,
            categoria TEXT NOT NULL,
            prioridad TEXT NOT NULL,
            estado TEXT NOT NULL DEFAULT 'abierto',
            creado TEXT NOT NULL
        )"""
    )
    return con


@mcp.tool()
def crear_ticket(
    usuario: str,
    titulo: str,
    descripcion: str,
    categoria: Categoria,
    prioridad: Prioridad = "normal",
) -> dict:
    """Crea un ticket de soporte y devuelve su número.

    Usa prioridad "urgente" solo si la persona no puede trabajar o hay un
    riesgo de seguridad (por ejemplo, pérdida o robo de equipo).
    """
    with _conexion() as con:
        cur = con.execute(
            "INSERT INTO tickets (usuario, titulo, descripcion, categoria, prioridad, creado)"
            " VALUES (?, ?, ?, ?, ?, ?)",
            (
                usuario,
                titulo,
                descripcion,
                categoria,
                prioridad,
                datetime.now(timezone.utc).isoformat(timespec="seconds"),
            ),
        )
        return {"id": cur.lastrowid, "estado": "abierto", "prioridad": prioridad}


@mcp.tool()
def consultar_tickets(usuario: str, solo_abiertos: bool = True) -> list[dict]:
    """Lista los tickets de un usuario, del más reciente al más antiguo."""
    consulta = "SELECT * FROM tickets WHERE usuario = ?"
    if solo_abiertos:
        consulta += " AND estado = 'abierto'"
    consulta += " ORDER BY id DESC LIMIT 20"
    with _conexion() as con:
        return [dict(fila) for fila in con.execute(consulta, (usuario,))]


@mcp.tool()
def cerrar_ticket(id_ticket: int) -> dict:
    """Cierra un ticket existente. Devuelve un error si no existe."""
    with _conexion() as con:
        cur = con.execute(
            "UPDATE tickets SET estado = 'cerrado' WHERE id = ?", (id_ticket,)
        )
        if cur.rowcount == 0:
            return {"error": f"No existe el ticket {id_ticket}."}
        return {"id": id_ticket, "estado": "cerrado"}


if __name__ == "__main__":
    mcp.run(transport="stdio")
