package src;

public class Services
{
    public static int sum(double[] v){
        int sumer = 0;
        for(double num : v){
            sumer = (int) (sumer + num);
        }
        return sumer; 
    }

    static double[] temper;
    public static double[] normal(double[] v){
        for(int i = 0; i < v.length; i++){
            int newVar = i/sum(v);
            temper[i] = newVar;
        }
        return temper;
    }
}