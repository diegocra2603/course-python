import json
from pathlib import Path


# Escribir json
# productos = [
#     {"id":1, "name":"Cerveza Gallo"},
#     {"id":2, "name":"Cerveza Modelo"},
#     {"id":3, "name":"Cerveza Corona"},
# ]

# data = json.dumps(productos)

# Path("archivos/productos.json").write_text(data)


# Leer JSON

data = Path("archivos/productos.json").read_text(encoding="utf-8")
productos = json.loads(data)

# Modificar JSON
productos[0]["name"] = "Chancito feliz"
Path("archivos/productos.json").write_text(json.dumps(productos))

