/**
 * Author: Rithvik Bhogadi
 * Revised: March 26 2021
 */
package src;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Arrays;

/*
@brief This class is used for having multiple methods which are related to descriving the different types of
courses within the CEAB
*/
public class CourseT
{
    /*
    @brief This method converts a set to a sequence
    @param s is a set of elements
    @return return the sequence of all the set of elements in set s
    */
    private LOsT[] set_to_seq(HashSet<LOsT> s){
        LOsT[] temperArr = new LOsT[s.size()];
        int count = 0;
        Iterator iterator = s.iterator();
        while(iterator.hasNext()){
            temperArr[count] = (LOsT) iterator.next();
            count++;
        }
        return temperArr;
    }

    /*
    @brief This method does the summation of each element from two arrays together at their respective position
    @param a is double array
    @param b is a double array
    @return returns a array which has sum of the elements between two arrays into one
    */
    private double[] sumMeas(double[] a, double[] b){
        int length = 4;
        double[] theArr = new double[length];
        for(int i = 0; i < length; i++){
            theArr[i] = a[i] + b[i];
        }
        return theArr;
    }

    protected String name;
    protected HashMap<IndicatorT, HashSet<LOsT>> m;

    /*
    @brief This method creates a course
    @param courseName is a string which consists of the courseName
    @param indicators is an IndicatorT array
    */
    public CourseT(String courseName, IndicatorT[] indicators){
        name = courseName;
        HashMap<IndicatorT, HashSet<LOsT>> newHash1 = new HashMap<IndicatorT, HashSet<LOsT>>();
        m = new HashMap<IndicatorT, HashSet<LOsT>>();
        for(int i = 0; i < indicators.length; i++){
            m.put(indicators[i], new HashSet<LOsT>());
        }
    }

    /*
    @brief This methods gets the name of the course
    @return It returns the name
    */
    public String getName(){
        return name;
    }

    /*
    @brief This method gets the indicators
    @return It returns all the elements from a hashset into an IndicatorT array and return that
    */
    public IndicatorT[] getIndicators(){
        IndicatorT[] atempArr = new IndicatorT[m.size()];
        int count = 0;
        for(IndicatorT indicator : m.keySet()){
            atempArr[count] = indicator;
            count++;
        }
        return atempArr;
    }

    /*
    @brief This method gets the learning outcome
    @param indicator is a variable assigned from IndicatorT
    @return a sequence of elements from the hashset
    */
    public LOsT[] getLOs(IndicatorT indicator){
        if(!m.containsKey(indicator)){
            return null;
        }
        else{
            return set_to_seq(m.get(indicator));
        }
    }

    /*
    @brief This method add learning outcomes together
    @param indicator is a variable assigned from IndicatorT
    @param outcome is a variable assigned from LOsT
    */
    public void addLO(IndicatorT indicator, LOsT outcome){
        if(m.containsKey(indicator)){
            m.get(indicator).add(outcome);
        }   
    }

    /*
    @brief This method deletes learning outcomes 
    @param indicator is a variable assigned from IndicatorT
    @param outcome is a variable assigned from LOsT
    */
    public void delLO(IndicatorT indicator, LOsT outcome){
        if(m.containsKey(indicator)){
            m.get(indicator).remove(outcome);
        }   
    }

    /*
    @brief This method checks if the outcome is inside the course
    @param indicator is a variable assigned from IndicatorT
    @param outcomes is a variable assigned from LOsT
    @return returns a boolean 
    */
    public boolean member(IndicatorT indicator, LOsT[] outcomes)
    {
        if(m.containsKey(indicator))
        {
            HashSet<LOsT> setOfLOs = m.get(indicator); //Creating a reference to the hashset
            HashSet<LOsT> setOutcomes = new HashSet<LOsT>(Arrays.asList(outcomes));
            return setOfLOs.equals(setOutcomes);
        }else{
            return false;
        }

    }

    /*
    @brief This method throws an exception
    */
    public void measures(){
        throw new UnsupportedOperationException();
    }

    /*
    @brief This method measures the learning outcome
    @param ind is a variable assigned from IndicatorT
    @return returns a double array 
    */
    public double[] measures(IndicatorT ind){
        if(getLOs(ind).length == 0){
            return new double[] {0,0,0,0};
        }

        double[] measureInd = {0,0,0,0};
        if(Norm.getNInd() == true){
            for(LOsT xyz : getLOs(ind)){
                measureInd = sumMeas(measureInd, xyz.measures());
            }
            return Services.normal(measureInd);
        }
        return measureInd;
    }

    /*
    @brief This method measures the learning outcome
    @param att is a variable assigned from AttributeT
    @return returns a double array 
    */
    public double[] measures(AttributeT att){
        if(att.getIndicators().length == 0){
            return new double[] {0,0,0,0};
        }

        double[] measureInd = {0,0,0,0};
        if(Norm.getNAtt() == true){
            for(IndicatorT zyx : att.getIndicators()){
                measureInd = sumMeas(measureInd, this.measures(zyx));
            }
            return Services.normal(measureInd);
        }
        return measureInd;
    }
}
