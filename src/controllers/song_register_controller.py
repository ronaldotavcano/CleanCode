class SongRegisterController:
    def insert(self, new_song_information: dict) -> dict:
        self.__verify_songs_infos()
        self.__verify_if_song_already_registered()
        self.__insert_song()
        self.__format_response()
        pass

        # colocar __ antes do método torna ele privado
        # Pq privado? para nenhuma outra região do código utilize esse método. Vantagem: se ele der problema, ele só dá problema nessa parte do código
    def __verify_if_song_already_registered(new_song_informations: dict) -> None:
        pass

    def __verify_songs_infos(new_song_informations: dict) -> None:
        pass

    def __insert_song() -> None:
        pass

    def __format_response() -> None:
        pass


