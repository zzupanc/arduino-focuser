// defining the constants
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

// These are values define the speed of the servomotor; you can change them to adjust the speed CW and CCW
// Later in code we will remap these values from analog readings comming from joystick to control the servo speed
// NOTE This is for continious 360 degree servo - min is INJORA 35KG continous
#define SERVOSTOP    0
#define SERVO_CW_F   410
#define SERVO_CCW_F  140
#define SERVO_CW_S   250
#define SERVO_CCW_S  315
#define SERVO_FREQ   50

#define VRX_PIN      A1
#define VRY_PIN      A0

// Threshold is like controller deadzone, smaller LOW-HIGH Threshold window means smaller the deadzone of joystick is
// analogRead reads the value from the joystick (0-1023), neutral joystick position reads 515
// If you have problems with servo not stopping the moment joystick is in neutral position, changing these values helped me get it more responsive
#define THRESHOLD_LOW    400
#define THRESHOLD_HIGH   700

// We are using only one servo on port 0, when using multiple servos you can add servonums for specific ports
// PWM servo driver from Adafruit can support up to 16 servos
int servonum = 0;

// This part of code is from Adafruit servo libraray to set OscFreq and PWM Freq (PWM freq is usually 50-60Hz)
void setup() {
  Serial.begin(9600);

  pwm.begin();
  pwm.setOscillatorFrequency(27000000);
  pwm.setPWMFreq(SERVO_FREQ);
  delay(10);
}


void loop() {
    if (Serial.available() > 0) {
        char command = Serial.read();
        // Handle commands
        switch (command) {
            case 'A':
                pwm.setPWM(servonum, 0, 325);  // Add semicolon here
                break;
            case 'B':
                pwm.setPWM(servonum, 0, 220);
                break;
            case 'C':
                pwm.setPWM(servonum, 0, 300);  // Add semicolon here
                break;
            case 'D':
                pwm.setPWM(servonum, 0, 260);
                break;
            case 'E':
                Serial.println("JOYSTICK NEUTRAL");
                pwm.setPWM(servonum, 0, SERVOSTOP);
                break;
            // Add more cases as needed
        }
    }
}
