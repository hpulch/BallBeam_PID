# BallBeam_PID
Documentation and Application for a PID controlled Ball-and-beam style plant

# Mechanical Design Considerations
The ball and beam system is a well studied control problem, uMichigan has a great model available online.
![Screenshot](https://github.com/hpulch/BallBeam_PID/blob/main/uMichiganModel_BallandBeam.jpg)

In uMichigan's Ball and Beam model there is this assumption that the relationship between $\alpha$ and $\theta$ is approximately linearized by $d \over L$. In order to use this assumption we need to make some mechanical design decisions to minimize the non-linear component of the system.

$$
Displacement = d sin(\theta)
$$

$$
Displacement(cos(\beta)) = Lsin(\alpha)
$$

The nonlinear component $\beta$ can be set to its maximum when $\theta = 0$ which can be expressed as $\beta_{max} = sin^{-1}({d \over A})$. To minimize $\beta_{max}$ a suitable $A$ and $d$ should be selected such that $d << A$. Selecting $d$ to be too small will result in a low displacement and selecting $A$ to be too large will scale up the displacement error.

# Electronic Design Considerations

# Software Design Considerations





Reference Materials:
  -  PID control theory from CalTech https://www.cds.caltech.edu/~murray/books/AM08/pdf/am06-pid_16Sep06.pdf
  -  Ball and Beam system model from uMichigan https://ctms.engin.umich.edu/CTMS/index.php?example=BallBeam&section=SystemModeling#1
  -  Stepper Motor https://pdf1.alldatasheet.com/datasheet-pdf/download/1141537/STEPPERONLINE/17HS08-1004S.html
