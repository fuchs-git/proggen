lyrics = ''
for i in range(99, 1, -1):
    lyrics += f'{i} bottles of beer on the wall, {i} bottles of beer.\nTake one down, pass it around, {i - 1} bottles of beer on the wall.\n\n'
lyrics += f'1 bottle of beer on the wall, 1 bottle of beer.\nTake it down, pass it around, no more bottles of beer on the wall.\n\n'
lyrics += f'No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.'

with open('99_bottles_of_beer.txt', 'w') as f:
    f.write(lyrics)