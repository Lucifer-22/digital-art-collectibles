from PIL import Image

no_of_bg = 8
no_of_bottom = 6
no_of_center = 7
no_of_corner = 6
no_of_ml = 6
no_of_mr = 6
no_of_tl = 6
no_of_tr = 6

for a in range(1, no_of_bg + 1):
    for b in range(1, no_of_bottom +1):
        for c in range(1, no_of_center + 1):
            for d in range(1, no_of_corner + 1):
                for e in range(1, no_of_ml + 1):
                    for f in range(1, no_of_mr + 1):
                        for g in range(1, no_of_tl + 1):
                            for h in range(1, no_of_tr + 1):

                                bg = Image.open('background/bg' + str(a) + '.png')  
                                bottom = Image.open('bottom/bottom' + str(b) + '.png')  
                                center = Image.open('center/center' + str(c) + '.png')
                                corner = Image.open('corner/corner' + str(d) + '.png')
                                middle_left = Image.open('middle_left/middle_left' + str(e) + '.png')  
                                middle_right = Image.open('middle_right/middle_right' + str(f) + '.png')
                                top_left = Image.open('top_left/top_left' + str(g) + '.png')    
                                top_right = Image.open('top_right/top_right' + str(h) + '.png')

                                bg.paste(bottom, (0, 0), bottom)
                                bg.paste(center, (0, 0), center)
                                bg.paste(corner, (0, 0), corner)
                                bg.paste(middle_left, (0, 0), middle_left)
                                bg.paste(middle_right, (0, 0), middle_right)
                                bg.paste(top_left, (0, 0), top_left)
                                bg.paste(top_right, (0, 0), top_right)

                                bg.save('Result/Soccer_Ball' + str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h) + '.png')
#Soccer_ball32112222.png
                                
#500 * 500 
#features = 4/5
#no_of_items = ~5
#4000 /5000


