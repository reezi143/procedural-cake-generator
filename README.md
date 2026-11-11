GitHub Repo: https://github.com/reezi143/procedural-cake-generator.git

Program that creates and adds a custom shelf button to the Maya "Custom" shelf that allows the user to generate a three-tiered cake with any 
height, width, or length. 
The program also allows the user to choose the light the candle on top of the cake, and/or add a topper decoration to the cake's top-most layer.

Notes: 
  Icon image must be in the Maya 2026 "Icon" folder.
  Button is added to shelf by pasting the code in the Maya Script Editor, and selecting and running
  "cmds.shelfButton(label="Create A Cake!!", parent=shelf_name, image="test_img.png", command="create_a_cake()", style="iconOnly")" which adds
  the button to the shelf and automatically opens the "Create A Cake!!" window. 
