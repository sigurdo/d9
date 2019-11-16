# d9
Designprosjekt 9

## Plotting av amplituderespons
Python-koden for plotting av amplituderespons ligger i mappa `D9_plotting`.
Amplituderesponsen er plotta ved hjelp av matplotlib i python. Dette scriptet kan kun brukes til å plotte grafer for vilkårlig N og samplingsfrekvens, gitt at T_S1 = 2 T_S0. Så for å plotte andre verdier av N og T_S, redigerer man linje 8 og 9 i `main.py`.

## Implementasjon på arduino
Arduinokoden ligger i mappa `arduinokode2`
Arduinoen er konfigurert slik at r(t) må kobles til pin A0, og så får man ut b(t) på pin 13 og u(t) på pin 12.
