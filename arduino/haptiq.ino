#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>


/****** For servos *****/
// called this way, it uses the default address 0x40
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
#define SERVOMAX  300
#define NB_SERVO 8

int mins[] = {210, 200, 200, 190, 200, 200, 190, 200};
int servos[] = {0, 1, 2, 3, 4, 5, 6, 7, 8};
int levels[] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
int timer1_counter;
int num_servo;      // will contain the servo id
int level;          // will contain the level
char val;
char message[3];
int i = 0;
bool delivering = false;


void setup() {
  Serial.begin(115200);
  delay(1000);
  
  debug("INFOS::setup::servos init begins");
  pwm.begin();
  pwm.setPWMFreq(60); // just needed, I guess
  for (int i = 0; i < NB_SERVO; i++) {
    debug("INFOS::setup::reset servo: " + String(i));
    pwm.setPWM(servos[i], 0, mins[i]);
    delay(500);
  }
  debug("INFOS::setup::All servos reset to their minimums.");
  
  noInterrupts();    // disable all interrupts
  TCCR1A = 0;
  TCCR1B = 0;
  
  // Set timer1_counter to the correct value for our interrupt interval
  timer1_counter = 34286;   // preload timer 65536-16MHz/256/2Hz
  
  TCNT1 = timer1_counter;   // preload timer
  TCCR1B |= (1 << CS12);    // 256 prescaler 
  TIMSK1 |= (1 << TOIE1);   // enable timer overflow interrupt
  interrupts(); 
}

/****** interrupt routive *****/
ISR(TIMER1_OVF_vect) {
  if (analogRead(0) <= 750) {
    while(1) Serial.println("WARNING::not enough battery::" + String(analogRead(0)));
  }
}

void loop() {
  if (Serial.available()) {
      val = Serial.read();
      if (val == 's') {
          delivering = true;
          i = 0;
      } else if (val == 'f') {
        delivering = false;
        debug("Message delivered:\t" + String(message[0]) + String(message[1]) + String(message[2]));
        i = 0;
        
        num_servo = int(message[0]) - 48;
        level = (int(message[1]) - 48) * 10 + int(message[2]) - 48;
        ctrl_servo(servos[num_servo], level); 
      } else if (delivering) {
        message[i] = val;
        i++;
      }
  }
}

/****** functions *****/

// Converts a level (0-99) to a pulse (mins[id] -> mins[id]+SERVOMAX)
int level_to_pulse(int servo_id, int level) {
  return ((int) level * SERVOMAX / 100) + mins[servo_id];
}

// Moves the servo from servo_level to level
void move(int servo_id, int servo_level, int level) {
  if (level == servo_level) {
      debug("INFOS::move::levels are the same: " + String(level));
      return;
  }

  int from = level_to_pulse(servo_id, servo_level);
  int to = level_to_pulse(servo_id, level);
  
  if (from < to) {
    while (from < to) {
      pwm.setPWM(servo_id, 0, from);
      from++;
    }
  } else {
    while (from > to) {
      pwm.setPWM(servo_id, 0, from);
      from--;
    }
  }
  debug("INFOS::move::Servo: " + String(servo_id) + " is now: " + String(level));
}

// Control the servo information before calling move (and actually move it)
bool ctrl_servo(int servonum, int level) {
  if (level > 100 || level < 0) {
    debug("WARNING::ctrl_servo::bad level entry: " + String(level));
    return false;
  }
  debug("DEBUG::ctrl_servo::should be calling move with: " + String(servonum) + String(level));
  move(servonum, levels[servonum], level);
  levels[servonum] = level;
  return true;
}

void debug(String msg) {
//  Serial.println(msg);
}
