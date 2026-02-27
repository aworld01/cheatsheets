kattha = 2
dhur = 9
dhurki = 8

kattha_sqft = 1620 #square fit
dismil = 435.6 #square fit

dismil_kattha = (kattha_sqft / dismil)
dismil_dhur = dismil_kattha / 20
dismil_dhurki = dismil_dhur / 20

total_dismil_kattha = kattha * dismil_kattha
total_dismil_dhur = dhur*dismil_dhur
total_dismil_dhurki = dhurki*dismil_dhurki

all_total_dismil = total_dismil_kattha+total_dismil_dhur+total_dismil_dhurki
all_total_dismil = (f"{all_total_dismil:.2f}")

print(all_total_dismil)