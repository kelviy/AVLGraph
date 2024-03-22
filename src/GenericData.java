

/**
 * GenericData class is a class that holds the term, sentence, and score of a term. This is data from GenericsKB.txt file.
 */
public class GenericData implements Comparable<GenericData> {
    private String term;
    private String sentence;
    private double score;

    public GenericData(String term, String sentence, double score) {
        this.term = term;
        this.sentence = sentence;
        this.score = score;
    }

    /**
     * Compares two GenericData objects based on their term.
     */
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

    /**
     * Compares a GenericData object with a term.
     * @param term
     * @return
     */
    public boolean equals(String term) {
        return this.term.equals(term);
    }

    /**
     * Compares two GenericData objects based on their term.
     */
    public int compareTo(GenericData other) {
        return this.term.compareToIgnoreCase(other.term);
    }

    /**
     * Returns a string representation of the GenericData object.
     */
    public String toString() {
        return term + ": " + sentence + " (" + score + ")";
    }

    /**
     * Returns the term of the GenericData object.
     * @return
     */
    public String getTerm() {
        return term;
    }

    /**
     * Sets the term of the GenericData object.
     */
    public void setTerm(String term) {
        this.term = term;
    }

    /**
     * Returns the sentence of the GenericData object.
     * @return
     */
    public String getSentence() {
        return sentence;
    }

    /**
     * Sets the sentence of the GenericData object.
     * @param sentence
     */
    public void setSentence(String sentence) {
        this.sentence = sentence;
    }

    /**
     * Returns the score of the GenericData object.
     * @return
     */
    public double getScore() {
        return score;
    }

    /**
     * Sets the score of the GenericData object.
     * @param score
     */
    public void setScore(double score) {
        this.score = score;
    }

}
