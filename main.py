import tkinter as tk
from tkinter import ttk
import socket

def get_network_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return hostname, ip_address

def copy_to_clipboard(root, status_label, hostname, ip_address):
    info = f"Hostname: {hostname}\nIP: {ip_address}"
    root.clipboard_clear()
    root.clipboard_append(info)
    root.update()
    status_label.config(text="Copiado!", foreground="green")
    root.after(2000, lambda: status_label.config(text=""))

def main():
    # Criando a janela principal
    root = tk.Tk()
    root.title("Informações do Computador")
    root.geometry("350x180")
    root.resizable(False, False)
    root.configure(bg="#f0f0f0")

    # Obtendo informações
    hostname, ip_address = get_network_info()

    # Criando widgets
    frame = ttk.Frame(root, padding=15)
    frame.pack(expand=True, fill="both")

    ttk.Label(frame, text="Informações de Rede", font=("Arial", 12, "bold")).pack(pady=5)
    ttk.Label(frame, text=f"Hostname: {hostname}", font=("Arial", 10)).pack(pady=2)
    ttk.Label(frame, text=f"IP: {ip_address}", font=("Arial", 10)).pack(pady=2)

    button_frame = ttk.Frame(frame)
    button_frame.pack(pady=10)

    # Use lambda para passar os parâmetros para a função de cópia
    copy_button = ttk.Button(button_frame, text="Copiar", command=lambda: copy_to_clipboard(root, status_label, hostname, ip_address))
    copy_button.pack(side="left", padx=5)

    close_button = ttk.Button(button_frame, text="Fechar", command=root.quit)
    close_button.pack(side="left", padx=5)

    status_label = ttk.Label(frame, text="", font=("Arial", 9), foreground="green")
    status_label.pack(pady=5)

    root.mainloop()

if __name__ == '__main__':
    main()
