# d9
Designprosjekt 9

## Plotting av amplituderespons
Python-koden for plotting av amplituderespons ligger i mappa `D9_plotting`.
Amplituderesponsen er plotta ved hjelp av matplotlib i python. For å plotte med andre paramtre må du endre på linje 8 til 13 i main.py

## Implementasjon på arduino
Arduinokoden ligger i mappa `arduinokode2`
Arduinoen er konfigurert slik at r(t) må kobles til pin A0, og så får man ut b(t) på pin 13 og u(t) på pin 12. Det er også viktig inngangssignalet har offset på 2.5V.
