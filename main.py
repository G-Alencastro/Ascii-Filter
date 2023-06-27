from statistics import mean
from PIL import Image
import os

INPUT_FOLDER = 'Input'
TUNES = '_.,-=+:;cba!?0123456789$W#@Ñ'
TUNES = '▁▁' '░░' '▒▒' '▓▓' '██'
TUNES = '▁▂▃▄▅▆▇'
TUNES = '▁░▒▓█'
TUNES = '_-;=8$@#Ñ'

res = 7

#return the relative path in 'Input' folder
def in_path(filename):
    return os.path.join(INPUT_FOLDER, filename)

#return the mean luminanse of a chosen image divided in boxes
def get_tunes(img, square_size=res):
    w, h = img.size
    
    x_squares = w//square_size
    y_squares = h//square_size

    squares = []
    
    for ys in range(y_squares):
        for xs in range(x_squares):
        
            square = []
            for y in range((ys)*square_size, ys*square_size+1):
                for x in range((xs)*square_size, xs*square_size+1):
                    pixel = img.getpixel((x, y))
                    lum = int(mean(pixel))
                    square.append(lum)

            squares.append(int(mean(square)))
    
    return squares

def get_text(boxes, img, square_size=res, tunes=TUNES):
    w, h = img.size
    x_squares = w//square_size
    text = '\n'
    
    for i in range(len(boxes)):
        text += tunes[(boxes[i])//(255//len(TUNES)+1)]*2
        if i%x_squares == 0 and i > 0:
            text += '\n'

    return text

if __name__ == '__main__':
    imgs = ['beiço.jpeg', 'bolso.jpeg', 'cosplay.jpeg', 'daluncio.jpeg', 'desenho.jpeg', 
    'dormir.jpeg', 'gorilada.jpeg', 'japao.jpg', 'joao1.jpeg', 'quixo.jpeg', 'roberto.jpeg',
    'saltitao.jpeg', 'Shrek.jpg', 'shrek2.jpg', 'bolo.jpeg', 'deitado1.jpeg', 'deitado2.jpeg']
    img = Image.open(in_path(imgs[-5]))
    boxes = get_tunes(img)
    txt = get_text(boxes, img)
    print(txt)

