#define LED 2

void main(){
    pinmode(LED, OUTPUT);
}

void loop(){
    digitalWrite(LED, HIGH);
    delay(1000);
    digitalWrite(LED, LOW);
    delay(1000);
}