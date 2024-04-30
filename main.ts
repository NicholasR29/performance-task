namespace SpriteKind {
    export const hitbox = SpriteKind.create()
    export const projectile2 = SpriteKind.create()
    export const uppp = SpriteKind.create()
    export const down = SpriteKind.create()
    export const left = SpriteKind.create()
    export const right = SpriteKind.create()
}
scene.onHitWall(SpriteKind.Projectile, function (sprite3, location) {
    if (projectileene.image.equals(assets.image`purpdino`) || projectileene.image.equals(assets.image`yellowdino`)) {
        info.changeLifeBy(-1)
        sprites.destroy(sprite3)
    } else {
        sprites.destroy(sprite3)
    }
})
sprites.onOverlap(SpriteKind.hitbox, SpriteKind.Projectile, function (sprite2, otherSprite) {
    sprites.destroy(otherSprite)
    sprites.destroy(sprite2)
})
function spawndino (doffoculty: number) {
    list2 = [
    assets.image`purpdino`,
    assets.image`yellowdino`,
    assets.image`princess`,
    assets.image`mayor`
    ]
    projectile_kind = randint(0, num)
    initialpos = randint(0, scene.screenHeight())
    if (projectile_kind == 3) {
        projectileene = sprites.create(list2.removeAt(3), SpriteKind.Projectile)
        num = 2
        projectileene.setPosition(160, initialpos)
        projectileene.setVelocity(doffoculty * -25, 0)
    } else {
        projectileene = sprites.create(list2[projectile_kind], SpriteKind.Projectile)
        projectileene.setPosition(160, initialpos)
        projectileene.setVelocity(doffoculty * -25, 0)
    }
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    animation.runImageAnimation(
    mySprite,
    assets.animation`swipe`,
    100,
    false
    )
    box = sprites.create(assets.image`hitbox`, SpriteKind.hitbox)
    for (let value of sprites.allOfKind(SpriteKind.Projectile)) {
        if (mySprite.overlapsWith(value)) {
            if (value.image.equals(assets.image`purpdino`) || value.image.equals(assets.image`yellowdino`)) {
                sprites.destroy(value, effects.spray, 100)
            } else {
                sprites.destroy(value, effects.spray, 100)
                info.changeLifeBy(-1)
            }
        }
    }
})
sprites.onCreated(SpriteKind.hitbox, function (sprite) {
    sprite.setPosition(mySprite.x + 5, mySprite.y)
    pause(100)
    sprites.destroy(sprite)
})
let box: Sprite = null
let initialpos = 0
let projectile_kind = 0
let list2: Image[] = []
let projectileene: Sprite = null
let num = 0
let mySprite: Sprite = null
tiles.setCurrentTilemap(tilemap`freedom`)
info.setLife(10)
mySprite = sprites.create(assets.image`MYSPRITE`, SpriteKind.Player)
mySprite.setStayInScreen(true)
controller.moveSprite(mySprite, 0, 200)
mySprite.x = 35
let speed = 50
num = 3
let difff = game.askForNumber("What Dino Difficulty?", 1)
game.onUpdateInterval(1000, function () {
    if (info.life() <= 0) {
        game.gameOver(false)
    }
    spawndino(difff)
    info.changeScoreBy(1)
})
