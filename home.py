from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
def stack(x,y,z,block,up):
    for x in range(up):
        y = y + 1
        mc.setBlock(x,y,z,block)
stack(0,71,20,41,5)
mc.player.setTilePos(x,y ,z )
