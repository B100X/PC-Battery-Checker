import psutil


battery = psutil.sensors_battery()
percent = str(battery.percent)

print ("Your device has been running on : " +percent + "% battery !")



# -------- Example Output --------

Your device has been running on : 74% battery !
