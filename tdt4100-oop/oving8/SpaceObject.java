package oving8;

import java.awt.Rectangle;

import javax.vecmath.Vector2d;

import acm.graphics.GPoint;
import acm.graphics.GPolygon;
import acm.graphics.GRectangle;

public class SpaceObject extends GPolygon {

	private Vector2d speed;
	private double mass;
	
	public SpaceObject() {
		speed = new Vector2d(0, 0);
		mass = 0;
	}
	
	public double getSpeedX() {
		return speed.x;
	}
	
	public double getSpeedY() {
		return speed.y;
	}
	
	public void setSpeed(double dx, double dy) {
		speed.set(dx, dy);
	}
	
	public void accelerate(double ax, double ay) {
		setSpeed((speed.x + ax), (speed.y + ay));
	}
	
	public double getMass() {
		return mass;
	}
		
	// http://en.wikipedia.org/wiki/Distance
	// http://en.wikipedia.org/wiki/Newton%27s_law_of_universal_gravitation				
	public void applyGravitationalForce(SpaceObject other) {
		double G = 1; //6.7 * Math.pow(10, -11);
//		if (getMass() != 0 && other.getMass() != 0) {
//			double bothMasses = getMass() * other.getMass();
//			double distance = getDistance(other);
//			// F = G*((m1*m2)/(r^2))
//			double force = ((G * bothMasses) / Math.pow(distance, 2));
//			this.accelerate(speed.x * force), speed.y + (force / getMass()));
//		}
		Vector2d distance = this.getDistance(other);
		double accelAmount = ( G*other.getMass() ) / ( Math.pow(distance.length(), 2) );
		Vector2d accelVector = distance;
		accelVector.normalize(); // only interested in direction, make unit vector
		accelVector.scale(accelAmount);
		this.accelerate(accelVector.x, accelVector.y);
	}
	// bruk Newtons law of universal gravitiaton for å få krafta
	// akselerer this med hensyn til X og Y
	
	private Vector2d getDistance(SpaceObject other) {
		// regn ut distansen mellom de to spaceobjektene med calcDistance
//		double deltaX = Math.pow((other.getX() - this.getX()), 2);
//		double deltaY = Math.pow((other.getY() - this.getY()), 2);
//		return (Math.sqrt(deltaX + deltaY));
		return new Vector2d(other.getX()-this.getX(), other.getY()- this.getY());
	}
	
	public boolean intersects(SpaceObject other) {
		if (this.getBounds().intersects(other.getBounds())) {
			return true;
		}
		return false;
	}
	
	public void tick() {
		this.move(speed.x, speed.y);
		
	}
}