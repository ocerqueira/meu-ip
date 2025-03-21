from setuptools import setup

setup(
    name="network-info",
    version="1.0.0",
    description="Utilitário para exibir informações de rede do computador",
    author="Seu Nome",
    author_email="seu.email@exemplo.com",
    py_modules=["main"],
    install_requires=[],  # tkinter geralmente vem com o Python
    entry_points={
        'console_scripts': [
            'network-info=main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
