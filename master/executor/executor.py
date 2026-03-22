import subprocess
import os
import platform

class Executor:

    def __init__(self):
        print("[INFO] Inicializando Executor (modo local - simulación distribuida)\n")
        self.groups = {
            "grupoA": ["nodo1", "nodo2"],
            "grupoB": ["nodo2", "nodo3"]
        }

    def run_on_node(self, node, script):
        print(f"[INFO] Ejecutando script '{script}' en el nodo '{node}'")
        script_path = f"../nodes/{node}/cluster/scripts/{script}"

        if not os.path.exists(script_path):
            print(f"[ERROR] No existe el script en {node}: {script_path}")
            print("-" * 60)
            return

        try:
            bash_exe = "C:/Program Files/Git/bin/bash.exe" if platform.system() == "Windows" else "bash"
            result = subprocess.run([bash_exe, script_path], capture_output=True, text=True)
            print(f"[RESULTADO] Nodo '{node}':\n{result.stdout.strip()}")
            if result.stderr:
                print(f"[ERROR] Nodo '{node}':\n{result.stderr.strip()}")
            if result.returncode == 0:
                print(f"[INFO] Ejecución exitosa en '{node}'")
            else:
                print(f"[ERROR] Fallo en '{node}' (código {result.returncode})")
        except Exception as e:
            print(f"[ERROR] Fallo al invocar bash: {e}")
        print("-" * 60)

    def run_on_group(self, group, script):
        print(f"[INFO] Ejecutando '{script}' en el grupo '{group}'\n")
        if group not in self.groups:
            print(f"[ERROR] Grupo '{group}' no existe")
            return
        for node in self.groups[group]:
            self.run_on_node(node, script)

    def deploy(self, app, group):
        print(f"[INFO] Desplegando aplicación '{app}' en el grupo '{group}'\n")
        self.run_on_group(group, "deploy.sh")

    def update_group(self, group):
        print(f"[INFO] Actualizando grupo '{group}'\n")
        self.run_on_group(group, "update.sh")

    def get_sensor_data(self, node):
        print(f"[INFO] Consultando sensores en '{node}'")
        data = {"temp": 35, "cpu": 10}
        print(f"[INFO] Datos: {data}\n")
        return data
