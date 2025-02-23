# make canvas
# make a box the size of the canvas
# divide the box in half, and make two boxes
# repeat

W = 1000
H = 750

size(W,H)

rect(0,0,W,H)


fill(1,1,1,0)
stroke(0,1,0)
strokeWidth(2)

rect(0,0,W,H)

def makeRects(counter, loops, width, height):
    
    ratio = 1.25
    
    green = 1 / 20 + (1/15 * counter)
    print(green)
    fill(0,green,0)
    
    newWidth = width/ratio
    rect(0,0,newWidth, height)
    
    save()
    rotate(180)
    rect(0,0,newWidth, height)
    restore()
    
    green = green+green/3
    print(green)
    fill(0,green,0)

    newHeight = height/ratio
    rect(0,0,newWidth, newHeight)
    
    save()
    rotate(180)
    rect(0,0,newWidth, height)
    restore()
    
    # set a counter
    # while counter is less than x, fire makeRects with newWidth
    
    counter += 1
    
    if counter < loops:
        makeRects(counter, loops, newWidth, newHeight)
        
    
makeRects(0, 15, W, H)

# for i in range(3):
    # i += 1
    # newWidth = W/i/2
    # make rect at half of width and full height
    # rect(0,0,newWidth,H)
    # makeRects(W, H)
    
    # make rect at same half width and half height

