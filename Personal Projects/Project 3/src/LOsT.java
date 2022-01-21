package src;

public class LOsT
{
    String name;
    int n_blw;
    int n_mrg;
    int n_mts;
    int n_exc;

    public LOsT(String topic, int nblw, int nmrg, int nmts, int nexc){
        name = topic;
        n_blw = nblw;
        n_mrg = nmrg;
        n_mts = nmts;
        n_exc = nexc;

        if((nblw < 0) || (nmrg < 0) || (nmts < 0) || (nexc < 0))
            throw new IllegalArgumentException();
        
        if((nblw == 0) && (nmrg == 0) && (nmts == 0) && (nexc == 0))
            throw new IllegalArgumentException();
        
    }

    public String getName(){
        return name;
    }

    public boolean equals(LOsT o){
        if(name == o.getName())
            return true;
        return false;
    }

    public double[] measures(){
        if(Norm.getNLOs() == false){
            return new double[] {n_blw, n_mrg, n_mts, n_exc};
        }
        else if(Norm.getNLOs() == true){
            return normal(new double[] {n_blw, n_mrg, n_mts, n_exc});
        }
        else{
            return null;
        }
    }

    private double[] normal(double[] ds) {
        return null;
    }

    public void measures(IndicatorT ind){
        throw new UnsupportedOperationException();
    }

    public void measures(AttributeT att){
        throw new UnsupportedOperationException();
    }
}