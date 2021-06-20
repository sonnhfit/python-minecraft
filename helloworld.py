

from mcpi.minecraft import Minecraft
mc = Minecraft.create(address="localhost", port=4711)

blockID = mc.getBlock(0, 0, 0)
print(blockID)

mc.player.setTilePos(0, 120, 0)