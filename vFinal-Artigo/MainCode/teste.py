import time
from pynput.mouse import Listener

# Shared flag to control threads
running = True
ac_tracker = []
last_click_time = time.time()  # Armazena o tempo do último clique

def mouse_listener():
    global ac_tracker
    global last_click_time
    
    def on_click(x, y, button, pressed):
        global last_click_time
        if not pressed or not running:
            return
            
        current_time = time.time()
        time_since_last_click = current_time - last_click_time
        last_click_time = current_time
        
        print(f"Mouse clicked at ({x}, {y}) with {button}")
        print(f"Tempo desde o último clique: {time_since_last_click:.3f} segundos")
        
        # Adiciona à lista de tracking (ajuste conforme suas variáveis globais)
        ac_tracker.append((
            time_since_last_click,
            teclado.keyb_thread_on if 'teclado' in globals() else None,
            calculadora.calc_thread_on if 'calculadora' in globals() else None,
            interface_google.interface_google_on if 'interface_google' in globals() else None
        ))

    with Listener(on_click=on_click) as listener:
        while running:
            time.sleep(0.1)
        listener.stop()

# Exemplo de uso
if __name__ == "__main__":
    mouse_listener()