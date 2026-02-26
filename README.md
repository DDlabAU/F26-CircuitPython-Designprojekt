# F26 CircuitPython Designprojekt (4. semester, DD)

Dette repository er companion-materiale til en 2-delt workshop-serie i CircuitPython og physical computing for Designprojekt på 4. semester Digital Design.


## Workshop 1

### Opsætning af board og editor
Før vi kan gå i gang er vi nødt til at installere CircuitPython (herefter cpy) på et board. Vi starter med at bruge et Circuit Playground Express (herefter cpx) board, som I kender fra tidligere workshops på 1. og 2. semester.

Vi skal også have en editor, hvor vi kan skrive kode og kommunikere med boardet. Jeg har valgt at bruge MU-editoren, fordi den er forholdsvis let at komme i gang med og er anbefalet af adafruit.

> [!NOTE]
> I er velkomne til at bruge en anden editor, hvis I har en som I bedre kan lide. I skal bare kunne få adgang til seriel forbindelse til boardet og repl. 
>
> Hvis I ikke ved, hvad det vil sige, så brug MU.

| Board | Firmware download | How to install |
|---|---|---|
| Circuit Playground Express | [CPY downloadside](https://circuitpython.org/board/circuitplayground_express/) | [Adafruit vejledning](https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-quickstart) |

Downloadsiden ovenfor går til den officielle circuitpython-hjemmeside og indeholder både information om boardet og downloads man kan have brug for. Hvis I en anden gang selv skal sætte et board op, så start derinde og søg det pågældende board frem. Derfra skal I klikke på `Learn how to install CircuitPython on this board` som går til adafruits installationsvejledning, der også er linket ovenfor. 

Jeg vil gerne have, at I følger vejledningen, både læse og udføre eventuelle eksempler, til og med afsnittet ` The REPL`.

> [!IMPORTANT]
> Lad være med at kæmpe lang tid med noget og gå i stå.
> Vejledningen er ikke for, at I skal kunne det hele selv, men for at få jer på det rette spor.
>
> Spørg endelig om hjælp, hvis noget er svært eller ikke giver mening for jer.

---

### Miniprojekt 1: NeoPixels
Startkode: `code/ws1-miniprojekt_1-neopixels/mp_1_0.py`

```python
from adafruit_circuitplayground import cp
import time

cp.pixels.brightness = 0.3

while True:
    cp.pixels[0] = (255, 0, 0)
    cp.pixels[1] = (0, 0, 255)
```

#### Opgaver:
Løsninger er i mappen `code/ws1-miniprojekt_1-neopixels/`

1. Få de to første pixels til at lyse med andre farver.
2. Brug et `for`-loop til at lave alle samme farve.
3. Lav en animation med `time.sleep(0.1)`. Prøv at ændre værdien.
4. Lav "politi-blink" med hver anden rød/blå på skift.


> [!note] 
> Bemærk at selvom miniprojektet hedder neopixels, så bruger vi boardets indbyggede neopixels gennem adafruits `adafruit_circuitplayground` modul, som følger med cpy installationen på dette board. 
>
> Skal man bruge neopixels på et andet board, skal man oftest importere det normale `neopixel` library. I kommer til at installere og importere andre biblioteker senere.

Ressourcer til denne og fremtidige opgaver:
- [Circuit Playground Express library guide](https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library)
- [Dokumentation for sleep](https://docs.micropython.org/en/v1.5/pyboard/library/time.html#time.sleep)
- [Dokumentation for for loops og range](https://docs.python.org/3/tutorial/controlflow.html#the-range-function)

---

### Miniprojekt 2: Tap-input
Startkode: `code/ws1-miniprojekt_2-tap/mp_1_0.py`

```python
from adafruit_circuitplayground import cp
import time

cp.detect_taps = 1

while True:
    if cp.tapped:
        print("Tapped!")
        cp.red_led = True
        time.sleep(1)
    else:
        cp.red_led = False
```

#### Opgaver:
Løsninger er i mappen `code/ws1-miniprojekt_2-tap/`

1. Brug det sammen med neo pixels.
2. Registrer et double-tap i stedet for et enkelt
3. Lav logik så et (double-)tap tænder lyset og lader det være tændt indtil der registreres endnu et (double-)tap.
    - Hint: I skal bruge en boolean variabel og if-statement
4. Shake skal få lyset til at skifte til en anden farve. Resten af interaktionen skal stadig virke på samme måde.
    - Hint: cp.shake(), elif.

---

### Miniprojekt 3: Touch-input
Startkode: `code/ws1-miniprojekt_3-touch/mp_3_0.py`

```python
import time
from adafruit_circuitplayground import cp

while True:
    if cp.touch_A1:
        print("Touched pad A1")
    time.sleep(0.05)
```

#### Opgaver:
Løsninger er i mappen `code/ws1-miniprojekt_3-touch/`
1. Få touch på A1 til at trigge output.
2. Tilknyt toner til flere pads. Spil en melodi.
    - Se "Play Tone" og "Start and Stop Tone" i library guide linket i miniprojekt 1.
3. Ekstra: brug krokodillenæb + ledende materialer som input.

---

### Libraries
For at kunne bruge andre komponenter, end dem der følger med boardet eller anden funktionalitet end den der kommer med  de indbyggede moduler, skal man installere libraries på sit board. 

Følg [adafruits vejledning til libraries](https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-libraries). 
Læs og udfør, hvad der står i guiden. Lad dog være med at hente koden til deres project bundle eksempel.

Når I er færdige med vejledningen, vil I have både Adafruits bundle af libraries, samt et community bundle, hentet på jeres maskiner. Gem dem et sted hvor I let kan finde dem igen. I kan bruge disse libraries til fremtidige miniopgaver, projekter og designarbejde, så længe I ikke installerer en ny version af cpy. Det kan dog være en god idé at tjekke efter opdateringener til de to bundles med jævne mellemrum. 

> [!IMPORTANT]
> Husk at vælge versionen der passer til din version af CircuitPython

---

### Miniprojekt 4: Servo
Startkode: `code/ws1-miniprojekt_4-servo/mp4_0.py`

En servo er en motor der kan styres til en bestemt position. Dem vi skal arbejde med i dag kan sættes mellem 0 og 180 grader. Den er et godt alternativ til lys, når man skal bruge et simpelt output. Kan også let bruges kreativt til f.eks. at åbne noget eller pege på noget. Husk at servoens "arm" let kan erstattes af eller udvides med noget I bygger eller 3d-printer.

```python
import time
import board
import pwmio
from adafruit_motor import servo

# Hvis ledningerne er rød, sort, hvid:
# Rød -> VOut
# Sort -> GND
# Hvid -> A2

# Hvis ledningerne er rød, brun, orange:
# Rød -> VOut
# Brun -> GND
# Orange -> A2

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
```

#### Opgaver:
Løsninger er i mappen `code/ws1-miniprojekt_4-servo`
1. Styr servo med et input. Måske får et tryk på en touch pad den til at bevæge sig til tilsvarende sted hen. Måske ryster den, når det larmer, eller når det bliver mørkt. 
    - Se forskellige muligheder i linket under miniprojekt 1

---

### Valgfrit: Installer Circup
Circup er en terminal applikation der markant letter arbejdet med eksterne libraries i jeres projektarbejde. 

> [!caution]
> Installationen kan være lidt besværlig og man kan løbe ind i mange forskellige unikke problemer, afhængigt af hvordan man har python installeret på sit system. Læs vejledningen grundigt og vær hurtige til at spørge om hjælp, hvis noget ikke virker eller ikke giver mening.

Når det er sagt, så er tiden brugt på installation godt givet ud, i forhold til hvor meget hurtigere og mindre besværligt I kan arbejde med libraries, når I kommer i gang med jeres designprojekt. 

I stedet for at rode rundt i serial monitoren efter fejl-beskeder omkring manglende libraries (og libraries manglende libraries), kan I blot skrive `circup install -a` i jeres terminal, og circup vil automatisk detektere, hvilke libraries jeres kode bruger og installere dem på boardet.

Følg denne guide fra adafruit: [use circup to easily keep your CircuitPython libraries up to date](https://learn.adafruit.com/keep-your-circuitpython-libraries-on-devices-up-to-date-with-circup/prepare)


`usage`-afsnittet bliver hurtigt langhåret, så orienter jer bare I det og prøv så selv at eksperimentere i jeres terminal. 

Prøv det med jeres egen kode fra servo-opgaven, ved at slette lib-mappen fra boardet og derefter køre `circup install -a` og se hvad der sker. 


- [CircUp overview](https://learn.adafruit.com/keep-your-circuitpython-libraries-on-devices-up-to-date-with-circup/overview)
- [Install CircUp](https://learn.adafruit.com/keep-your-circuitpython-libraries-on-devices-up-to-date-with-circup/install-circup)
- [CircUp update command](https://learn.adafruit.com/keep-your-circuitpython-libraries-on-devices-up-to-date-with-circup/update-command)

---

### Valgfrit: Opsætning af ESP32-S3 QT PY Board

| Board | Firmware download | How to install |
|---|---|---|
| Circuit Playground Express | [CPY downloadside](https://circuitpython.org/board/circuitplayground_express/) | [Adafruit vejledning](https://learn.adafruit.com/adafruit-circuit-playground-express/circuitpython-quickstart) |
| QT Py ESP32-S3 (**4MB Flash / 2MB PSRAM**) | [CPY downloadside](https://circuitpython.org/board/adafruit_qtpy_esp32s3_4mbflash_2mbpsram/) | [Adafruit vejledning](https://learn.adafruit.com/adafruit-qt-py-esp32-s3/circuitpython-2) |

Hvis I har lyst til allerede nu at prøve at arbejde med et andet board, kan I installere cpy på vores QT Py ESP32 boards. Vi kommer til at opsætte og arbejde med et helt tredje board næste gang, så det er ikke nødvendigt, men gør det, hvis I har lyst til en udfordring og synes det kunne være sjovt.

> [!IMPORTANT]
> Sørg for at vælge den rigtige version af cpy. Vores boards er 4MB Flash/2MB PSRAM.

---

### Projekt:
Lav jeres eget **lille** projekt med input og output, krav er at enten input, output, eller begge dele skal være noget I ikke har brugt i miniprojekt 1-4.
F.eks. lyd som output eller temperatur/lyssensor som input.
I skal bruge 1 STEMMA komponent, men I må gerne kombinere den med et input eller output der er indbygget på boardet. Husk også at boardet som output kan agere som mus eller tastatur og på den måde interagere med programmer på jeres computer.

Lige nu skal I ikke finde på en designløsning, I skal eksperimentere og udforske teknologien og mulighederne i den. Så vær kreative og lav noget sjovt, dumt eller brugbart. 

Se `workflow`-afsnittet i Job fra lab'ets "Zero to hero guide", for inspiration til hvordan man griber sådan et projekt an, fra tanke til prototype: [zero to hero - workflow](https://docs.google.com/document/d/1oywz79RARudm-3sqovUlj2K9e-uLEUzZAVwu1wq0sEI/edit?tab=t.m60h028sypq7)

Se dokumentet med eksempelprojekter for at få inspiration til hvordan man kan bruge de forskellige komponenter og endda også arbejde med ekstern data via api-kald:
[eksempelprojekter](https://docs.google.com/document/d/1bwTzcuTXtILzkFCv7g-AoKLSnFdLQmI5HjeFAsUAfX4/edit?tab=t.i9rm4vxij2do)


## Workshop 2
### Miniprojekt 1: Wifi-projekt med whippersnapper
Adafruit IO Whippersnappers er Adafruits no-code løsning til at arbejde med et udvalg af boards og komponenter, styre dem samt modtage data fra dem på deres webplatform, helt uden at skulle skrive kode. 

Det er hurtigt at komme i gang med og det er også muligt at lave simple blok-programmerede "actions". Men hvis man skal lave mere avancerede projekter opleverer man også hurtigt begrænsningerne og kan med fordel arbejde med IO platformen fra CPY-kode, man selv skriver. Det kommer I til at prøve i sektionerne efter.

> [!IMPORTANT]
> I er nødt til at lave installationen i google chrome. Det vil ikke virke med andre browsere.

Gennemfør vejledningen og lav opgaven med et ESP32-S3 Feather board.

Følg adafruits vejledning indtil I kan styre led'en på boardet, fra hjemmesiden. 
https://learn.adafruit.com/quickstart-adafruit-io-wippersnapper


#### Opgave

Få en komponent (udover led'en fra guiden) til at virke på whippersnapper. 

Det må gerne blot være den indbyggede neopixel, hvis I føler det er svært og har brugt lang tid. 

Har I været hurtige, kan I prøve at tilføje et StemmaQT input eller output. Vi har en række sensorer, der virker med platformen som input, og nogle af vores simplere tekst-displays virker som outputs.

### Installer circuitpython på Feather ESP32-S3
Vi skal nu til at arbejde med det nye board direkte i Circuit Python. Det gør I på samme måde som sidste gang. Følg vejledningen nedenfor, hvis I har brug for det. Når jeres board kommer frem på computeren som `CIRCUITPY` kan I fortsætte til næste sektion.

| Board | Firmware download | How to install |
|---|---|---|
| Feather ESP32-S3 4MB Flash 2MB PSRAM | [CPY downloadside](https://circuitpython.org/board/adafruit_feather_esp32s3_4mbflash_2mbpsram/) | [Adafruit vejledning](https://learn.adafruit.com/adafruit-esp32-s3-feather/circuitpython) |


### Wifi Forbindelse i Circuit Python
Følg denne vejledning for at prøve at få jeres board på internettet: https://learn.adafruit.com/adafruit-esp32-s3-feather/circuitpython-internet-test

> [!IMPORTANT]
> Når I bliver bedt om at udfylde settings.toml med wifi-information, skal I oprette et hotspot på jeres telefon
> og angive informationerne hertil.
>
> Man kan desværre ikke forbinde boards til eduroam eller lignende netværk heroppe.

I behøver ikke læse sektionen, der forklarer koden i detaljer, når I har fået det til at virke.

### Data til AdafruitIO fra Circuit Python
Adafruits IO-platform kan ikke kun bruges med whippersnapper, den kan også bruges fra normal CPY. På den måde får man en større kontrol over interaktionen og det er muligt at bruge langt flere komponenter. 

Følg denne vejledning for at prøve at sende og modtage data fra IO med CPY: https://learn.adafruit.com/adafruit-esp32-s3-feather/adafruit-io-send-and-receive-data 

Når I modtager en "random" tal-værdi på IO og fra jeres IO-dashboard kan styre farven på boardets neopixel, kan I fortsætte til næste sektion.

### Projekt
Hvis I har svært ved at finde på noget at arbejde med, så vælg en af de 3 cases herunder. Hvis I allerede er så langt med jeres designarbejde, at I kan finde på noget, der relaterer til det, så må I gerne arbejde med det.

Jeg vil gerne have at I eksperimenterer med mindst 2 komponenter, inden I vælger, hvad I vil arbejde med.

Projektet er afsluttet, når I har indsendt billede/video og en kort tekst der viser og forklarer jeres interaktion hertil: https://forms.gle/8rRWbTLjk8PhMCzm7

Hvis I laver seje ting, lægger vi det på lab'ets instagram.

#### Case 1
Brug det aktuelle vejr eller en prognose fra en api til at hente vejrdata ned og brug det til at styre et eller flere outputs.

Fokus: Kan det bruges til noget bæredygtigt eller brugbart, som er mere end blot at fortælle brugeren temperaturen på en sjov måde?

Input: Vejr API // Output: ?

#### Case 2
Vores liv er i høj grad indrettet efter Solen, da den har indflydelse på både lys, varme og energiproduktion. Find en api og brug noget valgfrit live sol-data som input. Output er valgfrit. Prøv eventuelt at tilføje solcelle og lademodul, så batteriet til jeres board lades op af solenergi.

Input: Sol api // Output: ? // Strømkilde: eventuelt solcelle

#### Case 3
Brug et board med valgfrit input. Brug et andet board med valgfrit output. De må ikke være i samme rum. Wifi skal benyttes til kommunikation imellem dem.

Fokus på at lave en prototype der kan øge sundhed, mindske ensomhed eller spare energi. I stedet for at lave den nye birdie, prøv at lave noget brugeren har på kroppen, i lommen eller lign.

Input: ? // Output: ? // Strømkilde: evt. batteri

#### Inspiration
Se `workflow`-afsnittet i Job fra lab'ets "Zero to hero guide", for inspiration til hvordan man griber sådan et projekt an, fra tanke til prototype: [zero to hero - workflow](https://docs.google.com/document/d/1oywz79RARudm-3sqovUlj2K9e-uLEUzZAVwu1wq0sEI/edit?tab=t.m60h028sypq7)

Se dokumentet med eksempelprojekter for at få inspiration til hvordan man kan bruge de forskellige komponenter og endda også arbejde med ekstern data via api-kald:
[eksempelprojekter](https://docs.google.com/document/d/1bwTzcuTXtILzkFCv7g-AoKLSnFdLQmI5HjeFAsUAfX4/edit?tab=t.i9rm4vxij2do)

Se oversigten over Lab'ets Stemma QT komponenter for inspiration til hvad I kan arbejde med: [oversigt](https://ddlabau.github.io/CircuitPython-and-STEMMA-QT/stemmaqt/)
