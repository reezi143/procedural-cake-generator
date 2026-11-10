import maya.cmds as cmds

# gui

cake_width = 8
cake_height = 27
cake_length = cake_width # depth = length

# functions

    # make cake layers


def make_cake_layer(cake_width, cake_height, cake_length):

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


    # make candle / light candle

    # make topper

    # combine layers, candle, and topper?

    # generate / create cake 

    # generate / create random cake


make_cake_layer(cake_width, cake_height, cake_length)