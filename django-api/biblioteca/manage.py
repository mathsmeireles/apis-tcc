import time
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    import os
    import sys

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "biblioteca.settings")
    
    # Capturar o tempo de início
    start_time = time.time()

    try:
        execute_from_command_line(sys.argv)
    finally:
        # Calcular o tempo de inicialização
        elapsed_time = time.time() - start_time
        print(f"Tempo de inicialização: {elapsed_time:.2f} segundos")
