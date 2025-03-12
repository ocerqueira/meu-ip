from setuptools import setup, find_packages

setup(
    name="meu_ip",
    version="1.0",
    description="Um programa para mostrar o IP",
    packages=find_packages(),
    py_modules=["main"], 
    entry_points={
        "console_scripts": [
            "meu_ip=main:main",
        ],
    },
)
