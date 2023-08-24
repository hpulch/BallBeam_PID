import time
from machine import Pin

def init_stepper(IN1,IN2,IN3,IN4):

  # Create a Pin object for each connection
  in1, in2, in3, in4 = Pin(IN1, Pin.OUT), Pin(IN2, Pin.OUT), Pin(IN3, Pin.OUT), Pin(IN4, Pin.OUT)
  in1.value(0), in2.value(0), in3.value(0), in4.value(0)

  return [in1,in2,in3,in4]

def omega_stepper(RPM, DIR, RES):

  # Define rotation sequences
  step1, step2, step3, step4 = [1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]

  if DIR == "CCW":
    seq = [step1,step4,step3,step2]
  elif DIR == "CW":
    seq = [step1,step2,step3,step4]
  else:
    print("DIR parameter must be CW or CCW")

  # Calculate the time per step given speed and resolution
  stepsPerRev = 360/RES
  stepsPerSec = (RPM * stepsPerRev) / 60
  speed = 1 / stepsPerSec
  return [seq, speed]

def run_stepper(OMEGA,DATA):

  data = DATA
  seq = OMEGA[0]
  speed = OMEGA[1]
  while True:
    for step in seq:
      x=-1
      time.sleep(speed)

      # Disable all pins before writing another pin high
      data[0].value(0), data[1].value(0), data[2].value(0), data[3].value(0)
      time.sleep_us(2)
      for pin in data:
        x=x+1
        pin.value(step[x])


data = init_stepper(14,15,17,16)
omega = omega_stepper(3, "CW", 1.8)
print(omega)
run_stepper(omega,data)
