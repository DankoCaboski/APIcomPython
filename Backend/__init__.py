# dao/__init__.py
import os
import sys

# Obtém o caminho absoluto do diretório dao
dao_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
# Adiciona o caminho ao sys.path para que o Python possa encontrá-lo
sys.path.append(dao_path)
