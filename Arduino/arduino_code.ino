int verdeA = 9;
int amareloA = 10;
int vermelhoA = 11;

int verdeB = 3;
int amareloB = 5;
int vermelhoB = 6;

void setup() {
  Serial.begin(9600);
  
  pinMode(verdeA, OUTPUT);
  pinMode(amareloA, OUTPUT);
  pinMode(vermelhoA, OUTPUT);
  pinMode(verdeB, OUTPUT);
  pinMode(amareloB, OUTPUT);
  pinMode(vermelhoB, OUTPUT);
  
  
  setSemaforoA('V');
  setSemaforoB('M');
  
  Serial.println("Sistema pronto. Comandos: A (libera A), B (libera B)");
}

void setSemaforoA(char estado) {
  digitalWrite(verdeA, LOW);
  digitalWrite(amareloA, LOW);
  digitalWrite(vermelhoA, LOW);
  
  switch(estado) {
    case 'V': digitalWrite(verdeA, HIGH); break;
    case 'A': digitalWrite(amareloA, HIGH); break;
    case 'M': digitalWrite(vermelhoA, HIGH); break;
  }
}

void setSemaforoB(char estado) {
  digitalWrite(verdeB, LOW);
  digitalWrite(amareloB, LOW);
  digitalWrite(vermelhoB, LOW);
  
  switch(estado) {
    case 'V': digitalWrite(verdeB, HIGH); break;
    case 'A': digitalWrite(amareloB, HIGH); break;
    case 'M': digitalWrite(vermelhoB, HIGH); break;
  }
}

void piscaAmareloA(int vezes) {
  for(int i = 0; i < vezes; i++) {
    digitalWrite(amareloA, HIGH);
    delay(500);
    digitalWrite(amareloA, LOW);
    delay(500);
  }
}

void piscaAmareloB(int vezes) {
  for(int i = 0; i < vezes; i++) {
    digitalWrite(amareloB, HIGH);
    delay(500);
    digitalWrite(amareloB, LOW);
    delay(500);
  }
}

void loop() {
  if (Serial.available() > 0) {
    char comando = Serial.read();
    
    switch(comando) {
      case 'A':  
        Serial.println("Comando: Liberar A");
        piscaAmareloB(3);       
        setSemaforoB('M');    
        setSemaforoA('V');       
        Serial.println("A VERDE | B VERMELHO");
        break;
        
      case 'B':
        Serial.println("Comando: Liberar B");
        piscaAmareloA(3);        
        setSemaforoA('M');       
        setSemaforoB('V');      
        Serial.println("A VERMELHO | B VERDE");
        break;
    }
  }
}