#!/usr/bin/env python3
import os
import shutil
import subprocess
import sys
from pathlib import Path

# Configurações do pacote
PACKAGE_NAME = "network-info"
VERSION = "1.0.0"
MAINTAINER = "lucacersan@gmail.com"
DESCRIPTION = "Utilitário para exibir informações de rede do computador"
LONG_DESCRIPTION = "Aplicativo simples que mostra o hostname e endereço IP do computador e permite copiar essas informações para a área de transferência."
SECTION = "utils"
ARCHITECTURE = "amd64"  # ou "all" para scripts puros

# Diretórios
WORKING_DIR = Path("debian_build")
DEBIAN_DIR = WORKING_DIR / "DEBIAN"
BIN_DIR = WORKING_DIR / "usr" / "bin"
APPLICATIONS_DIR = WORKING_DIR / "usr" / "share" / "applications"
PIXMAPS_DIR = WORKING_DIR / "usr" / "share" / "pixmaps"
DIST_DIR = Path("dist")

def clean_build_dirs():
    """Limpa os diretórios de build anteriores"""
    if WORKING_DIR.exists():
        shutil.rmtree(WORKING_DIR)
    if not DIST_DIR.exists():
        os.makedirs(DIST_DIR)

def create_directory_structure():
    """Cria a estrutura de diretórios necessária"""
    os.makedirs(DEBIAN_DIR, exist_ok=True)
    os.makedirs(BIN_DIR, exist_ok=True)
    os.makedirs(APPLICATIONS_DIR, exist_ok=True)
    os.makedirs(PIXMAPS_DIR, exist_ok=True)

def build_executable():
    """Constrói o executável usando PyInstaller"""
    print("Gerando executável com PyInstaller...")
    subprocess.run([
        "pyinstaller",
        "--onefile",
        "--name", PACKAGE_NAME,
        "main.py"
    ], check=True)
    
    # Copiar o executável para o diretório de destino
    shutil.copy(f"dist/{PACKAGE_NAME}", str(BIN_DIR))

def create_debian_control():
    """Cria o arquivo de controle Debian"""
    control_content = f"""Package: {PACKAGE_NAME}
Version: {VERSION}
Section: {SECTION}
Priority: optional
Architecture: {ARCHITECTURE}
Maintainer: {MAINTAINER}
Description: {DESCRIPTION}
 {LONG_DESCRIPTION.replace('\n', '\n ')}
"""
    with open(DEBIAN_DIR / "control", "w") as f:
        f.write(control_content)

def create_desktop_file():
    """Cria o arquivo .desktop para o menu de aplicativos"""
    desktop_content = f"""[Desktop Entry]
Name=Informações de Rede
Comment={DESCRIPTION}
Exec=/usr/bin/{PACKAGE_NAME}
Icon={PACKAGE_NAME}
Terminal=false
Type=Application
Categories=Utility;Network;
"""
    with open(APPLICATIONS_DIR / f"{PACKAGE_NAME}.desktop", "w") as f:
        f.write(desktop_content)

def copy_icon():
    """Copia o ícone para o diretório de ícones"""
    icon_source = Path("assets/icone.png")
    if icon_source.exists():
        shutil.copy(icon_source, PIXMAPS_DIR / f"{PACKAGE_NAME}.png")
    else:
        print("Aviso: Arquivo de ícone não encontrado.")

def build_deb_package():
    """Constrói o pacote .deb final"""
    print("Gerando pacote .deb...")
    deb_filename = f"{PACKAGE_NAME}_{VERSION}_{ARCHITECTURE}.deb"
    subprocess.run([
        "dpkg-deb",
        "--build",
        str(WORKING_DIR),
        str(DIST_DIR / deb_filename)
    ], check=True)
    print(f"Pacote criado: {DIST_DIR / deb_filename}")

def main():
    print(f"Iniciando build do pacote {PACKAGE_NAME} {VERSION}...")
    
    # Preparar diretórios
    clean_build_dirs()
    create_directory_structure()
    
    # Criar conteúdo
    build_executable()
    create_debian_control()
    create_desktop_file()
    copy_icon()
    
    # Gerar pacote
    build_deb_package()
    
    print("Build concluído com sucesso!")

if __name__ == "__main__":
    main()
