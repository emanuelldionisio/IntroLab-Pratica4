void setup() {
  Serial.begin(115200);
}

void loop() {
  double termo = 5.0 * analogRead(A0) / 1023;
  double R = 5e4/(5 - termo) - 1e4;
  Serial.println(R);
}