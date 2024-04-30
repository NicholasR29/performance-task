@namespace
class SpriteKind:
    hitbox = SpriteKind.create()
    projectile2 = SpriteKind.create()
    uppp = SpriteKind.create()
    down = SpriteKind.create()
    left = SpriteKind.create()
    right = SpriteKind.create()
def spawndino(doffoculty: number):
    global list2, projectile_kind, initialpos, projectileene, num
    list2 = [assets.image("""
            purpdino
        """),
        assets.image("""
            purpdino
        """),
        assets.image("""
            yellopwdino
        """),
        assets.image("""
            princess
        """)]
    projectile_kind = randint(0, num)
    initialpos = randint(0, scene.screen_height())
    if projectile_kind == 3:
        projectileene = sprites.create(list2.remove_at(3), SpriteKind.projectile)
        num = 2
        projectileene.set_position(160, initialpos)
        projectileene.set_velocity(doffoculty * -25, 0)
    else:
        projectileene = sprites.create(list2[projectile_kind], SpriteKind.projectile)
        projectileene.set_position(160, initialpos)
        projectileene.set_velocity(doffoculty * -25, 0)

def on_a_pressed():
    global box
    animation.run_image_animation(mySprite,
        [img("""
            . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
                    . . . . . . . . . . . . . . . .
        """)],
        100,
        False)
    box = sprites.create(assets.image("""
        mayor
    """), SpriteKind.hitbox)
    for value in sprites.all_of_kind(SpriteKind.projectile):
        if mySprite.overlaps_with(value):
            if value.image.equals(assets.image("""
                ghost
            """)):
                sprites.destroy(value, effects.spray, 100)
            else:
                sprites.destroy(value, effects.spray, 100)
                info.change_life_by(-1)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_created(sprite):
    sprite.set_position(mySprite.x + 5, mySprite.y)
    pause(100)
    sprites.destroy(sprite)
sprites.on_created(SpriteKind.hitbox, on_on_created)

def on_on_overlap(sprite2, otherSprite):
    sprites.destroy(otherSprite)
    sprites.destroy(sprite2)
sprites.on_overlap(SpriteKind.hitbox, SpriteKind.projectile, on_on_overlap)

def on_hit_wall(sprite3, location):
    if sprite3.image.equals(img("""
        . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
                . . . . . . . . . . . . . . . .
    """)):
        info.change_life_by(-1)
        sprites.destroy(sprite3)
    else:
        sprites.destroy(sprite3)
scene.on_hit_wall(SpriteKind.projectile, on_hit_wall)

box: Sprite = None
projectileene: Sprite = None
initialpos = 0
projectile_kind = 0
list2: List[Image] = []
num = 0
mySprite: Sprite = None
tiles.set_current_tilemap(tilemap("""
    level1
"""))
info.set_life(10)
mySprite = sprites.create(assets.image("""
    mysprite
"""), SpriteKind.player)
mySprite.set_stay_in_screen(True)
controller.move_sprite(mySprite, 0, 200)
mySprite.x = 35
speed = 50
num = 3
difff = game.ask_for_number("What Dino Difficulty?", 1)

def on_update_interval():
    if info.life() <= 0:
        game.game_over(False)
    spawndino(difff)
game.on_update_interval(1000, on_update_interval)
