from adafruit_circuitplayground import cp
import time

cp.detect_taps = 2

lights_on = False

while True:
    if cp.tapped:
        print("Tapped!")

        lights_on = not lights_on
        # En mere forklarende måde at skrive det på kunne være:
        # if lights_on:
        #     lights_on = False
        # else:
        #     lights_on = True

        # Her tænder og slukker vi vores lys inde i vores første if-statement
        # så det kun sker når vi tapper på vores Circuit Playground.
        # Det betyder at vi også kan påvirke lyset fra andre steder i vores kode.
        # Hvis vi gerne vil undgå det, kan vi rykke denne del ud, så de er indenteret på linje med if cp.tapped:
        if lights_on:
            cp.pixels.fill((255, 0, 0))
        else:
            cp.pixels.fill((0, 0, 0))
        
        # Vi holder en kort pause, så vi ikke registrerer ekstra taps
        time.sleep(1)

    elif cp.shake():
        print("Shaken!")
        lights_on = True
        cp.pixels.fill((0, 255, 0))
        time.sleep(1)