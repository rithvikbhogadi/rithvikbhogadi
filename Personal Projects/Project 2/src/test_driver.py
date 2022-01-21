## @file test_driver.py
#  @author Rithvik Bhogadi
#  @brief tests the methods from various modules
#  @date 02/16/2021

from CircleT import CircleT
from TriangleT import TriangleT
from BodyT import BodyT
from Scene import Scene

from pytest import *

class TestCircleT:

    # initialize an instance of Set for each test
    def setup_method(self, method):
        self.object1 = CircleT(1,2,3,45)

    # reset state variables
    def teardown_method(self, method):
        self.object1 = None
        
    # test_to_cmx method
    def test_to_cmx(self): 
        assert self.object1.cm_x()==1
    
    # test_to_cmy method
    def test_to_cmy(self):
        assert self.object1.cm_y()==2
    
    # test_to_mass method
    def test_to_mass(self):
        assert self.object1.mass()==45
    
    # test_to_m_inert method
    def test_to_m_inert(self):
        assert self.object1.m_inert()==202.5
    
    def test_toexceptionr(self):
        with raises(ValueError):
            CircleT(1,2,-4,6) 


class TestTriangleT:

    # initialize an instance of Set for each test
    def setup_method(self, method):
        self.object2 = TriangleT(2,4,5,6)

    # reset state variables
    def teardown_method(self, method):
        self.object2 = None

    # test_to_cmx method
    def test_to_cmx(self): 
        assert self.object2.cm_x()==2


    def test_to_cmy(self):
        assert self.object2.cm_y()==4
    

    def test_to_mass(self):
        assert self.object2.mass()==6
    
    
    def test_to_m_inert(self):
        assert self.object2.m_inert()==12.5

    def test_toexceptions(self):
        with raises(ValueError):
            TriangleT(2,4,-5,7)

class TestBodyT:

    # initialize an instance of Set for each test
    def setup_method(self, method):
        self.cmxs = [3.0, 5.0, 2.0, 4.0]
        self.cmys = [6.0, 9.0, 5.0, 8.0]
        self.ms = [2.0, 3.0, 1.0, 4.0]
        self.object3 = BodyT(self.cmxs, self.cmys, self.ms)

    # reset state variables
    def teardown_method(self, method):
        self.object3 = None

    # test_to_cmx method
    def test_to_cmx(self): 
        assert self.object3.cm_x()==(39.0/10.0)


    def test_to_cmy(self):
        assert self.object3.cm_y()==(76.0/10.0)
    

    def test_to_mass(self):
        assert self.object3.mass()==10.0
    
    def test_to_m_inert(self):
        assert self.object3.m_inert()==(757-729.7)
    
    def test_toexceptionlists(self):
        with raises(ValueError):
            self.cmxs = [3.0, 5.0, 2.0, 4.0]
            self.cmys = [6.0, 9.0, 5.0, 8.0]
            self.ms = [2.0, 3.0, 1.0]
            BodyT(self.cmxs, self.cmys, self.ms)

class TestScene:

    def Fx(self, t):
        return 5 if t < 5 else 0


    def Fy(self, t):
        g = 9.81  # accel due to gravity (m/s^2)
        m = 1  # mass (kg)
        return -g * m if t < 3 else g * m

    # initialize an instance of Set for each test
    def setup_method(self, method):
        self.object4 = Scene(CircleT(1,2,3,4), self.Fx, self.Fy, 4, 5)
    # reset state variables
    def teardown_method(self, method):
        self.object4 = None

    def test_getshape(self):
        assert self.object4.get_shape().cm_x() == CircleT(1,2,3,4).cm_x()

    def test_getinitvelo(self):
        assert self.object4.get_init_velo() == (4,5)

    def test_setshape(self):
        self.object4.set_shape(CircleT(2,3,4,5)) 
        assert self.object4.get_shape().cm_x() == CircleT(2,3,4,5).cm_x()
    
    def test_setinitvelo(self):
        self.object4.set_init_velo(79,300)
        assert self.object4.get_init_velo() == (79,300)


    
    

    

