import sys
import random

random.seed()

positions = ["top", "mid", "bot", "support", "jungle"]


#************************************************************#

top_champs = ["Singed", "Irelia", "Garen", "Kayle", "Jax", "Nasus", "Shen", "Shyvana", "Vi", "Teemo"]
mid_champs = ["Akali", "Annie", "Diana", "Ezreal", "Katarina", "Lux", "Morgana", "Ryze", "Veigar"]
bot_champs = ["Ashe", "Caitlyn", "Ezreal", "Graves", "Ms Fortune", "Sivir"]
support_champs = ["Alistar", "Annie", "Blitzcrank", "Janna", "Kayle", "Lux", "Morgana", "Shen", "Sona", "Soraka"]
jungle_champs = ["Amumu", "Diana", "Shyvana", "Vi"]

#************************************************************#


champs_arr = [top_champs, mid_champs, bot_champs, support_champs, jungle_champs]


# Here is where the actual code begins #

if len(sys.argv) > 1:
   position_ndx = int(sys.argv[1])
else:
   position_ndx = random.randint(0, len(positions) - 1)

position = positions[position_ndx]


champ_arr = champs_arr[position_ndx]
champ_ndx = random.randint(0, len(champ_arr) - 1)
champion = champ_arr[champ_ndx]


print( "Your position is: " + position + " and your champion is: " + champion  )
