import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
//STEPS
//ArrayList of Semesters
//For Each Semester, get course offerings and store into a hashmap
//Hashmap Key is crn, value is the course
//if the class already exists in the hashmap, don't make alterations
public class ScrapeOSCAR {
	public static void main(String[] args) throws IOException {
		Document doc = Jsoup.connect("https://oscar.gatech.edu/bprod/bwckctlg.p_disp_cat_term_date").get();
		Elements times = doc.getElementsByClass("dedefault");
		ArrayList<String> timesListInitial = new ArrayList<>();
		String longTimeString = "";
		for (Element time : times) {
			longTimeString = time.toString();
		}
		String[] timeArray = longTimeString.split("> <");
		ArrayList<String> timesListFinal = new ArrayList<>(); 
		for (String time : timeArray) {
			if (time.charAt(0) == 'o') {
				time = time.substring(22);
				if (time.charAt(0) == 'F' || time.charAt(0) == 'S' || time.charAt(0) == 'W') {
					String[] tempTime = time.split("<");
					timesListFinal.add(tempTime[0]);
				}
			}
		}
		for (String time : timesListFinal) {
			System.out.println(time);
		}
	}
}