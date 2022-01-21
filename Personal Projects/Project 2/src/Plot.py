## @file
#  @author
#  @brief
#  @date
#  @details

import matplotlib.pyplot as plt

def plot(w,t):
    if not (len(w) == len(t)):
        raise ValueError
    x = []
    y = []
    for i in range(len(w)):
        x.append(w[i][0])
        y.append(w[i][1])
    
    fig, (xvt, yvt, yvx) = plt.subplots(3)
    fig.suptitle("Motion Simulation")
    yvx.plot(x, y)
    yvx.set(xlabel="x(m)", ylabel="y(m)")
    xvt.plot(t,x)
    xvt.set(xlabel="t(m)", ylabel="x(m)")
    yvt.plot(t,y)
    yvt.set(xlabel="t(m)", ylabel="y(m)")
    plt.show()
    


    
