package oving8;

import java.awt.Color;

public class Spaceship extends SpaceObject {
	
	private int angle = 0;
	
	public Spaceship() {
		setColor(Color.WHITE);
		addEdge(5, 0);
		addEdge(-10, -1);
		addEdge(0, 6);
	}
	
	public double getMass() {
		return 50;
	}

	public void setDirection(int direction){
		this.angle = direction;
		this.rotate(direction);	
	}
	
	public void incrementDirection(int angle){
		this.angle -= angle;
		this.rotate(angle);
	}
	
	public void thrust(){
		double radians = angle*Math.PI/180;
		this.accelerate(0.5*Math.cos(radians), 0.5*Math.sin(radians));
	}
}
