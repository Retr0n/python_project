from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
flX = pos.x - 2
flY = pos.y - 1
flZ = pos.z - 2
w = 10
l = 10
b = 41
mc.setBlocks(flX,flY,flZ,flX +w,flY,flZ+l,b)
while flX<= pos.x<=flX+w and flZ<=flZ<=flX+w and flX<=flX<=flX+l:
    if b == 41:
        b = 57
    else:
        b = 41
        mc.setBlocks(flX,flY,flZ,flX +w,flY,flZ+l,b)
        pos = mc.player.getTilePos()
        time.sleep(0.5)
