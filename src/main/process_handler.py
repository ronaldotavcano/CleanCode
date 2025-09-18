# nome do arquivo tem que estar de acordo com sua função/funcionalidade
# gerencia processos

from src.view.first_view import introduction_page
from .constructor.song_register_constructor import song_register_process
from .constructor.playlist_creator_constructor import playlist_creator_process

def start() -> None:
    while True:

        command = introduction_page()
        if command == '1' : song_register_process()
        elif command == '2' : playlist_creator_process()
        elif command == '5' : exit()
        else : print("\nComando nao encontrado, tente novamente! \n\n")