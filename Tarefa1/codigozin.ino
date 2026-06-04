
struct termistor {
  double A, B, C;
};

termistor term1 = {0.0015394079530505833, 0.0001519389760841483, 5.401038851632163e-7};
termistor term2 = {0.0012908258763502612, 0.00019037973506470178, 4.0637257507869733e-07};
termistor term3 = {0.0006627035426614272, 0.0002876966734390638, 5.380238759988452e-08};

void setup() {
  Serial.begin(115200);
}

double lerTensao(int porta) {
  return 5.0 * analogRead(porta) / 1023;
}

double calcularResistencia(double entrada) {
  return 5e4/(5 - entrada) - 1e4;
}

double calcularTemperatura(double R, termistor &coef) {
  return 1 / (coef.A + coef.B * log(R) + coef.C * log(R) * log(R) * log(R));
}

void loop() {
  double Ta0 = calcularTemperatura(calcularResistencia(lerTensao(A0)), term1);
  double Ta1 = calcularTemperatura(calcularResistencia(lerTensao(A1)), term2);
  double Ta2 = calcularTemperatura(calcularResistencia(lerTensao(A2)), term3);

  Serial.println(Ta0);
  Serial.println(Ta1);
  Serial.println(Ta2);
  Serial.println();
  delay(100);
  
}

// term 1: Azul/Branco + Azul/Branco
// term 2: Laranja/Marrom + Vermelho/Marrom
// term 3: Amarelo/Preto + Roxo/Preto
// term 4:
// term 5: