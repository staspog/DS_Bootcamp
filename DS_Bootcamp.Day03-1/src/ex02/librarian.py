import os
import subprocess
import sys
import shutil
from pathlib import Path

def verify_environment():
    venv_path = os.environ.get("VIRTUAL_ENV")
    if not venv_path or Path(venv_path).name != "numbersr":
        raise RuntimeError("Скрипт должен запускаться в окружении 'numbersr'")
    return venv_path

def get_pip_path(venv_path):
    return str(Path(venv_path) / "Scripts" / "pip.exe" if os.name == "nt" else Path(venv_path) / "bin" / "pip")

def install_libraries(pip_path):
    subprocess.check_call([pip_path, "install", "-r", "requirements.txt"])

def save_requirements(pip_path):
    with open("requirements.txt", "w") as f:
        subprocess.run([pip_path, "freeze"], stdout=f)
    
    print("Установленные библиотеки в окружении 'numbersr':")
    with open("requirements.txt", "r") as f:
        print(f.read())

def create_env_archive(venv_path):
    env_archive_name = "numbersr_env"
    shutil.make_archive(env_archive_name, "zip", venv_path)
    print(f"\nАрхив окружения создан: {env_archive_name}.zip")

def main():
    try:
        # 1. Проверка окружения
        venv_path = verify_environment()
        
        # 2. Получение пути к pip
        pip_path = get_pip_path(venv_path)
        
        # 3. Установка библиотек
        install_libraries(pip_path)
        
        # 4. Сохранение зависимостей
        save_requirements(pip_path)
        
        # 5. Архивация окружения
        create_env_archive(venv_path)
        
    except subprocess.CalledProcessError as e:
        print(f"Ошибка выполнения команды: {e}", file=sys.stderr)
        sys.exit(1)
    except RuntimeError as e:
        print(f"Ошибка окружения: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Неожиданная ошибка: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()