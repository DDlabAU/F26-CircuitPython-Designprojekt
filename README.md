# F26 CircuitPython Designprojekt (4. semester, DD)

Dette repository er companion-materiale til en 2-delt workshop-serie i CircuitPython for designstuderende.
Formatet er hands-on og øvelsesbaseret: mindre tavleundervisning, mere eksperiment og prototyping.

## Før workshop: Klargøring af board og software

Målet med klargøring:
- Board monterer som `CIRCUITPY`.
- En første testkode kører og giver både serial output + synlig LED/NeoPixel respons.
- Nødvendige libraries er på boardet (`/lib`).

Hvis ikke alt er forberedt på forhånd, bruges de første 25 min i Workshop 1 til parallel setup lane.

### Hurtiglink: Canonical ressourcer

Generel onboarding:
- [Welcome to CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython)
- [Installing CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython)
- [Installing Mu Editor](https://learn.adafruit.com/welcome-to-circuitpython/installing-mu-editor)
- [CircuitPython board downloads](https://circuitpython.org/downloads)

Libraries:
- [CircuitPython Libraries bundle](https://circuitpython.org/libraries)
- [CircUp overview](https://learn.adafruit.com/keep-your-circuitpython-libraries-on-devices-up-to-date-with-circup/overview)
- [Install CircUp](https://learn.adafruit.com/keep-your-circuitpython-libraries-on-devices-up-to-date-with-circup/install-circup)
- [CircUp update command](https://learn.adafruit.com/keep-your-circuitpython-libraries-on-devices-up-to-date-with-circup/update-command)

### Board-link matrix

| Board | Firmware download | Bootloader reference |
|---|---|---|
| Circuit Playground Express | [CPX download page](https://circuitpython.org/board/circuitplayground_express/) | Åbn samme side og følg afsnittet om bootloader/UF2 hvis nødvendig |
| QT Py ESP32-S3 (4MB Flash / 2MB PSRAM) | [QT Py S3 4MB/2MB page](https://circuitpython.org/board/adafruit_qtpy_esp32s3_4mbflash_2mbpsram/) | Åbn samme side og følg bootloader/UF2 vejledning ved behov |
| QT Py ESP32-S3 (8MB Flash / no PSRAM) | [QT Py S3 8MB page](https://circuitpython.org/board/adafruit_qtpy_esp32s3_nopsram/) | Åbn samme side og følg bootloader/UF2 vejledning ved behov |

### Trin-for-trin setup

1. Identificer board:
- Læs navn på boardets silketryk.
- Åbn matchende board-side i matrixen ovenfor.

2. Bootloader tjek/opdatering (kun hvis nødvendig):
- Sæt board i bootloader mode.
- Tjek `INFO_UF2.TXT` på boot-drevet.
- Er bootloader for gammel eller defekt, brug board-sidens bootloader/UF2 instruktioner.

3. Installer/opdater CircuitPython:
- Download korrekt `.uf2` fra board-siden.
- Drag-and-drop filen til boot-drevet.
- Bekræft at board monterer som `CIRCUITPY`.

4. Installer libraries:
- Download library bundle, samme major-version som boardets CircuitPython.
- Kopiér kun nødvendige filer/mapper til `CIRCUITPY/lib`.
- Brug CircUp hvis I vil opdatere libraries hurtigere på flere boards.

5. Kør første testkode:
- CPX: `code/00-setup-first-test-cpx/code.py`
- QT Py: `code/00-setup-first-test-qtpy/code.py`
- Bekræft serial print + LED/NeoPixel respons.

6. Hurtig fejlsøgning:
- USB-kabel er power-only (skift kabel).
- Forkert board firmware (genflash fra korrekt board-side).
- Manglende library i `/lib` (kopiér igen fra korrekt bundle-version).
- Forveksling af boot-drev vs `CIRCUITPY`.

7. Hvis setup ikke lykkes på 15 min:
- Join et par med fungerende board.
- Fortsæt øvelsesopgaverne.
- Gå tilbage til setup i checkpoint/pause-vindue.

Se også facilitatorens tjekliste: `templates/setup-checklist.md`.

## Workshop-format (2 x 4 timer)

### Workshop 1: Fundament via eksperimenter

0:00-0:10:
- Introduktion: øvelsesformat, outputkrav, demoformat.

0:10-0:35:
- Parallel setup lane:
- Track A: board klar -> start Øvelse 1.
- Track B: følg "Før workshop" setup flow.

0:35-0:45:
- Checkpoint gate:
- Alle par viser første testkode, eller kobles på et klargjort board.

0:45-3:25:
- Øvelse 1: NeoPixel miniprojekt.
- Øvelse 2: Tap-input miniprojekt.
- Øvelse 3: Touch-input miniprojekt.
- Øvelse 4: Servo miniprojekt.
- Korte debriefs efter hver øvelse.

3:25-4:00:
- Par samles i grupper (3-4 pers.) og vælger valgfri projekt-retning.

### Workshop 2: Eksterne komponenter + prototype

0:00-0:15:
- Re-entry og hardware check.

0:15-0:30:
- Kort intro til komponent-typer, resistor/3.3V og sikker tilkobling.

0:30-1:00:
- Øvelse I: QT Py + valgfri sensor (med CircUp).

1:00-1:45:
- Øvelse 2: Relay projekt.

1:45-2:30:
- Øvelse 3/4/5: vælg én track (gamepad, afstand+LED-strip, temperatur+RFID).

2:30-3:10:
- Øvelse 6: simpelt Wi-Fi projekt (Adafruit IO).

3:10-4:00:
- CASE arbejde + 60-90 sek. showcase pr. team.

## Track A / Track B under workshop

- Track A (klar board): går direkte til øvelsesopgaver.
- Track B (setup mangler): følger setup flow i denne README.
- Facilitering: hvis kø på hjælp, spørg først et nabopar før facilitator.

## Øvelser (bruges direkte i undervisningen)

Denne sektion matcher sidste års slides i struktur (miniprojekter + øvelse 1-6 + case).
Formatet er bevidst simpelt:
- `Startkode` til studerende.
- `Løsning` for de faste øvelser.
- Ingen hint-lag.

### Workshop 1

### Øvelse 1: Miniprojekt NeoPixels

Tid: 20-25 min  
Startkode: `code/w1-ovelse-1-neopixel/code.py`
Løsning: `code/w1-ovelse-1-neopixel/solution.py`

```python
import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.3
while True:
    cp.pixels[0] = (255, 0, 0)
    cp.pixels[1] = (0, 0, 255)
    time.sleep(0.2)
```

Opgaver:
1. Få de to første pixels til at lyse med forskellige farver.
2. Ekstra: Brug et `for`-loop til at lave alle pixels røde.
3. Ekstra: Lav animation med `time.sleep(0.1)`.
4. Ekstra: Lav "politi-blink" med hver anden rød/blå på skift.

Ressource:
- [Circuit Playground Express library guide](https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/circuit-playground-express-library)

Done: Teamet viser mindst ét mønster + én ændring af timing eller farvelogik.

### Øvelse 2: Miniprojekt Tap-input

Tid: 20-25 min  
Startkode: `code/w1-ovelse-2-tap/code.py`
Løsning: `code/w1-ovelse-2-tap/solution.py`

```python
import time
from adafruit_circuitplayground import cp

cp.detect_taps = 1
while True:
    if cp.tapped:
        print("Tapped!")
        cp.red_led = True
        time.sleep(0.1)
    else:
        cp.red_led = False
```

Opgaver:
1. Få tap til at toggle et output.
2. Ekstra: Kombinér tap med NeoPixels.
3. Ekstra: Undersøg forskellen på single/double tap.

Done: Teamet demonstrerer stabil tap-detektion med synlig respons.

### Øvelse 3: Miniprojekt Touch-input

Tid: 20-25 min  
Startkode: `code/w1-ovelse-3-touch/code.py`
Løsning: `code/w1-ovelse-3-touch/solution.py`

```python
import time
from adafruit_circuitplayground import cp

while True:
    if cp.touch_A1:
        print("Touched pad A1")
    time.sleep(0.05)
```

Opgaver:
1. Få touch på A1 til at trigge output.
2. Ekstra: Tilknyt toner/melodi.
3. Ekstra: Brug krokodillenæb + ledende materialer som input.

Done: Teamet viser touch-baseret interaktion, ikke kun print i console.

### Øvelse 4: Miniprojekt Servo

Tid: 30-35 min  
Startkode: `code/w1-ovelse-4-servo/code.py`
Løsning: `code/w1-ovelse-4-servo/solution.py`

```python
import time
import board
import pwmio
from adafruit_motor import servo

pwm = pwmio.PWMOut(board.A2, duty_cycle=2**15, frequency=50)
my_servo = servo.Servo(pwm)
```

Opgaver:
1. Kør servo 0 -> 180 -> 0 grader.
2. Ekstra: Styr servo med et input, I ikke har brugt før.

Ressource:
- [CircuitPython Essentials](https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials)

Done: Teamet demonstrerer kontrolleret servo-bevægelse med klar trigger/regler.

### Valgfrit projekt (slut Workshop 1 eller start Workshop 2)

Krav i samme ånd som slides:
1. Brug input + output hvor mindst én del er ny ift. øvelse 1-4.
2. Afprøv flere STEMMA-komponenter og vælg de bedste til jeres idé.
3. Vær kreative, men hold fokus på fungerende kode + komponentintegration.

### Workshop 2

### Øvelse I: QT Py + valgfri sensor

Tid: 30 min  
Startkode: `code/w2-ovelse-1-qtpy-komponent/code.py`
Løsning: ingen fælles løsning (afhænger af valgt sensor/komponent).

Opgaver:
1. Vælg QT Py board + én sensor/komponent.
2. Find officiel guide og kør eksempelkode.
3. Brug CircUp til library-installation.
4. Ekstra: Lav mindst én adfærdsændring i eksempelkoden.

Ressource:
- [CircUp overview](https://learn.adafruit.com/keep-your-circuitpython-libraries-on-devices-up-to-date-with-circup/overview)

Done: Teamet viser komponenten virker på QT Py med korrekt library-setup.

### Øvelse 2: Relay projekt

Tid: 35-45 min  
Startkode: `code/w2-ovelse-2-relay/code.py`
Løsning: `code/w2-ovelse-2-relay/solution.py`

```python
import time
import board
import digitalio

relay = digitalio.DigitalInOut(board.A1)
relay.direction = digitalio.Direction.OUTPUT
```

Opgaver:
1. Lav lampe-simulation med relay on/off.
2. Tilslut relay korrekt og få stabil blink-kørsel.
3. Ekstra: Tilslut knap og brug den til at styre relay.

Done: Relay opfører sig stabilt i flere gentagelser.

### Øvelse 3/4/5: Vælg én track

Tid: 30 min  
Vælg én af disse:
1. Input: gamepad, output: Y8/computerstyring via HID.
2. Input: afstandssensor, output: LED-strip med afstand->antal lys mapping.
3. Input: temperatursensor, output: RFID/NFC respons (over/under grænse).

Kode-start:
1. Start fra officiel guide/eksempelkode for jeres valgte komponent.
2. Kør eksempel uændret først.
3. Tilføj derefter jeres egen mapping/logik.

Ressource:
- [CircuitPython HID API](https://docs.circuitpython.org/projects/hid/en/latest/api.html#)

Løsning: ingen fælles løsning (tre forskellige tracks).

Done: Teamet kan forklare mappingen mellem input og output med én konkret regel.

### Øvelse 6: Simpelt Wi-Fi projekt (valgfri ved ustabilt net)

Tid: 30-40 min  
Startkode: `code/w2-ovelse-6-wifi/code.py`  
Settings template: `code/w2-ovelse-6-wifi/settings.toml.example`
Løsning: ingen fælles løsning (to forskellige krav + hardware variation).

`settings.toml` udgangspunkt:
```toml
WIFI_SSID = "wifinavn"
WIFI_PASSWORD = "wifikode"
AIO_USERNAME = "dit adafruit io brugernavn"
AIO_KEY = "din aio nøgle"
BROKER = "io.adafruit.com"
PORT = 1883
```

Opgaver (vælg én):
1. Styr 1 output-komponent med Adafruit IO dashboard.
2. Send data fra 1 input-komponent til Adafruit IO dashboard.
3. Ekstra: Tilføj valgfri funktionalitet.

Done: Teamet viser enten dashboard->board eller board->dashboard dataflow.

### CASE (afslutning)

Vælg én case:
1. Vejr API som input, minimum 2 outputs, med brugbar/bæredygtig vinkel.
2. Sol API + solcelle som strømkilde, fokus på energioptimering.
3. To boards i forskellige rum, Wi-Fi kommunikation mellem input og output.

Ressourcer:
- [Open-Meteo API](https://open-meteo.com/en/docs)
- [OpenWeather API](https://openweathermap.org/api)

Done: 60-90 sekunders fremvisning med problem, løsning og live adfærd.

## Repo struktur

- `README.md` - lineær playbook for begge workshops.
- `code/` - kørende kodeeksempler og første testkoder.
- `cards/` - valgfrit facilitator-materiale (ikke nødvendigt for studerende).
- `templates/` - faciliterings- og setupskabeloner.

## Acceptance criteria (kursusniveau)

1. Setup-kapitlet kan følges af et par uden facilitator-indgreb.
2. Begge første testkoder kører på mindst ét fysisk board hver.
3. Forældet bootloader kan routes til korrekt board-specifik guide.
4. Library mismatch løses via korrekt bundle major-version.
5. Setup lane holdes omkring 25 min median uden at stoppe resten af workshoppen.
