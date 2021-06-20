# python-minecraft
control minecraft 1.16.5  using python3

## Tested one macos bigsur 11.4
i think it will run the same on ubuntu

## [Important]If you do not run python with server minecraft 1.16.5+ it's because you haven't added the plugin like me. see folder plugin 
### step 1 runserver minecraft with javas
- install java8
- clone this project
- edit config in file if you need 
- runserver with  terminal 

see [detail document](https://www.spigotmc.org/wiki/buildtools/) for this step if you want to build server by yourseft 

```
git clone https://github.com/sonnhfit/python-minecraft.git
cd python-minecraft
java -jar spigot-1.16.5.jar nogui     
```

see [folder plugin ](https://github.com/sonnhfit/python-minecraft/tree/master/plugins) because if you use new version you need copy pate plugin folder like me


### step 2 

```
pip install mcpi==1.2.0
```
i use 1.2.0 if you using newer version version 
```
pip install mcpi
```


# step 3 code python for control minecraft 
see document in [this link](https://www.stuffaboutcode.com/p/minecraft-api-reference.html)

```
from mcpi.minecraft import Minecraft
mc = Minecraft.create(address="localhost", port=4711)
blockID = mc.getBlock(0, 0, 0)
print(blockID)
mc.player.setTilePos(0, 120, 0)
```
