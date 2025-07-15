import kaboom from "https://unpkg.com/kaboom@3000.0.0-beta.1/dist/kaboom.mjs"

const k = kaboom({
  width: 360,
  height: 640,
  background: [26, 26, 26],
  scale: 1,
  canvas: document.createElement("canvas"),
})

document.body.appendChild(k.canvas)

let currentState = "idle"
const states = [
  "idle", "eat", "play_left", "play_right",
  "sleep", "refuse", "walk_left", "walk_right"
]

const animationConfig = {
  sliceX: 2,
  sliceY: 1,
  anims: {
    default: {
      from: 0,
      to: 1,
      loop: true,
      speed: 8,
    },
  },
}

for (const state of states) {
  loadSprite(state, `animations/${state}/sprite.png`, animationConfig)
}

let pet

onLoad(() => {
  pet = add([
    sprite("idle", { anim: "default" }),
    pos(180, 400),
    scale(1.5),
    anchor("center"),
  ])
})

window.setState = (state) => {
  if (!pet || currentState === state) return
  currentState = state
  pet.use(sprite(state))
  pet.play("default")
}

if (window.Telegram?.WebApp) {
  window.Telegram.WebApp.ready()
  const user = Telegram.WebApp.initDataUnsafe?.user
  console.log("Telegram user:", user)
}
