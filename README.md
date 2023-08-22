# BallBeam_PID

Balance an object onto a beam about a set point and reject disturbances. 

![Screenshot](https://github.com/hpulch/BallBeam_PID/blob/main/uMichiganModel_BallandBeam.jpg)

The objective of this project is to design and develop a prototype plant and PID controller to demonstrate a practical solution to the [ball and beam control problem](https://ctms.engin.umich.edu/CTMS/index.php?example=BallBeam&section=SystemModeling#1). System response of this control case is categorized as [maginally stable](https://en.wikipedia.org/wiki/Marginal_stability) and, as such, using a proportional controller will cause an oscillation about the system's target position. A heuristic approach to tuning the PID parameters can be implemented using the [Ziegler-Nichols method](https://en.wikipedia.org/wiki/Ziegler%E2%80%93Nichols_method), where the oscillating properties of a proportionally controlled plant can be used to develop $K_p, K_i, K_d$ gain parameters to reject disturbances. 

### Electromechanical Design
IV Projects developed a very elegant physical layout which will be the reference model.

### Electronic Design





### Software Design Considerations





Reference Materials:
  -  [Ziegler-Nichols Method](https://www.mstarlabs.com/control/znrule.html)
  -  [Ball and Beam system model](https://ctms.engin.umich.edu/CTMS/index.php?example=BallBeam&section=SystemModeling#1)
  -  [Maginally Stable](https://en.wikipedia.org/wiki/Marginal_stability)
  -  Stepper Motor https://pdf1.alldatasheet.com/datasheet-pdf/download/1141537/STEPPERONLINE/17HS08-1004S.html
