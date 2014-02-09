package oving8;

import java.awt.Color;

public class Asteroid extends SpaceObject {
	
	private double density;
	private double radius;
	
	public Asteroid(double density, double radius, int cornerCount) {
		this.density = density;
		this.radius = radius;
		setColor(Color.WHITE);
		
		int theta = 360/cornerCount;
		for (int i = 1; i <= cornerCount; i++) {
			this.addPolarEdge(radius, 360-i*theta);
		}
		
	}
	
	public double getMass() {
		double V = ((4 * Math.PI * Math.pow(radius, 3)) / 3);	// p = m/V --> m = pV
		return density * V;
	}
}
