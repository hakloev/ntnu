package sokoban2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;

public class GetLevel implements Level {
	
	private String[] level;
	
	@Override
	public String[] getLines() {
		return this.level;
	}

	public void getFromUrl(String urlToLevel) throws IOException {
		URL url = new URL(urlToLevel);
		InputStreamReader instreamreader = new InputStreamReader(url.openStream());
		BufferedReader in = new BufferedReader(instreamreader);
		
		List<String> tempList = new ArrayList<String>();
		String inputLine;
		while ((inputLine = in.readLine()) != null) {
			tempList.add(inputLine);
		}
		in.close();
		
		level = tempList.toArray(new String[tempList.size()]);
	}

	public void getFromFile(int lvlNr) throws IOException, NullPointerException {
		InputStream instream = getClass().getResourceAsStream(Constants.PATH_TO_LEVELS + lvlNr + ".txt");
		InputStreamReader instreamreader = new InputStreamReader(instream);
		BufferedReader in = new BufferedReader(instreamreader);
		
		List<String> tempList = new ArrayList<String>();
		String inputLine;
		while ((inputLine = in.readLine()) != null) {
			tempList.add(inputLine);
		}
		in.close();
		
		level = tempList.toArray(new String[tempList.size()]);
	}
	
	public void getFromLoad() {
		
	}
}
