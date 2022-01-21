/**
 * Author: Rithvik Bhogadi
 * Revised: March 26 2021
 * 
 * Description: Test driver for AttributeT
 */

package src;

import org.junit.*;
import static org.junit.Assert.*;

public class TestAttributeT
{
    

    @Test
    public void testBlank()
    {   
        testing = new AttributeT("oasas", IndicatorT.math()))
        assertTrue(testing.getName == "oasas");
    }

    public void testBlank()
    {
        testing2 = new AttributeT();
        assertTrue(testing2.getIndicators == IndicatorT.math);
    }

}
