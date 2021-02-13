import time
from wc_functions import cornerlights, word_minutes, word_hours

secs = time.time()
local = time.localtime(secs)

intro = 'ES IST' # LEDs 4,5, 7,8,9

min_indv = cornerlights(local.tm_min)
min_word = word_minutes(local.tm_min)
hour_word = word_hours(local.tm_hour,local.tm_min)

print("{} {} {} \n{}\n".format(intro, min_word, hour_word, min_indv))

while True:
    
    secs = time.time()
    local = time.localtime(secs)

    new_min_indv = cornerlights(local.tm_min)
    new_min_word = word_minutes(local.tm_min)
    new_hour_word = word_hours(local.tm_hour,local.tm_min)
    
    if min_indv != new_min_indv:
        min_indv = new_min_indv

        print("{} {} {} \n{}\n".format(intro, new_min_word, new_hour_word, new_min_indv))
