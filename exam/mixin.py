class MusicPlayerMixin:
    def play_music(self, song):
        print(f'Now playing {song}')


class Car(MusicPlayerMixin):
    def ride(self):
        print('Riding a car!')
