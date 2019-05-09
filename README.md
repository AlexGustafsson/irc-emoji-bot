# IRC Emoji Bot
### A Dockerized IRC Emoji Bot written in Python 3
***

### Setting up

##### Quickstart

```Bash
# Clone the repository
git clone https://github.com/AlexGustafsson/irc-emoji-bot
# Enter the directory
cd irc-emoji-bot
# Build the image
./build-docker.sh
# Start the image
docker run -d -e SERVER='irc.example.org' --restart always axgn/irc-emoji-bot
```

### Documentation

#### Running with Docker

```Bash
docker run -d \
-e SERVER='irc.example.org' \
-e PORT='6697' \
-e CHANNEL='#random' \
-e NICK='emoji-bot' \
-e USER='emoji-bot' \
-e GECOS='Emoji Bot v0.1 (github.com/AlexGustafsson/irc-emoji-bot)' \
axgn/irc-emoji-bot
```

#### Invoking via IRC

To see help messages send `emoji-bot: help` in the channel where the bot lives.

By sending a message such as `I just saw my friend use Vim (rage)`, the bot will lookup `(rage)` and send an appropriate emoji.

#### Available emojis

Source: http://asciimoji.com

| command | emoji |
|---|---|
| (acid) | ⊂(◉‿◉)つ |
| (afraid) | (ㆆ _ ㆆ) |
| (alpha) | α |
| (angel) | ☜(⌒▽⌒)☞ |
| (angry) | •`_´• |
| (arrowhead) | ⤜(ⱺ ʖ̯ⱺ)⤏ |
| (apple) |  |
| (ass) | (‿|‿) |
| (butt) | (‿|‿) |
| (awkward) | •͡˘㇁•͡˘ |
| (bat) | /|\ ^._.^ /|\ |
| (bear) | ʕ·͡ᴥ·ʔ |
| (koala) | ʕ·͡ᴥ·ʔ |
| (bearflip) | ʕノ•ᴥ•ʔノ ︵ ┻━┻ |
| (bearhug) | ʕっ•ᴥ•ʔっ |
| (because) | ∵ |
| (since) | ∵ |
| (beta) | β |
| (bigheart) | ❤ |
| (blackeye) | 0__# |
| (blubby) | ( 0 _ 0 ) |
| (blush) | (˵ ͡° ͜ʖ ͡°˵) |
| (bond) | ┌( ͝° ͜ʖ͡°)=ε/̵͇̿̿/’̿’̿ ̿ |
| (boobs) | ( . Y . ) |
| (bored) | (-_-) |
| (bribe) | ( •͡˘ _•͡˘)ノð |
| (bubbles) | ( ˘ ³˘)ノ°ﾟº❍｡ |
| (butterfly) | ƸӜƷ |
| (cat) | (= ФェФ=) |
| (catlenny) | ( ͡° ᴥ ͡°) |
| (check) | ✔ |
| (cheer) | ※\(^o^)/※ |
| (chubby) | ╭(ʘ̆~◞౪◟~ʘ̆)╮ |
| (claro) | (͡ ° ͜ʖ ͡ °) |
| (clique) | ヽ༼ ຈل͜ຈ༼ ▀̿̿Ĺ̯̿̿▀̿ ̿༽Ɵ͆ل͜Ɵ͆ ༽ﾉ |
| (gang) | ヽ༼ ຈل͜ຈ༼ ▀̿̿Ĺ̯̿̿▀̿ ̿༽Ɵ͆ل͜Ɵ͆ ༽ﾉ |
| (squad) | ヽ༼ ຈل͜ຈ༼ ▀̿̿Ĺ̯̿̿▀̿ ̿༽Ɵ͆ل͜Ɵ͆ ༽ﾉ |
| (cloud) | ☁ |
| (club) | ♣ |
| (coffee) | c[_] |
| (cuppa) | c[_] |
| (cmd) | ⌘ |
| (command) | ⌘ |
| (cool) | (•_•) ( •_•)>⌐■-■ (⌐■_■) |
| (csi) | (•_•) ( •_•)>⌐■-■ (⌐■_■) |
| (copy) | © |
| (c) | © |
| (creep) | ԅ(≖‿≖ԅ) |
| (creepcute) | ƪ(ړײ)‎ƪ​​ |
| (cross) | † |
| (cry) | (╥﹏╥) |
| (crywave) | ( ╥﹏╥) ノシ |
| (cute) | (｡◕‿‿◕｡) |
| (dab) | ヽ( •_)ᕗ |
| (damnyou) | (ᕗ ͠° ਊ ͠° )ᕗ |
| (dance) | ᕕ(⌐■_■)ᕗ ♪♬ |
| (dead) | x⸑x |
| (dealwithit) | (⌐■_■) |
| (dwi) | (⌐■_■) |
| (delta) | Δ |
| (depressed) | (︶︹︶) |
| (derp) | ☉ ‿ ⚆ |
| (diamond) | ♦ |
| (dj) | d[-_-]b |
| (dog) | (◕ᴥ◕ʋ) |
| (dollar) | $ |
| (dollarbill) | [̲̅$̲̅(̲̅ιο̲̅̅)̲̅$̲̅] |
| (dong) | (̿▀̿ ̿Ĺ̯̿̿▀̿ ̿)̄ |
| (donger) | ヽ༼ຈل͜ຈ༽ﾉ |
| (dontcare) | (- ʖ̯-) |
| (idc) | (- ʖ̯-) |
| (dontwant) | ヽ(｀Д´)ﾉ |
| (dope) | <(^_^)> |
| (doubleflat) | 𝄫 |
| (doublesharp) | 𝄪 |
| (doubletableflip) | ┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻ |
| (down) | ↓ |
| (duckface) | (・3・) |
| (duel) | ᕕ(╭ರ╭ ͟ʖ╮•́)⊃¤=(————- |
| (duh) | (≧︿≦) |
| (dunno) | ¯\(°_o)/¯ |
| (ebola) | ᴇʙᴏʟᴀ |
| (eeriemob) | (-(-_-(-_(-_(-_-)_-)-_-)_-)_-)-) |
| (ellipsis) | … |
| (emdash) | – |
| (emptystar) | ☆ |
| (emptytriangle) | △ |
| (endure) | (҂◡_◡) ᕤ |
| (envelope) | ✉︎ |
| (letter) | ✉︎ |
| (epsilon) | ɛ |
| (euro) | € |
| (evil) | ψ(｀∇´)ψ |
| (evillenny) | (͠≖ ͜ʖ͠≖) |
| (excited) | (ﾉ◕ヮ◕)ﾉ*:・ﾟ✧ |
| (execution) | (⌐■_■)︻╦╤─ (╥﹏╥) |
| (facebook) | (╯°□°)╯︵ ʞooqǝɔɐɟ |
| (facepalm) | (－‸ლ) |
| (fancytext) | "вєωαяє, ι αм ƒαη¢у!" |
| (fart) | (ˆ⺫ˆ๑)<3 |
| (fight) | (ง •̀_•́)ง |
| (finn) | | (• ◡•)| |
| (fish) | "<""(((<3" |
| (five) | 卌 |
| (flat) | ♭ |
| (bemolle) | ♭ |
| (flexing) | ᕙ(`▽´)ᕗ |
| (fliptext) | ǝןqɐʇ ɐ ǝʞıן ǝɯ dıןɟ |
| (fliptexttable) | (ノ ゜Д゜)ノ ︵ ǝןqɐʇ ɐ ǝʞıן ʇxǝʇ dıןɟ |
| (flipped) | ┬─┬ ︵ /(.□. \） |
| (heavytable) | ┬─┬ ︵ /(.□. \） |
| (flower) | (✿◠‿◠) |
| (flor) | (✿◠‿◠) |
| (f) | ✿ |
| (fly) | ─=≡Σ((( つ◕ل͜◕)つ |
| (friendflip) | (╯°□°)╯︵ ┻━┻ ︵ ╯(°□° ╯) |
| (frown) | (ღ˘⌣˘ღ) |
| (fuckoff) | ୧༼ಠ益ಠ╭∩╮༽ |
| (gtfo) | ୧༼ಠ益ಠ╭∩╮༽ |
| (fuckyou) | ┌П┐(ಠ_ಠ) |
| (fu) | ┌П┐(ಠ_ಠ) |
| (gentleman) | ಠ_ರ |
| (sir) | ಠ_ರ |
| (monocle) | ಠ_ರೃ |
| (ghast) | = _ = |
| (ghost) | ༼ つ ╹ ╹ ༽つ |
| (gift) | (´・ω・)っ由 |
| (present) | (´・ω・)っ由 |
| (gimme) | ༼ つ ◕_◕ ༽つ |
| (givemeyourmoney) | (•-•)⌐ |
| (glitter) | (*・‿・)ノ⌒*:･ﾟ✧ |
| (glasses) | (⌐ ͡■ ͜ʖ ͡■) |
| (glassesoff) | ( ͡° ͜ʖ ͡°)ﾉ⌐■-■ |
| (glitterderp) | (ﾉ☉ヮ⚆)ﾉ ⌒*:･ﾟ✧ |
| (gloomy) | (_゜_゜_) |
| (goatse) | (з๏ε) |
| (gotit) | (☞ﾟ∀ﾟ)☞ |
| (greet) | ( ´◔ ω◔`) ノシ |
| (greetings) | ( ´◔ ω◔`) ノシ |
| (gun) | ︻╦╤─ |
| (mg) | ︻╦╤─ |
| (hadouken) | ༼つಠ益ಠ༽つ ─=≡ΣO)) |
| (hammerandsickle) | ☭ |
| (hs) | ☭ |
| (handleft) | ☜ |
| (hl) | ☜ |
| (handright) | ☞ |
| (hr) | ☞ |
| (haha) | ٩(^‿^)۶ |
| (happy) | ٩( ๑╹ ꇴ╹)۶ |
| (happygarry) | ᕕ( ᐛ )ᕗ |
| (h) | ♥ |
| (heart) | ♥ |
| (hello) | (ʘ‿ʘ)╯ |
| (ohai) | (ʘ‿ʘ)╯ |
| (bye) | (ʘ‿ʘ)╯ |
| (help) | \(°Ω°)/ |
| (highfive) | ._.)/\(._. |
| (hitting) | ( ｀皿´)｡ﾐ/ |
| (hug) | (づ｡◕‿‿◕｡)づ |
| (hugs) | (づ｡◕‿‿◕｡)づ |
| (iknowright) | ┐｜･ิω･ิ#｜┌ |
| (ikr) | ┐｜･ิω･ิ#｜┌ |
| (illuminati) | ୧(▲ᴗ▲)ノ |
| (infinity) | ∞ |
| (inf) | ∞ |
| (inlove) | (っ´ω`c)♡ |
| (int) | ∫ |
| (internet) | ଘ(੭*ˊᵕˋ)੭* ̀ˋ ɪɴᴛᴇʀɴᴇᴛ |
| (interrobang) | ‽ |
| (jake) | (❍ᴥ❍ʋ) |
| (kappa) | "(¬,‿,¬)" |
| (kawaii) | ≧◡≦ |
| (keen) | ┬┴┬┴┤Ɵ͆ل͜Ɵ͆ ༽ﾉ |
| (kiahh) | ~\(≧▽≦)/~ |
| (kiss) | (づ ￣ ³￣)づ |
| (kyubey) | ／人◕ ‿‿ ◕人＼ |
| (lambda) | λ |
| (lazy) | _(:3」∠)_ |
| (left) | ← |
| (lenny) | ( ͡° ͜ʖ ͡°) |
| (lennybill) | [̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅] |
| (lennyfight) | (ง ͠° ͟ʖ ͡°)ง |
| (lennyflip) | (ノ ͡° ͜ʖ ͡°ノ) ︵ ( ͜。 ͡ʖ ͜。) |
| (lennygang) | ( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°) |
| (lennyshrug) | ¯\_( ͡° ͜ʖ ͡°)_/¯ |
| (lennysir) | ( ಠ ͜ʖ ರೃ) |
| (lennystalker) | ┬┴┬┴┤( ͡° ͜ʖ├┬┴┬┴ |
| (lennystrong) | ᕦ( ͡° ͜ʖ ͡°)ᕤ |
| (lennywizard) | ╰( ͡° ͜ʖ ͡° )つ──☆*:・ﾟ |
| (loading) | ███▒▒▒▒▒▒▒ |
| (lol) | L(° O °L) |
| (look) | (ಡ_ಡ)☞ |
| (loud) | ᕦ(⩾﹏⩽)ᕥ |
| (noise) | ᕦ(⩾﹏⩽)ᕥ |
| (love) | ♥‿♥ |
| (lovebear) | ʕ♥ᴥ♥ʔ |
| (lumpy) | ꒰ ꒡⌓꒡꒱ |
| (luv) | -`ღ´- |
| (magic) | "ヽ(｀Д´)⊃━☆ﾟ. * ･ ｡ﾟ," |
| (magicflip) | (/¯◡ ‿ ◡)/¯ ~ ┻━┻ |
| (meep) | \(°^°)/ |
| (meh) | ಠ_ಠ |
| (metal) | "\m/,(> . <)_\m/" |
| (rock) | "\m/,(> . <)_\m/" |
| (mistyeyes) | ಡ_ಡ |
| (monster) | ༼ ༎ຶ ෴ ༎ຶ༽ |
| (natural) | ♮ |
| (needle) | ┌(◉ ͜ʖ◉)つ┣▇▇▇═── |
| (inject) | ┌(◉ ͜ʖ◉)つ┣▇▇▇═── |
| (nerd) | (⌐⊙_⊙) |
| (nice) | ( ͡° ͜ °) |
| (no) | →_← |
| (noclue) | ／人◕ __ ◕人＼ |
| (nom) | (っˆڡˆς) |
| (yummy) | (っˆڡˆς) |
| (delicious) | (っˆڡˆς) |
| (note) | ♫ |
| (sing) | ♫ |
| (nuclear) | ☢ |
| (radioactive) | ☢ |
| (nukular) | ☢ |
| (nyan) | "~=[,,_,,]:3" |
| (nyeh) | @^@ |
| (ohshit) | ( º﹃º ) |
| (omega) | Ω |
| (omg) | ◕_◕ |
| (opt) | ⌥ |
| (option) | ⌥ |
| (orly) | (눈_눈) |
| (ohyou) | (◞థ౪థ)ᴖ |
| (ou) | (◞థ౪థ)ᴖ |
| (peace) | ✌(-‿-)✌ |
| (victory) | ✌(-‿-)✌ |
| (pear) | (__>- |
| (pi) | π |
| (pingpong) | ( •_•)O*¯`·.¸.·´¯`°Q(•_• ) |
| (plain) | ._. |
| (pleased) | (˶‾᷄ ⁻̫ ‾᷅˵) |
| (point) | (☞ﾟヮﾟ)☞ |
| (pooh) | ʕ •́؈•̀) |
| (porcupine) | (•ᴥ• )́`́'́`́'́⻍ |
| (pound) | £ |
| (praise) | (☝ ՞ਊ ՞)☝ |
| (punch) | O=('-'Q) |
| (rage) | t(ಠ益ಠt) |
| (mad) | t(ಠ益ಠt) |
| (rageflip) | (ノಠ益ಠ)ノ彡┻━┻ |
| (rainbowcat) | (=^･ｪ･^=))ﾉ彡☆ |
| (really) | ò_ô |
| (r) | ® |
| (right) | → |
| (riot) | ୧༼ಠ益ಠ༽୨ |
| (rolldice) | ⚃ |
| (rolleyes) | (◔_◔) |
| (rose) | ✿ڿڰۣ— |
| (run) | (╯°□°)╯ |
| (sad) | ε(´סּ︵סּ`)з |
| (saddonger) | ヽ༼ຈʖ̯ຈ༽ﾉ |
| (sadlenny) | ( ͡° ʖ̯ ͡°) |
| (sharp) | ♯ |
| (diesis) | ♯ |
| (shout) | ╚(•⌂•)╝ |
| (shrug) | ¯\_(ツ)_/¯ |
| (shy) | =^_^= |
| (sigma) | Σ |
| (sum) | Σ |
| (skull) | ☠ |
| (smile) | ツ |
| (smiley) | ☺︎ |
| (smirk) | ¬‿¬ |
| (snowman) | ☃ |
| (sob) | (;´༎ຶД༎ຶ`) |
| (soviettableflip) | ノ┬─┬ノ ︵ ( \o°o)\ |
| (spade) | ♠ |
| (sqrt) | √ |
| (squid) | <コ:彡 |
| (star) | ★ |
| (strong) | ᕙ(⇀‸↼‶)ᕗ |
| (suicide) | ε/̵͇̿̿/’̿’̿ ̿(◡︵◡) |
| (sum) | ∑ |
| (sun) | ☀ |
| (surprised) | (๑•́ ヮ •̀๑) |
| (surrender) | \_(-_-)_/ |
| (stalker) | ┬┴┬┴┤(･_├┬┴┬┴ |
| (swag) | (̿▀̿‿ ̿▀̿ ̿) |
| (sword) | o()xxxx[{::::::::::::::::::> |
| (tabledown) | ┬─┬ ノ( ゜-゜ノ) |
| (tableflip) | (ノ ゜Д゜)ノ ︵ ┻━┻ |
| (tau) | τ |
| (tears) | (ಥ﹏ಥ) |
| (terrorist) | ୧༼ಠ益ಠ༽︻╦╤─ |
| (thanks) | \(^-^)/ |
| (thankyou) | \(^-^)/ |
| (ty) | \(^-^)/ |
| (this) | ( ͡° ͜ʖ ͡°)_/¯ |
| (tiefighter) | |=-(¤)-=| |
| (tired) | (=____=) |
| (toogood) | ᕦ(òᴥó)ᕥ |
| (tm) | ™ |
| (triangle) | ▲ |
| (t) | ▲ |
| (unflip) | ┬──┬ ノ(ò_óノ) |
| (up) | ↑ |
| (victory) | (๑•̀ㅂ•́)ง✧ |
| (wat) | (ÒДÓױ) |
| (wave) | ( * ^ *) ノシ |
| (whaa) | Ö |
| (whistle) | (っ^з^)♪♬ |
| (whoa) | (°o•) |
| (why) | ლ(`◉◞౪◟◉‵ლ) |
| (witchtext) | WHΣИ $HΛLL WΣ †HЯΣΣ MΣΣ† ΛGΛ|И? |
| (woo) | ＼(＾O＾)／ |
| (wtf) | (⊙＿⊙') |
| (wut) | ⊙ω⊙ |
| (yay) | \( ﾟヮﾟ)/ |
| (yen) | ¥ |
| (yinyang) | ☯ |
| (yolo) | Yᵒᵘ Oᶰˡʸ Lᶤᵛᵉ Oᶰᶜᵉ |
| (youkids) | ლ༼>╭ ͟ʖ╮<༽ლ |
| (yuno) | (屮ﾟДﾟ)屮 Y U NO |
| (zen) | ⊹╰(⌣ʟ⌣)╯⊹ |
| (meditation) | ⊹╰(⌣ʟ⌣)╯⊹ |
| (omm) | ⊹╰(⌣ʟ⌣)╯⊹ |
| (zoidberg) | "(V) (°,,,,°) (V)" |
| (zombie) | [¬º-°]¬ |

### Contributing

Any contribution is welcome. If you're not able to code it yourself, perhaps someone else is - so post an issue if there's anything on your mind.

###### Development

Clone the repository:
```
git clone https://github.com/AlexGustafsson/irc-emoji-bot && cd irc-emoji-bot
```

### Disclaimer

_Although the project is very capable, it is not built with production in mind. Therefore there might be complications when trying to use the bot for large-scale projects meant for the public. The bot was created to easily send emojis in IRC channels and as such it might not promote best practices nor be performant._
