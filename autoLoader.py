import subprocess

# Linux Device list command
listCommand = "ls /dev/" 

# Get a list of current devices
startList = subprocess.check_output(listCommand, shell=True).split('\n')

while True:
  # Get list of devices again and compared with old list
  out = subprocess.check_output(listCommand, shell=True).split('\n')

  if startList != out:
    diff = list(set(out) - set(startList))
    startList = out

    for item in list(set(diff) - set(['serial',''])):
      # Change the path to where your arduino folder is located - This comes from Arduino IDE based on board selected
      cmd = "/Tools/arduino-1.6.4/hardware/tools/avr/bin/avrdude -C/Tools/arduino-1.6.4/hardware/tools/avr/etc/avrdude.conf -v -patmega328p -carduino -P/dev/"
      cmd += item
      # Change the path to the Hex file.
      cmd += " -b57600 -D -Uflash:w:grbl_v0_9i_atmega328p_16mhz_115200.hex:i"

      print subprocess.check_output(cmd,shell=True)
