

// Class that stores data for each object
public class GenericData implements Comparable<GenericData> {
    private String term;
    private String sentence;
    private double score;

    public GenericData(String term, String sentence, double score) {
        this.term = term;
        this.sentence = sentence;
        this.score = score;
    }

    public boolean equals(Object other) {
        if (other == null) {
            return false;
        }
        if (!(other instanceof GenericData)) {
            return false;
        }
        GenericData data = (GenericData) other;
        return this.term.equalsIgnoreCase(data.term);
    }

    public boolean equals(String term) {
        return this.term.equals(term);
    }

    public int compareTo(GenericData other) {
        return this.term.compareToIgnoreCase(other.term);
    }

    public String toString() {
        return term + ": " + sentence + " (" + score + ")";
    }

    public String getTerm() {
        return term;
    }

    public void setTerm(String term) {
        this.term = term;
    }

    public String getSentence() {
        return sentence;
    }

    public void setSentence(String sentence) {
        this.sentence = sentence;
    }

    public double getScore() {
        return score;
    }

    public void setScore(double score) {
        this.score = score;
    }

}
