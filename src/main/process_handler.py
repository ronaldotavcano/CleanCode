# nome do arquivo tem que estar de acordo com sua função/funcionalidade
# gerencia processos

from src.view.first_view import introduction_page

def start() -> None:
    while True:

        command = introduction_page()
        if command == '1' : print("Inserindo musica")
        elif command == '2' : print("Criando Playlist")
        elif command == '5' : exit()
        else : print("\nComando nao encontrado, tente novamente! \n\n")