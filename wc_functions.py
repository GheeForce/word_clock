import time

######## Corner Lights representing minutes 1-4
def cornerlights(minute):

    if minute % 5 == 0:
        ## NO LEDs LIT ##
        return "CORNER LIGHTS OFF"
    elif minute % 5 == 1:
        ## LED 0 LIT ##
        return "CORNER LIGHT ONE ON!"
    elif minute % 5 == 2:
        ## LED 1 LIT ##
        return "CORNER LIGHT TWO ON!"
    elif minute % 5 == 3:
        ## LED 2 LIT ##
        return "CORNER LIGHT THREE ON!"
    elif minute % 5 == 4:
        ## LED 3 LIT ##
        return "CORNER LIGHT FOUR ON!"

######## Words representing each possible hour
def word_hours(hrs, minute):
    
    if minute >= 20:
        hrs += 1
    
    if hrs == 1 or hrs == 13:
        ## LEDs
        return "EIN"
    elif hrs == 2 or hrs == 14:
        return "ZWEI"
    elif hrs == 3 or hrs == 15:
        return "DREI"
    elif hrs == 4 or hrs == 16:
        return "VIER"
    elif hrs == 5 or hrs == 17:
        return "FUNF"
    elif hrs == 6 or hrs == 18:
        return "SECHS"
    elif hrs == 7 or hrs == 19:
        return "SIEBEN"
    elif hrs == 8 or hrs == 20:
        return "ACHT"
    elif hrs == 9 or hrs == 21:
        return "NEUEN"
    elif hrs == 10 or hrs == 22:
        return "ZEHN"
    elif hrs == 11 or hrs == 23:
        return "ELF"
    elif hrs == 12 or hrs == 24:
        return "ZWOLF"

######## Words representing minutes
def word_minutes(min):
    
    if (min >= 0) and (min < 5):
        return "UHR"
    elif (min >= 5) and (min < 10) :
        return "FUNF NACH"
    elif (min >= 10) and (min < 15):
        return "ZEHN NACH"
    elif (min >= 15) and (min < 20):
        return "VIERTEL NACH"
    elif (min >= 20) and (min < 25):
        return "ZEHN VOR HALB"
    elif (min >= 25) and (min < 30):
        return "FUNF VOR HALB"      
    elif (min >= 30) and (min < 35):
        return "HALB"
    elif (min >= 35) and (min < 40):
        return "FUNF NACH"
    elif (min >= 40) and (min < 45):
        return "ZEHN NACH"
    elif (min >= 45) and (min < 50):
        return "VIERTEL NACH"
    elif (min >= 50) and (min < 55):
        return "ZEHN VOR"
    elif (min >= 55) and (min < 60):
        return "FUNF VOR"