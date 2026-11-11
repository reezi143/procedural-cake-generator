import maya.cmds as cmds

import random


def test_win_function():
    main_win = cmds.window(title='Make A Cake!!', width=400)

    cmds.columnLayout(rowSpacing=10)

    cmds.text(label='Cake Generator')

    cmds.intSliderGrp('width', label='Width', min=8, max=28, step=2)
    cmds.intSliderGrp('height', label='Height', min=27, max=42, step=3)
    cmds.intSliderGrp('length', label='Length', min=8, max=28, step=2)

    cmds.checkBox('lightCandle', label='Light Candle') # make dark when unchecked?
    cmds.checkBox('includeTopper', label='Include Topper') # center?

    cmds.button(label='Create Cake', command='generate_cake()')

    cmds.button(label='Create Random-Sized Cake', command='generate_random_cake()')

    cmds.showWindow(main_win)


def make_bottom_tier(cake_width, cake_height, cake_length):
    bottom_tier_obj, bottom_tier_node = cmds.polyCube(width=cake_width, 
        height=(cake_height/9), depth=cake_length, name='cakeBottomTier')
    cmds.select(bottom_tier_obj)
    cmds.polyBevel(offset=0.3)
    cmds.move(0, 0, 0)
    return bottom_tier_obj


def make_middle_tier(cake_width, cake_height, cake_length):
    middle_tier_obj, middle_tier_node = cmds.polyCube(width=(cake_width - 2), 
        height=(cake_height/9), depth=(cake_length-2), name='cakeMiddleTier')
    cmds.select(middle_tier_obj)
    cmds.polyBevel(offset=0.3)
    cmds.move(0, (cake_height*(1/9)), 0)
    return middle_tier_obj


def make_top_tier(cake_width, cake_height, cake_length):
    top_tier_obj, top_tier_node = cmds.polyCube(width=(cake_width - 4), 
        height=(cake_height/9), depth=(cake_length-4), name='cakeTopTier')
    cmds.select(top_tier_obj)
    cmds.polyBevel(offset=0.3)
    cmds.move(0, (cake_height*(2/9)), 0)
    return top_tier_obj


def make_candle_stick(cake_height):
    candle_stick_obj, candle_stick_node = cmds.polyCube(width=1, 
        height=cake_height/9, depth=1, name='candleStick')
    cmds.select(candle_stick_obj)
    cmds.polyBevel(offset=0.1)
    cmds.move(0, ((cake_height*(3/9)-0.25)), 0)
    candle_wick_obj, candle_wick_node = cmds.polyCube(width=0.2, 
        height=cake_height/7, depth=0.2, name='candleWick')
    cmds.select(candle_wick_obj)
    cmds.polyBevel(offset=0.1)
    cmds.move(0, ((cake_height*(3/9)-0.25)), 0)
    candle_grp = cmds.group([candle_stick_obj, candle_wick_obj], 
        name="candleStick_GRP")
    return candle_grp


def make_candle_flame(cake_height):
    candle_flame_btm_obj, candle_flame_btm_node = cmds.polyCube(width=0.5, 
        height=(cake_height/45), depth=0.5, name='candleFlameBottom')
    cmds.select(candle_flame_btm_obj)
    cmds.move(0, ((cake_height*(3.55/9)-0.25)), 0)
    candle_flame_top_obj, candle_flame_top_node = cmds.polyPyramid(
        sideLength=(0.5), name='candleFlameTop')
    cmds.select(candle_flame_top_obj)
    cmds.move(0, ((cake_height*(3.625/9))), 0)
    cmds.xform(candle_flame_top_obj, rotation=[0, 45, 0])
    flame_grp = cmds.group([candle_flame_btm_obj, candle_flame_top_obj], 
        name="candleFlame_GRP")
    return flame_grp


def make_cake_topper(cake_width, cake_height, cake_length):
    topper_left_stick_obj, topper_left_stick_node = cmds.polyCube(width=0.2, 
        height=cake_height/3, depth=0.2, name='leftTopperStick')
    cmds.select(topper_left_stick_obj)
    cmds.polyBevel(offset=0.1)
    cmds.move(0, ((cake_height*(3/9)-0.25)), ((cake_length/5)*-1))
    topper_right_stick_obj, topper_right_stick_node = cmds.polyCube(width=0.2, 
        height=cake_height/3, depth=0.2, name='rightTopperStick')
    cmds.select(topper_right_stick_obj)
    cmds.polyBevel(offset=0.1)
    cmds.move(0, ((cake_height*(3/9)-0.25)), ((cake_length/5)))
    banner_obj, banner_node = cmds.polyCube(width=(cake_width/12), 
        height=(cake_height/10), depth=(cake_length-4), name='topperBanner')
    cmds.select(banner_obj)
    cmds.move(0, (cake_height*(4.5/9)), 0)
    topper_grp = cmds.group([topper_left_stick_obj, topper_right_stick_obj, 
        banner_obj], name='cakeTopper_GRP')
    return topper_grp


def make_cake(cake_width, cake_height, cake_length):
    bottom_tier_obj = make_bottom_tier(cake_width, cake_height, cake_length)
    middle_tier_obj = make_middle_tier(cake_width, cake_height, cake_length)
    top_tier_obj = make_top_tier(cake_width, cake_height, cake_length)
    cake_grp = cmds.group([bottom_tier_obj, middle_tier_obj, top_tier_obj], 
        name="cakeTiers_GRP")
    make_candle_stick(cake_height)
    if (cmds.checkBox('lightCandle', query=True, value=True) == True):
        candleFlame = make_candle_flame(cake_height)
    if (cmds.checkBox('includeTopper', query=True, value=True) == True):
        cakeTopper = make_cake_topper(cake_width, cake_height, cake_length)


def generate_cake(cake_width=8, cake_height=27, cake_length=8):
    cake_width = cmds.intSliderGrp('width', query=True, value=True)
    cake_height = cmds.intSliderGrp('height', query=True, value=True)
    cake_length = cmds.intSliderGrp('length', query=True, value=True)
    make_cake(cake_width, cake_height, cake_length)


def generate_random_cake():
    randWidth = random.randint(8, 28)
    cake_width = randWidth
    randHeight = random.randint(27, 42)
    cake_height = randHeight
    randLength = random.randint(8, 28)
    cake_length = randLength
    make_cake(cake_width, cake_height, cake_length)


# shelf button


def create_a_cake():
    test_win_function()


shelf_name = "Custom"
icon_img = "cake_icon_img.png"

cmds.shelfButton(label="Create A Cake!!", parent=shelf_name, 
    image="cake_icon_img.png", command="create_a_cake()", style="iconOnly")