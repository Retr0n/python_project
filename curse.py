from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time
for i in range(10000):
    pos = mc.player.getPos()
    mc.setBlock(pos.x, pos.y-1, pos.z, 41)
    time.sleep(0.0000000001)
