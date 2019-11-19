from PIL import Image
import cv2
import numpy
import os
import random


img = None

def onChange(trackbarValue):
    global img
    cap.set(cv2.CAP_PROP_POS_FRAMES,trackbarValue)
    err,img = cap.read()
    cv2.imshow("output", img)
    pass

videourls = [
'https://youtu.be/LfocuQtAMW4',
'https://youtu.be/Rh_pTXvDg2g',
'https://youtu.be/LwqvKlVVGlg',
'https://youtu.be/rOd6fgJWZVU',
'https://youtu.be/CXr_Miha0Zs',
'https://youtu.be/mUtUZuCzPME',
'https://youtu.be/MYOn_Yf8Oos',
'https://youtu.be/BepTnaDBjyM',
    ]
monsters = [fn for fn in os.listdir() if fn.startswith('m') and fn.endswith('.png')]
monsterimgs = [Image.open(fn).resize((1280,720)) for fn in monsters]


index = 0
for videourl in videourls:
    cv2.namedWindow("output", cv2.WINDOW_NORMAL)        # Create window with freedom of dimensions
    cv2.resizeWindow("output", 1280, 720)
    index += 1
    os.system(f'bin/youtube-dl "{videourl}" -f mp4 -o input.mp4')


    cap = cv2.VideoCapture('input.mp4')
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cv2.createTrackbar( 'start', 'output', 0, length, onChange )

    onChange(0)
    cv2.waitKey()

    cv2.imshow("output", img)
    cv2.imwrite('thumbnail.png', img)

    random.shuffle(monsterimgs)

    tn_templ = Image.open('thumbnail.png')
    bg = Image.open('bg.png').resize((1280,720))
    tn_templ.paste(bg, (0,0), bg)

    for monsterimg in monsterimgs:
        tn = tn_templ.copy()
        tn.paste(monsterimg, (0, 0), monsterimg)
        #tn.save('tmp_created.png')
        #created = cv2.imread('tmp_created.png')
        created = cv2.cvtColor(numpy.array(tn), cv2.COLOR_RGB2BGR)
        cv2.imshow("output", created)
        if cv2.waitKey() & 0xFF == ord('s'):
            break
    os.unlink('input.mp4')
    tn.save(f'{index}_thumbnail_saved.png')
    cap.release()
    cv2.destroyAllWindows()
