import java.util.*;
//Schedule Class, contains all of the courses for the current user
public class Schedule {
    private ArrayList<Course> schedule;
    private int totalCreditHours;
    public Schedule() {
        schedule = new ArrayList<>();
        totalCreditHours = 0;
    }
    public void addClass(Course c) throws MissingPreReqException {
        if (c.getPreReqs() == null) {
            schedule.addToBack(c);
            totalCreditHours += c.getCreditHours();
        } else {
            for (int a = 0; a < c.getPreReqs().size(); a++) {
                if (!(contains(c.getPreReqs().get(a)))) {
                    throw new MissingPreReqException(c.getPreReqs().get(a).getPrefix(), c.getPrefix());
                }
            }
            schedule.addToBack(c);
            totalCreditHours += c.getCreditHours();
        }
    }
    private boolean contains(Course c) {
        for (int a = 0; a < schedule.size(); a++) {
            if (schedule.get(a).equals(c)) {
                return true;
            }
        }
        return false;
    }
    private class MissingPreReqException extends Exception {
        private MissingPreReqException(String p, String s) {
            super("Missing " + p + ", cannot add " + s);
        }
    }
}
