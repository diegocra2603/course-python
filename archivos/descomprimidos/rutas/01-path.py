from pathlib import Path


# Path(r"C:\Archivos de Programa\Minecraft")
# Path("/user/bin")
# Path()
# Path.home()
# Path("one/__init__.py")

path = Path("hola-mundo/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,
    path.stem,
    path.suffix,
    path.parent,
    path.absolute()
)

p = path.with_name("chancito.py")

print(p)

p = path.with_suffix(".bat")

print(p)

p = path.with_stem(".exe")

print(p)