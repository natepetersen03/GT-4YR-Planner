import java.util.*;
public class Course {
    private String name;
    private String prefix;
    private String subject;
    private ArrayList<Course> preReqs;
    private int creditHours;
    //Constructor
    public Course(String name, String prefix, String subject, ArrayList<Course> preReqs, int creditHours) {
        this.name = name;
        this.prefix = prefix;
        this.preReqs = preReqs;
        this.creditHours = creditHours;
    }
    public String getName() {
        return name;
    }
    public String getPrefix() {
        return prefix;
    }
    public String getSubject() { return subject; }
    public ArrayList<Course> getPreReqs() {
        return preReqs;
    }
    public int getCreditHours() {
        return creditHours;
    }
    public void setName(String name) {
        this.name = name;
    }
    public void setPrefix(String prefix) {
        this.prefix = prefix;
    }
    public void setPreReqs(ArrayList<Course> preReqs) {
        this.preReqs = preReqs;
    }
    public void setPreReqs(ArrayList<Course> prereqs, Course c) {
        prereqs.addToBack(c);
        preReqs = prereqs;
    }
    public void setCreditHours(int creditHours) {
        this.creditHours = creditHours;
    }
    public void setSubject(String subject) { this.subject = subject; }
}
