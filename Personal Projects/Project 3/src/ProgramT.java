package src;

import java.util.HashSet;

public class ProgramT extends HashSet<CourseT>{

    
    private double[] sumMeas(double[] a, double[] b){
        int length = 4;
        double[] theArr = new double[length];
        for(int i = 0; i < length; i++){
            theArr[i] = a[i] + b[i];
        }
        return theArr;
    }

    public void measures(){
        throw new UnsupportedOperationException();
    }

    public void measures(IndicatorT ind){
        throw new UnsupportedOperationException();
    }

    public double[] measures(AttributeT att){
        double[] theMeasure = {0,0,0,0};
        if(Norm.getNAtt() == true){
            for(IndicatorT zyx : att.getIndicators()){
                theMeasure = sumMeas(theMeasure, this.measures(att));
            }
            return Services.normal(theMeasure);
        }
        return theMeasure;
    }
}
