import maya.cmds as cmds

# gui

cake_width = 8
cake_height = 27
cake_length = cake_width # depth = length

# functions

# make cake layers / tiers


def make_bottom_tier(cake_width, cake_height, cake_length):
    bottom_tier_obj, bottom_tier_node = cmds.polyCube(width=cake_width, height=(cake_height/9), depth=cake_length, name='cakeBottomTier')
    cmds.select(bottom_tier_obj)
    cmds.polyBevel(offset=0.3)
    cmds.move(0, 0, 0)
    return bottom_tier_obj


def make_middle_tier(cake_width, cake_height, cake_length):
    middle_tier_obj, middle_tier_node = cmds.polyCube(width=(cake_width - 2), height=(cake_height/9), depth=(cake_length-2), name='cakeMiddleTier')
    cmds.select(middle_tier_obj)
    cmds.polyBevel(offset=0.3)
    cmds.move(0, (cake_height*(1/9)), 0)
    return middle_tier_obj


def make_top_tier(cake_width, cake_height, cake_length):
    top_tier_obj, top_tier_node = cmds.polyCube(width=(cake_width - 4), height=(cake_height/9), depth=(cake_length-4), name='cakeTopTier')
    cmds.select(top_tier_obj)
    cmds.polyBevel(offset=0.3)
    cmds.move(0, (cake_height*(2/9)), 0)
    return top_tier_obj


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
    candle_flame_btm_obj, candle_flame_btm_node = cmds.polyCube(width=0.5, height=(cake_height/45), depth=0.5, name='candle_flameBottom')
    cmds.select(candle_flame_btm_obj)
    cmds.move(0, ((cake_height*(3.55/9)-0.25)), 0)

    # tip / tear / top 
    candle_flame_top_obj, candle_flame_top_node = cmds.polyPyramid(sideLength=(0.5), name='candle_flameTop')
    cmds.select(candle_flame_top_obj)
    cmds.move(0, ((cake_height*(3.625/9))), 0)
    cmds.xform(candle_flame_top_obj, rotation=[0, 45, 0])

    flame_grp = cmds.group([candle_flame_btm_obj, candle_flame_top_obj], name="candle_flame_GRP")
    return flame_grp


# make topper


def make_cake_topper(cake_width, cake_height, cake_length): # make only shows on box check

    topper_left_stick_obj, topper_left_stick_node = cmds.polyCube(width=0.2, height=cake_height/3, depth=0.2, name='leftTopperStick')
    cmds.select(topper_left_stick_obj)
    cmds.polyBevel(offset=0.1)
    cmds.move(0, ((cake_height*(3/9)-0.25)), ((cake_length/5)*-1))

    topper_right_stick_obj, topper_right_stick_node = cmds.polyCube(width=0.2, height=cake_height/3, depth=0.2, name='rightTopperStick')
    cmds.select(topper_right_stick_obj)
    cmds.polyBevel(offset=0.1)
    cmds.move(0, ((cake_height*(3/9)-0.25)), ((cake_length/5)))

    banner_obj, banner_node = cmds.polyCube(width=(cake_width/12), height=(cake_height/10), depth=(cake_length-4), name='topperBanner')
    cmds.select(banner_obj)
    # cmds.polyBevel(offset=0.3)
    cmds.move(0, (cake_height*(4.5/9)), 0)

    topper_grp = cmds.group([topper_left_stick_obj, topper_right_stick_obj, banner_obj], name='cake_topper_GRP')
    return topper_grp


# combine layers, candle, and topper?


def make_cake(cake_width, cake_height, cake_length):

    # cake
    bottom_tier_obj = make_bottom_tier(cake_width, cake_height, cake_length)
    middle_tier_obj = make_middle_tier(cake_width, cake_height, cake_length)
    top_tier_obj = make_top_tier(cake_width, cake_height, cake_length)
    cake_grp = cmds.group([bottom_tier_obj, middle_tier_obj, top_tier_obj], name="cakeTiers_GRP")

    # candle
    make_candle_stick(cake_height)


# generate / create cake 

# generate / create random cake



make_cake(cake_width, cake_height, cake_length)
make_candle_flame(cake_height)
make_cake_topper(cake_width, cake_height, cake_length)