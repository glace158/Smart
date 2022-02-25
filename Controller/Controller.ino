#include <Keyboard.h>
#define INCREASE 1
#define NORMAL 0
#define DECREASE -1

const char l_speed_value[] = {'q', 'a', 'z', '0', 'Z', 'A', 'Q'};//moter0
const char r_speed_value[] = {'w', 's', 'x', '1', 'X', 'S', 'W'};//motor1
const char wrist_value[] = {'t', ' ', 'T'};// moter3
char key_check[] = {' ', ' ', ' ', ' ', ' '};

void setup() {
  pinMode(2, INPUT_PULLUP);
  pinMode(3, INPUT_PULLUP);
  pinMode(4, INPUT_PULLUP);
  pinMode(5, INPUT_PULLUP);
  pinMode(6, INPUT_PULLUP);
  Keyboard.begin();
  Serial.begin(9600);
}
//
void loop() {
  set_analog_key(0, l_speed_value, 170, true);//(motor0)
  set_analog_key(1, r_speed_value, 170, true);//(motor1)
  int state = set_state(5, 250, 750);//joystick state
  setkeywrite(2, 'P', 'p', state);//grip (servo0)
  setkeywrite(3, 'O', 'o', state);//wrist (servo1)
  setkeywrite(4, 'I', 'i', state);//wristroll (servo2)
  setkeywrite(5, 'U', 'u', state);//elbow (servo3)
  setkeywrite(6, 'Y', 'y', state);//shoulder (servo4)
  set_analog_key(4, wrist_value, 341, false);//waist (servo5)
  delay(10);
}

void set_analog_key(int pin, char speed_value[], int partition, bool check) {
  int key = analogRead(pin) / partition;
  if ( ((key_check[pin] != speed_value[key]) || !check) && (speed_value[key] != ' ')) {
    Keyboard.write(speed_value[key]);

    key_check[pin] = speed_value[key];
  }
}

int set_state(int pin, int min_threshold, int max_threshold) {
  int y = analogRead(pin);
  if (min_threshold > y) {
    return DECREASE;
  }
  else if (max_threshold < y ) {
    return INCREASE;
  }
  else {
    return NORMAL;
  }
}

void setkeywrite(int pin, char tkey, char fkey, int state) {
  char key = state != 0 ? (state > 0 ? tkey : fkey) : ' ';

  if (digitalRead(pin) == LOW && key != ' ') {
    Keyboard.write(key);
  }
}
