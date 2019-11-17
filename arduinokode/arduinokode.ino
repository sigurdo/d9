#include <Wire.h>
#include <TimerOne.h>

void setup() {
  Serial.begin(9600);
  // Oppsett av timer interrupt
  Timer1.initialize(650); // 500 mikrosekund mellom hver sample
  // Argumentet i "attachInterrupt" bestemmer hvilken funskjon som er interrupt handler
  Timer1.attachInterrupt(takeSample); 

  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
}

// Globale variaber
int sample = 0; // Holder siste sample

const int N = 2;
float H1 = 0;
int lastSamples1[N]{0};
float H2 = 0;
int lastSamples2[N]{0};
bool odd = false;

const int M = 8;
float avgArr1[M]{0};
float avg1 = 0;
float avgArr2[M]{0};
float avg2 = 0;

int b = 0;
int u = 0;

bool logging = false;
const int maxCount = 1024;
int count = 0;

void loop() {
  
}

// Interrupt-handler (kalles ved hvert interrupt)
void takeSample(void){
  sample = analogRead(0) - 512; // Sampler på A0  
  lastSamples1[1] = lastSamples1[0];
  lastSamples1[0] = sample;
  H1 = (lastSamples1[0] + lastSamples1[1])/2;

  if(odd) {
    lastSamples2[1] = lastSamples2[0];
    lastSamples2[0] = sample;
    H2 = (lastSamples2[0] + lastSamples2[1]) / 2;
  }

  avgArr1[count%M] = abs(H1);
  avgArr2[count%M] = abs(H2);
  if (count % M == 0) {
    int sum1 = 0;
    int sum2 = 0;
    for (int i = 0; i < M; i++) {
      sum1 += avgArr1[i];
      sum2 += avgArr2[i];
    }
    avg1 = sum1 / M;
    avg2 = sum2 / M;

    int d = avg1 - avg2;
    int threshold = 50;
    b = d >= 0 ? 0 : 1;
    u = abs(d) > threshold ? 1 : 0;

    digitalWrite(13, b);
    digitalWrite(12, u);
  }

  if (logging && count == maxCount-1) {
    count = 0;
    Serial.print("H1: ");
    Serial.print(avg1);
    Serial.print(", H2: ");
    Serial.println(avg2);

    Serial.print("u: ");
    Serial.print(u);
    Serial.print(", b: ");
    Serial.println(b);
  }
  count++;
  odd = !odd;
}
