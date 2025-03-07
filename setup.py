from cx_Freeze import setup, Executable
import os
import sys

# Definir o caminho do ícone com base no sistema operacional
if sys.platform == "win32":
    icone_path = os.path.join("assets", "icone.ico")  # Ícone para Windows
else:
    icone_path = os.path.join("assets", "icone.png")  # Ícone para Linux (se necessário)

# Configuração do executável
executables = [
    Executable(
        script="main.py",  # Arquivo principal do seu programa
        icon=icone_path,   # Caminho para o ícone
        base="Win32GUI" if sys.platform == "win32" else None,  # Usar Win32GUI para Windows
        target_name="meu_ip"  # Nome do executável
    )
]

# Configuração do setup
setup(
    name="Meu IP",
    version="1.0",
    description="Um programa para mostrar o IP",
    executables=executables,
    options={
        "build_exe": {
            "include_files": [("assets", "assets")],  # Incluir a pasta assets no build
        }
    }
)