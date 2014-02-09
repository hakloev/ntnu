def main():
	mass_kg = float(input('Enter mass: '))
	velocity = float(input('Enter velocity: '))
	print('The kinetic energy is:', kinetic_energy(mass_kg, velocity), 'joule')

def kinetic_energy(mass_kg, velocity):
	return (1/2) * mass_kg * (velocity ** 2)

main()