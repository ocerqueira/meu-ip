# setup.py (Windows - cx_Freeze)
from cx_Freeze import setup, Executable
import os
import sys

# Define o ícone com base no sistema operacional
if sys.platform == "win32":
    icone_path = os.path.join("assets", "icone.ico")
else:
    icone_path = os.path.join("assets", "icone.png")

executables = [
    Executable(
        script="main.py",       # Arquivo principal do programa
        icon=icone_path,        # Ícone para o executável
        base="Win32GUI" if sys.platform == "win32" else None,
        target_name="meu_ip"    # Nome do executável gerado
    )
]

setup(
    name="Meu IP",
    version="1.0",
    description="Um programa para mostrar o IP",
    executables=executables,
    options={
        "build_exe": {
            "include_files": [("assets", "assets")],  # Incluir a pasta de assets no build
        }
    }
)
