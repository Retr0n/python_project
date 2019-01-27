from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z
mc.setBlocks(x,y,z,x + 10,y + 5,z + 6,41)
