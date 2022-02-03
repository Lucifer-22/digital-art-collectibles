from PIL import Image

no_of_bulb = 4
no_of_filament = 4
no_of_holder = 5


for a in range(1, no_of_bulb + 1):
    for b in range(1, no_of_filament +1):
        for c in range(1, no_of_holder + 1):
            
            bulb = Image.open('bulb/bulb' + str(a) + '.png')  
            filament = Image.open('filament/filament' + str(b) + '.png')  
            holder = Image.open('holder/holder' + str(c) + '.png')
                                

            bulb.paste(bulb, (0, 0), bulb)
            bulb.paste(filament, (0, 0), filament)
            bulb.paste(holder, (0, 0), holder)
                                
            bulb.save('Result/Light_bulb' + str(a) + str(b) + str(c) + '.png')

                                


