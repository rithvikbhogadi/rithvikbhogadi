package src;

public interface Measures
{
    public double[] measures(IndicatorT ind) throws UnsupportedOperationException;
    public double[] measures(AttributeT att) throws UnsupportedOperationException;
}