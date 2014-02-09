package sokoban2;

public class Constants {

	public final static char WALL = '#';
	public final static char EMPTY = ' ';
	public final static char TARGET = '.';
	public final static char PLAYER = '@';
	public final static char PLAYER_ON_TARGET = '+';
	public final static char BOX = '$';
	public final static char BOX_ON_TARGET = '*';
	
	public static final String DEFAULT_LEVEL_URL = "http://basar.idi.ntnu.no/svn/tdt4100/anonymous/trunk/ovinger/resources/sokoban_levels/004.txt";
//	public static final String DEFAULT_LEVEL_URL = "http://folk.ntnu.no/haakool/random/sokoban_lvl/lvl1.txt";
	public static final String DEFAULT__LEVEL_PATH = "/sokoban_levels/004.txt";
	public static final String PATH_TO_LEVELS = "/sokoban_levels/00";
	public static final String PATH_TO_IMAGE = "sokoban/";
	
	public static final int IMGSIZE = 16;
}
