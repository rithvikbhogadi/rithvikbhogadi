package src;

import java.util.HashSet;

public class AttributeT
{
    String name;
    HashSet<IndicatorT> s;

    public AttributeT(String attribName, IndicatorT[] indicators){
        name = attribName;
        HashSet<IndicatorT> newHash = new HashSet<IndicatorT>();
        for(int i = 0; i < indicators.length; i++){
            newHash.add(indicators[i]);
        }
        s = newHash;
    }

    public String getName()
    {
        return name;
    }

    public IndicatorT[] getIndicators()
    {
        IndicatorT[] sampleArr = new IndicatorT[s.size()];
        sampleArr = (IndicatorT[]) s.toArray(sampleArr);
        return sampleArr;
    }

}
