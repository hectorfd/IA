print("Admin playlist")

list_song = []
def add_song():
    number = int(input("how many songs do you want to add? "))
    for i in range(number):
        song = input("Enter the name of the song: ")
        list_song.append(song)
    print("Songs added successfully!")

add_song()

list_song.sort()
print("Songs in the playlist:")
count = 1
for i in list_song:
    print(f'{count}.- {i}')
    count += 1
