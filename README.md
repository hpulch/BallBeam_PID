# BallBeam_PID
Documentation, application and implementation for a PID controlled Ball-and-beam style plant.



## Mechanical Design
The ball and beam system is a well studied control problem, uMichigan has a great model available online.
![Screenshot](https://github.com/hpulch/BallBeam_PID/blob/main/uMichiganModel_BallandBeam.jpg)

### Transfer Function

In uMichigan's Ball and Beam model there is this assumption that the relationship between $\alpha$ and $\theta$ is approximately linearized by $d \over L$. This will reduce the control problem's complexity and make the overall design pheasible.
$$\alpha = {d \over L} \theta \tag{1}$$

Kinematic Equations

$$ x=1\tag{}$$

Potential Energy

$$ V=\tag{}$$

Kinetic Energy

$$ T=\tag{}$$ 

LaGrangian, Equations of Motion

$$ L = T - V $$

$$ L = \tag{} $$

$$ 0 = {\partial L \over \partial q_j} - {d\over dt} ({\partial L \over \partial \dot q_j}) \tag{234} $$

Testingdfg
dfg
dfgdfgdfg











# Electronic Design Considerations

# Software Design Considerations





Reference Materials:
  -  PID control theory from CalTech https://www.cds.caltech.edu/~murray/books/AM08/pdf/am06-pid_16Sep06.pdf
  -  Ball and Beam system model from uMichigan https://ctms.engin.umich.edu/CTMS/index.php?example=BallBeam&section=SystemModeling#1
  -  Stepper Motor https://pdf1.alldatasheet.com/datasheet-pdf/download/1141537/STEPPERONLINE/17HS08-1004S.html
