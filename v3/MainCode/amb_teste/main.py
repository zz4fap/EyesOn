import threading
import time
import interf
import kb_thread



# Inicializa a interface em uma thread separada
interface_tela = threading.Thread(target=interf.tela)
interface_tela.start()

# Monitora a variável global para verificar o status da thread do teclado
while interface_tela.is_alive():
    print(f"Keyboard thread running: {kb_thread.keyb_thread_on}")
    time.sleep(1)  # Print every 1 second
