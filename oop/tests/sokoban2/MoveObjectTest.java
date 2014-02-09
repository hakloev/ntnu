package sokoban2;

import static org.junit.Assert.*;

import org.junit.Test;

public class MoveObjectTest {

	@Test
	public void test() {
		// Push all directions
		Move pushN = new Move(Direction.NORTH, true);
		Move pushS = new Move(Direction.SOUTH, true);
		Move pushW = new Move(Direction.WEST, true);
		Move pushE = new Move(Direction.EAST, true);
		assertEquals("U", pushN.toString());
		assertEquals("D", pushS.toString());
		assertEquals("L", pushW.toString());
		assertEquals("R", pushE.toString());

		Move noPushN = new Move(Direction.NORTH, false);
		Move noPushS = new Move(Direction.SOUTH, false);
		Move noPushW = new Move(Direction.WEST, false);
		Move noPushE = new Move(Direction.EAST, false);
		assertEquals("u", noPushN.toString());
		assertEquals("d", noPushS.toString());
		assertEquals("l", noPushW.toString());
		assertEquals("r", noPushE.toString());
	}

}
