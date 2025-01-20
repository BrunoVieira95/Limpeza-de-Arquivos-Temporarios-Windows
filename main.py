import os
import shutil
import ctypes
import sys


def is_admin():
    """Verifica se o script está sendo executado com privilégios de administrador."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False


def executar_como_admin():
    """Reinicia o script como administrador, se necessário."""
    if not is_admin():
        print("Reiniciando o script como administrador...")
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1
        )
        sys.exit()


def limpar_pasta_temp_sistema():
    """Limpa a pasta Temp do sistema."""
    pasta = r'C:\Windows\Temp'
    print("\nLimpando a pasta Temp do sistema...")

    for item in os.listdir(pasta):
        caminho_item = os.path.join(pasta, item)
        try:
            if os.path.isfile(caminho_item) or os.path.islink(caminho_item):
                os.remove(caminho_item)
                print(f'Arquivo {caminho_item} foi removido.')
            elif os.path.isdir(caminho_item):
                shutil.rmtree(caminho_item)
                print(f'Pasta {caminho_item} foi removida.')
        except PermissionError as e:
            print(f'Permissão negada para remover {caminho_item}: {e}')
        except Exception as e:
            print(f'Ocorreu um erro ao remover {caminho_item}: {e}')


def limpar_pasta_temp_usuario():
    """Limpa a pasta Temp do usuário."""
    pasta = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Temp')
    print("\nLimpando a pasta Temp do usuário...")

    for item in os.listdir(pasta):
        caminho_item = os.path.join(pasta, item)
        try:
            if os.path.isfile(caminho_item) or os.path.islink(caminho_item):
                os.remove(caminho_item)
                print(f'Arquivo {caminho_item} foi removido.')
            elif os.path.isdir(caminho_item):
                shutil.rmtree(caminho_item)
                print(f'Pasta {caminho_item} foi removida.')
        except PermissionError as e:
            print(f'Permissão negada para remover {caminho_item}: {e}')
        except Exception as e:
            print(f'Ocorreu um erro ao remover {caminho_item}: {e}')


def limpar_lixeira():
    """Esvazia a lixeira do sistema."""
    print("\nEsvaziando a lixeira...")
    SHERB_NOCONFIRMATION = 0x00000001
    SHERB_NOPROGRESSUI = 0x00000002
    SHERB_NOSOUND = 0x00000004

    try:
        ctypes.windll.shell32.SHEmptyRecycleBinW(
            None, None, SHERB_NOCONFIRMATION | SHERB_NOPROGRESSUI | SHERB_NOSOUND
        )
        print("Lixeira esvaziada com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro ao esvaziar a lixeira: {e}")


if __name__ == "__main__":
    executar_como_admin()
    limpar_pasta_temp_sistema()
    limpar_pasta_temp_usuario()
    limpar_lixeira()
