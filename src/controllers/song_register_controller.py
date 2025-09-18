from src.models.entities.music import Music
from src.models.repositories.musics_repository import musics_repository


class SongRegisterController:
    def insert(self, new_song_informations: dict) -> dict:
        # Princípio da Responsabilidade Única -> cada método tem sua responsabilidade separada
        try:
            self.__verify_songs_infos(new_song_informations)
            self.__verify_if_song_already_registered(new_song_informations)
            self.__insert_song(new_song_informations)
            return self.__format_response(new_song_informations)
        except Exception as exception:
            return self.__format_error_response(exception)

        # colocar __ antes do método torna ele privado
        # Pq privado? para nenhuma outra região do código utilize esse método. Vantagem: se ele der problema, ele só dá problema nessa parte do código
    def __verify_songs_infos(self, new_song_informations: dict) -> None:
        if len(new_song_informations["title"]) > 100:
            raise Exception("Título de música com mais de 100 caracteres")
        
        year = int(new_song_informations["year"])
        if year >= 2026:
            raise Exception("Ano de música inválido!")
    
    def __verify_if_song_already_registered(self, new_song_informations: dict) -> None:
        new_song_title = new_song_informations["title"]
        search_response = musics_repository.find_music(new_song_title)
        if search_response is not None:
            raise Exception("Música já cadastrada")

    def __insert_song(self, new_song_informations: dict) -> None:
        new_music = Music(
            title=new_song_informations["title"],
            artist=new_song_informations["artist"],
            year=int(new_song_informations["year"])
            )
        musics_repository.insert_music(new_music)

    def __format_response(self, new_song_informations: dict) -> dict:
        return {
            "success": True,
            "count": 1,
            "attributes": {
                "title": new_song_informations["title"],
            },
        }

    def __format_error_response(self, err: Exception) -> dict:
        return {
            "success": False,
            "error": str(err),
            }


