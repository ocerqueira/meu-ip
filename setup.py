import sys
from cx_Freeze import setup, Executable

# Verifica se o sistema operacional é Windows
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Isso evita que a janela do console apareça

setup(
    name="MeuProjeto",
    version="1.0",
    description="Meu Projeto Simples",
    executables=[Executable("main.py", base=base)],  # Adiciona o parâmetro base aqui
)