
echo "Start detection"


### ### ###
# Initial setting.


# Gpio setting.
#  - use 16(sensor output), 14(buzzer output)

SENSOR_GPIO=20
BUZZER_GPIO=14
SLEEP=2


# SENSOR GPIO's setting.
if [ ! -d /sys/class/gpio/gpio/gpio${SENSOR_GPIO} ]
then
  echo $SENSOR_GPIO > /sys/class/gpio/export
fi

# BUZZER GPIO's setting.
if [ ! -d /sys/class/gpio/gpio/gpio${BUZZER_GPIO} ]
then
  echo $BUZZER_GPIO > /sys/class/gpio/export
fi


# Initial gpio values.
gpio -g mode 16 output
gpio -g mode 20 input
gpio -g mode 14 output
gpio -g write 16 1
gpio -g write 14 0



### ### ###
# Detect process.

# Get sensor gpio value.
SENSOR_VALUE=/sys/class/gpio/gpio${SENSOR_GPIO}/value

# Detect if not press q

while :
do
  current_value=`cat $SENSOR_VALUE`
  if [ $current_value -eq 1 ]
  then
    gpio -g write 14 1
    echo "Water leak !!!"
  else
    gpio -g write 14 0
  fi
  sleep ${SLEEP}s
done


# End process.
gpio -g write 16 0
gpio -g mode 16 input
gpio 
