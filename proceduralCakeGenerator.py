import maya.cmds as cmds

# gui

cake_width = 8
cake_height = 27
cake_length = cake_width # depth = length

# functions

# make cake layers / tiers


def make_cake_layers(cake_width, cake_height, cake_length):

        # make bottom tier

    bottom_tier_obj, bottom_tier_node = cmds.polyCube(width=cake_width, height=(cake_height/9), depth=cake_length, name='cakeBottomTier')
    cmds.select(bottom_tier_obj)
    cmds.polyBevel(offset=0.3)
    cmds.move(0, 0, 0)

        # make middle tier

    middle_tier_obj, middle_tier_node = cmds.polyCube(width=(cake_width - 2), height=(cake_height/9), depth=(cake_length-2), name='cakeMiddleTier')
    cmds.select(middle_tier_obj)
    cmds.polyBevel(offset=0.3)
    cmds.move(0, (cake_height*(1/9)), 0)

        # make top tier

    top_tier_obj, top_tier_node = cmds.polyCube(width=(cake_width - 4), height=(cake_height/9), depth=(cake_length-4), name='cakeTopTier')
    cmds.select(top_tier_obj)
    cmds.polyBevel(offset=0.3)
    cmds.move(0, (cake_height*(2/9)), 0)

        # group tiers / cake layers

    cake_grp = cmds.group([bottom_tier_obj, middle_tier_obj, top_tier_obj], name="cakeTiers_GRP")
    return cake_grp


# make candle


def make_candle_stick(cake_height):

    # candle stick / wax
    candle_stick_obj, candle_stick_node = cmds.polyCube(width=1, height=cake_height/9, depth=1, name='candleStick')
    cmds.select(candle_stick_obj)
    cmds.polyBevel(offset=0.1)
    cmds.move(0, ((cake_height*(3/9)-0.25)), 0)

    # candle wick
    candle_wick_obj, candle_wick_node = cmds.polyCube(width=0.2, height=cake_height/7, depth=0.2, name='candleWick')
    cmds.select(candle_wick_obj)
    cmds.polyBevel(offset=0.1)
    cmds.move(0, ((cake_height*(3/9)-0.25)), 0)

    candle_grp = cmds.group([candle_stick_obj, candle_wick_obj], name="candleStick_GRP")
    return candle_grp


# make candle flame


def make_candle_flame(cake_height): # make only shows on box check
    
    # base
    candle_flame_btm_obj, candle_flame_btm_node = cmds.polyCube(width=0.5, height=(cake_height/45), depth=0.5, name='candleFlameBottom')
    cmds.select(candle_flame_btm_obj)
    cmds.move(0, ((cake_height*(3.55/9)-0.25)), 0)

    # tip / tear / top 
    candle_flame_top_obj, candle_flame_top_node = cmds.polyPyramid(sideLength=(0.5), name='candleFlameTop')
    cmds.select(candle_flame_top_obj)
    cmds.move(0, ((cake_height*(3.625/9))), 0)
    cmds.xform(candle_flame_top_obj, rotation=[0, 45, 0])

    flame_grp = cmds.group([candle_flame_btm_obj, candle_flame_top_obj], name="candleFlame_GRP")
    return flame_grp


    # make topper

    # combine layers, candle, and topper?

    # generate / create cake 

    # generate / create random cake


make_cake_layers(cake_width, cake_height, cake_length)
make_candle_stick(cake_height)
make_candle_flame(cake_height)