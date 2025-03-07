from cx_Freeze import setup, Executable

setup(
    name="MeuProjeto",
    version="1.0",
    description="Meu Projeto Simples",
    executables=[Executable("main.py")],
)
