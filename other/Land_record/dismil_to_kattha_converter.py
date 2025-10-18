x_dismil = 9.19

kattha_sqft = 1620 #square fit
dismil = 435.6 #square fit
kattha_dismil = kattha_sqft / dismil
dhur_dismil = kattha_dismil / 20
dhurki_dismil = dhur_dismil / 20

total_dhur = int(x_dismil / dhur_dismil)
total_dhur = int(x_dismil / dhur_dismil)
total_dhurki = round(x_dismil / dhurki_dismil)

kattha = int(x_dismil / kattha_dismil)
dhur = total_dhur % 20
dhurki = total_dhurki % 20

print(f"Dismil: {x_dismil}")
print(f"{kattha}: Katha, {dhur}: Dhur, {dhurki}: Dhurki")