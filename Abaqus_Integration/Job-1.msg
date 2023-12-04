1

   Abaqus Learning Edition 2023                                  Date 24-Nov-2023   Time 09:33:06
   

                                                                                 
                                                                                 
 STEP    1     INCREMENT     1     STEP TIME    0.00    


                        S T E P       1     S T A T I C   A N A L Y S I S


                                                                                          

          FIXED TIME INCREMENTS
          TIME INCREMENT IS                                    0.100    
          TIME PERIOD IS                                        1.00    

     LINEAR EQUATION SOLVER TYPE         DIRECT SPARSE

 CONVERGENCE TOLERANCE PARAMETERS FOR FORCE    
     CRITERION FOR RESIDUAL FORCE     FOR A NONLINEAR PROBLEM          5.000E-03
     CRITERION FOR DISP.    CORRECTION IN A NONLINEAR PROBLEM          1.000E-02
     INITIAL VALUE OF TIME AVERAGE FORCE                               1.000E-02
     AVERAGE FORCE     IS TIME AVERAGE FORCE    
     ALTERNATE CRIT. FOR RESIDUAL FORCE     FOR A NONLINEAR PROBLEM    2.000E-02
     CRITERION FOR ZERO FORCE     RELATIVE TO TIME AVRG. FORCE         1.000E-05
     CRITERION FOR RESIDUAL FORCE     WHEN THERE IS ZERO FLUX          1.000E-05
     CRITERION FOR DISP.    CORRECTION WHEN THERE IS ZERO FLUX         1.000E-03
     CRITERION FOR RESIDUAL FORCE     FOR A LINEAR INCREMENT           1.000E-08
     FIELD CONVERSION RATIO                                             1.00    
     CRITERION FOR ZERO FORCE     REL. TO TIME AVRG. MAX. FORCE        1.000E-05
     CRITERION FOR ZERO DISP.    RELATIVE TO CHARACTERISTIC LENGTH     1.000E-08

 CONVERGENCE TOLERANCE PARAMETERS FOR MOMENT   
     CRITERION FOR RESIDUAL MOMENT    FOR A NONLINEAR PROBLEM          5.000E-03
     CRITERION FOR ROTATION CORRECTION IN A NONLINEAR PROBLEM          1.000E-02
     INITIAL VALUE OF TIME AVERAGE MOMENT                              1.000E-02
     AVERAGE MOMENT    IS TIME AVERAGE MOMENT   
     ALTERNATE CRIT. FOR RESIDUAL MOMENT    FOR A NONLINEAR PROBLEM    2.000E-02
     CRITERION FOR ZERO MOMENT    RELATIVE TO TIME AVRG. MOMENT        1.000E-05
     CRITERION FOR RESIDUAL MOMENT    WHEN THERE IS ZERO FLUX          1.000E-05
     CRITERION FOR ROTATION CORRECTION WHEN THERE IS ZERO FLUX         1.000E-03
     CRITERION FOR RESIDUAL MOMENT    FOR A LINEAR INCREMENT           1.000E-08
     FIELD CONVERSION RATIO                                             1.00    
     CRITERION FOR ZERO MOMENT    REL. TO TIME AVRG. MAX. MOMENT       1.000E-05

     VOLUMETRIC STRAIN COMPATIBILITY TOLERANCE FOR HYBRID SOLIDS       1.000E-05
     AXIAL STRAIN COMPATIBILITY TOLERANCE FOR HYBRID BEAMS             1.000E-05
     TRANS. SHEAR STRAIN COMPATIBILITY TOLERANCE FOR HYBRID BEAMS      1.000E-05
     SOFT CONTACT CONSTRAINT COMPATIBILITY TOLERANCE FOR P>P0          5.000E-03
     SOFT CONTACT CONSTRAINT COMPATIBILITY TOLERANCE FOR P=0.0         0.100    
     CONTACT FORCE ERROR TOLERANCE FOR CONVERT SDI=YES                 1.00    
     DISPLACEMENT COMPATIBILITY TOLERANCE FOR DCOUP ELEMENTS           1.000E-05
     ROTATION COMPATIBILITY TOLERANCE FOR DCOUP ELEMENTS               1.000E-05

 EQUILIBRIUM WILL BE CHECKED FOR SEVERE DISCONTINUITY ITERATIONS

 ITERATION CONTROL PARAMETERS:
     FIRST EQUILIBRIUM ITERATION FOR CONSECUTIVE DIVERGENCE CHECK              4
     EQUILIBRIUM ITERATION AFTER WHICH ALTERNATE RESIDUAL IS USED              9
     MAXIMUM EQUILIBRIUM ITERATIONS ALLOWED                                   16
     MAXIMUM ITERATIONS FOR SEVERE DISCONTINUITIES                            12
     GLOBAL STABILIZATION CONTROL IS NOT USED

          PRINT OF INCREMENT NUMBER, TIME, ETC., EVERY    1  INCREMENTS

     THE MAXIMUM NUMBER OF INCREMENTS IN THIS STEP IS                     100

     LINEAR EXTRAPOLATION WILL BE USED

     CHARACTERISTIC ELEMENT LENGTH      3.96    

     DETAILS REGARDING ACTUAL SOLUTION WAVEFRONT REQUESTED

     DETAILED OUTPUT OF DIAGNOSTICS TO DATABASE REQUESTED

     PRINT OF INCREMENT NUMBER, TIME, ETC., TO THE MESSAGE FILE EVERY     1  INCREMENTS

     COLLECTING MODEL CONSTRAINT INFORMATION FOR OVERCONSTRAINT CHECKS

     COLLECTING STEP CONSTRAINT INFORMATION FOR OVERCONSTRAINT CHECKS


  INCREMENT     1 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  1260
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      7.497e+06
        SOLVER ELAPSED TIME:  11ms

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       47.1       TIME AVG. FORCE        47.1    
 LARGEST SCALED RESIDUAL FORCE      7.350E-11   AT NODE        160   DOF  2
   INSTANCE: ROOF-1                                                                          
  CORRESPONDING RESIDUAL FORCE      7.350E-11
 LARGEST INCREMENT OF DISP.        -0.974       AT NODE        158   DOF  2
   INSTANCE: ROOF-1                                                                          
 LARGEST CORRECTION TO DISP.       -0.974       AT NODE        158   DOF  2
   INSTANCE: ROOF-1                                                                          
          THE FORCE     EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 AVERAGE MOMENT                      192.       TIME AVG. MOMENT       192.    
 LARGEST SCALED RESIDUAL MOMENT    -4.434E-11   AT NODE        151   DOF  6
   INSTANCE: ROOF-1                                                                          
  CORRESPONDING RESIDUAL MOMENT    -4.434E-11
 LARGEST INCREMENT OF ROTATION      0.100       AT NODE        143   DOF  6
   INSTANCE: ROOF-1                                                                          
 LARGEST CORRECTION TO ROTATION     0.100       AT NODE        143   DOF  6
   INSTANCE: ROOF-1                                                                          
          THE MOMENT    EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.100    
 STEP TIME COMPLETED       0.100    ,  TOTAL TIME COMPLETED        0.100    


  INCREMENT     2 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  1260
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      7.497e+06
        SOLVER ELAPSED TIME:  2ms

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       234.       TIME AVG. FORCE        141.    
 LARGEST SCALED RESIDUAL FORCE      5.025E-11   AT NODE        167   DOF  2
   INSTANCE: ROOF-1                                                                          
  CORRESPONDING RESIDUAL FORCE      5.025E-11
 LARGEST INCREMENT OF DISP.        -0.974       AT NODE        158   DOF  2
   INSTANCE: ROOF-1                                                                          
 LARGEST CORRECTION TO DISP.        5.461E-14   AT NODE        159   DOF  2
   INSTANCE: ROOF-1                                                                          
          THE FORCE     EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 AVERAGE MOMENT                      426.       TIME AVG. MOMENT       309.    
 LARGEST SCALED RESIDUAL MOMENT     7.481E-11   AT NODE        160   DOF  6
   INSTANCE: ROOF-1                                                                          
  CORRESPONDING RESIDUAL MOMENT     7.481E-11
 LARGEST INCREMENT OF ROTATION      0.100       AT NODE        143   DOF  6
   INSTANCE: ROOF-1                                                                          
 LARGEST CORRECTION TO ROTATION     7.883E-15   AT NODE        161   DOF  4
   INSTANCE: ROOF-1                                                                          
          THE MOMENT    EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.200    
 STEP TIME COMPLETED       0.200    ,  TOTAL TIME COMPLETED        0.200    


  INCREMENT     3 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  1260
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      7.497e+06
        SOLVER ELAPSED TIME:  2ms

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       351.       TIME AVG. FORCE        211.    
 LARGEST SCALED RESIDUAL FORCE      8.765E-11   AT NODE        159   DOF  2
   INSTANCE: ROOF-1                                                                          
  CORRESPONDING RESIDUAL FORCE      8.765E-11
 LARGEST INCREMENT OF DISP.        -0.974       AT NODE        158   DOF  2
   INSTANCE: ROOF-1                                                                          
 LARGEST CORRECTION TO DISP.       -2.832E-14   AT NODE        159   DOF  2
   INSTANCE: ROOF-1                                                                          
          THE FORCE     EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 AVERAGE MOMENT                      640.       TIME AVG. MOMENT       419.    
 LARGEST SCALED RESIDUAL MOMENT    -9.027E-11   AT NODE        160   DOF  4
   INSTANCE: ROOF-1                                                                          
  CORRESPONDING RESIDUAL MOMENT    -9.027E-11
 LARGEST INCREMENT OF ROTATION      0.100       AT NODE        143   DOF  6
   INSTANCE: ROOF-1                                                                          
 LARGEST CORRECTION TO ROTATION    -3.826E-15   AT NODE        161   DOF  4
   INSTANCE: ROOF-1                                                                          
          THE MOMENT    EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.300    
 STEP TIME COMPLETED       0.300    ,  TOTAL TIME COMPLETED        0.300    


  INCREMENT     4 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  1260
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      7.497e+06
        SOLVER ELAPSED TIME:  2ms

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       468.       TIME AVG. FORCE        275.    
 LARGEST SCALED RESIDUAL FORCE      1.259E-10   AT NODE        150   DOF  2
   INSTANCE: ROOF-1                                                                          
  CORRESPONDING RESIDUAL FORCE      1.259E-10
 LARGEST INCREMENT OF DISP.        -0.974       AT NODE        158   DOF  2
   INSTANCE: ROOF-1                                                                          
 LARGEST CORRECTION TO DISP.        2.029E-15   AT NODE        159   DOF  2
   INSTANCE: ROOF-1                                                                          
          THE FORCE     EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 AVERAGE MOMENT                      853.       TIME AVG. MOMENT       528.    
 LARGEST SCALED RESIDUAL MOMENT    -1.442E-10   AT NODE        157   DOF  6
   INSTANCE: ROOF-1                                                                          
  CORRESPONDING RESIDUAL MOMENT    -1.442E-10
 LARGEST INCREMENT OF ROTATION      0.100       AT NODE        143   DOF  6
   INSTANCE: ROOF-1                                                                          
 LARGEST CORRECTION TO ROTATION    -5.158E-16   AT NODE        110   DOF  6
   INSTANCE: ROOF-1                                                                          
          THE MOMENT    EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.400    
 STEP TIME COMPLETED       0.400    ,  TOTAL TIME COMPLETED        0.400    


  INCREMENT     5 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  1260
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      7.497e+06
        SOLVER ELAPSED TIME:  2ms

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       585.       TIME AVG. FORCE        337.    
 LARGEST SCALED RESIDUAL FORCE     -1.507E-10   AT NODE        159   DOF  2
   INSTANCE: ROOF-1                                                                          
  CORRESPONDING RESIDUAL FORCE     -1.507E-10
 LARGEST INCREMENT OF DISP.        -0.974       AT NODE        158   DOF  2
   INSTANCE: ROOF-1                                                                          
 LARGEST CORRECTION TO DISP.        1.329E-15   AT NODE        174   DOF  2
   INSTANCE: ROOF-1                                                                          
          THE FORCE     EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 AVERAGE MOMENT                     1.066E+03   TIME AVG. MOMENT       635.    
 LARGEST SCALED RESIDUAL MOMENT    -1.241E-10   AT NODE        151   DOF  6
   INSTANCE: ROOF-1                                                                          
  CORRESPONDING RESIDUAL MOMENT    -1.241E-10
 LARGEST INCREMENT OF ROTATION      0.100       AT NODE        143   DOF  6
   INSTANCE: ROOF-1                                                                          
 LARGEST CORRECTION TO ROTATION    -5.736E-16   AT NODE        157   DOF  6
   INSTANCE: ROOF-1                                                                          
          THE MOMENT    EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.500    
 STEP TIME COMPLETED       0.500    ,  TOTAL TIME COMPLETED        0.500    


  INCREMENT     6 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  1260
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      7.497e+06
        SOLVER ELAPSED TIME:  2ms

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       702.       TIME AVG. FORCE        398.    
 LARGEST SCALED RESIDUAL FORCE      1.239E-10   AT NODE        110   DOF  2
   INSTANCE: ROOF-1                                                                          
  CORRESPONDING RESIDUAL FORCE      1.239E-10
 LARGEST INCREMENT OF DISP.        -0.974       AT NODE        158   DOF  2
   INSTANCE: ROOF-1                                                                          
 LARGEST CORRECTION TO DISP.       -2.305E-15   AT NODE        165   DOF  2
   INSTANCE: ROOF-1                                                                          
          THE FORCE     EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 AVERAGE MOMENT                     1.279E+03   TIME AVG. MOMENT       743.    
 LARGEST SCALED RESIDUAL MOMENT     2.178E-10   AT NODE        160   DOF  6
   INSTANCE: ROOF-1                                                                          
  CORRESPONDING RESIDUAL MOMENT     2.178E-10
 LARGEST INCREMENT OF ROTATION      0.100       AT NODE        143   DOF  6
   INSTANCE: ROOF-1                                                                          
 LARGEST CORRECTION TO ROTATION     6.530E-16   AT NODE        165   DOF  4
   INSTANCE: ROOF-1                                                                          
          THE MOMENT    EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.600    
 STEP TIME COMPLETED       0.600    ,  TOTAL TIME COMPLETED        0.600    


  INCREMENT     7 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  1260
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      7.497e+06
        SOLVER ELAPSED TIME:  2ms

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       819.       TIME AVG. FORCE        458.    
 LARGEST SCALED RESIDUAL FORCE     -2.046E-10   AT NODE        159   DOF  2
   INSTANCE: ROOF-1                                                                          
  CORRESPONDING RESIDUAL FORCE     -2.046E-10
 LARGEST INCREMENT OF DISP.        -0.974       AT NODE        158   DOF  2
   INSTANCE: ROOF-1                                                                          
 LARGEST CORRECTION TO DISP.       -2.970E-15   AT NODE        152   DOF  2
   INSTANCE: ROOF-1                                                                          
          THE FORCE     EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 AVERAGE MOMENT                     1.493E+03   TIME AVG. MOMENT       850.    
 LARGEST SCALED RESIDUAL MOMENT     1.592E-10   AT NODE        166   DOF  6
   INSTANCE: ROOF-1                                                                          
  CORRESPONDING RESIDUAL MOMENT     1.592E-10
 LARGEST INCREMENT OF ROTATION      0.100       AT NODE        143   DOF  6
   INSTANCE: ROOF-1                                                                          
 LARGEST CORRECTION TO ROTATION     1.070E-15   AT NODE        167   DOF  4
   INSTANCE: ROOF-1                                                                          
          THE MOMENT    EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.700    
 STEP TIME COMPLETED       0.700    ,  TOTAL TIME COMPLETED        0.700    


  INCREMENT     8 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  1260
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      7.497e+06
        SOLVER ELAPSED TIME:  2ms

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       937.       TIME AVG. FORCE        518.    
 LARGEST SCALED RESIDUAL FORCE     -1.619E-10   AT NODE        165   DOF  2
   INSTANCE: ROOF-1                                                                          
  CORRESPONDING RESIDUAL FORCE     -1.619E-10
 LARGEST INCREMENT OF DISP.        -0.974       AT NODE        158   DOF  2
   INSTANCE: ROOF-1                                                                          
 LARGEST CORRECTION TO DISP.        4.206E-15   AT NODE        167   DOF  2
   INSTANCE: ROOF-1                                                                          
          THE FORCE     EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 AVERAGE MOMENT                     1.706E+03   TIME AVG. MOMENT       957.    
 LARGEST SCALED RESIDUAL MOMENT     1.637E-10   AT NODE        174   DOF  6
   INSTANCE: ROOF-1                                                                          
  CORRESPONDING RESIDUAL MOMENT     1.637E-10
 LARGEST INCREMENT OF ROTATION      0.100       AT NODE        143   DOF  6
   INSTANCE: ROOF-1                                                                          
 LARGEST CORRECTION TO ROTATION    -9.056E-16   AT NODE        157   DOF  4
   INSTANCE: ROOF-1                                                                          
          THE MOMENT    EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.800    
 STEP TIME COMPLETED       0.800    ,  TOTAL TIME COMPLETED        0.800    


  INCREMENT     9 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  1260
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      7.497e+06
        SOLVER ELAPSED TIME:  2ms

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      1.054E+03   TIME AVG. FORCE        578.    
 LARGEST SCALED RESIDUAL FORCE     -3.756E-10   AT NODE        159   DOF  2
   INSTANCE: ROOF-1                                                                          
  CORRESPONDING RESIDUAL FORCE     -3.756E-10
 LARGEST INCREMENT OF DISP.        -0.974       AT NODE        158   DOF  2
   INSTANCE: ROOF-1                                                                          
 LARGEST CORRECTION TO DISP.       -5.388E-15   AT NODE        167   DOF  2
   INSTANCE: ROOF-1                                                                          
          THE FORCE     EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 AVERAGE MOMENT                     1.919E+03   TIME AVG. MOMENT      1.064E+03
 LARGEST SCALED RESIDUAL MOMENT     4.566E-10   AT NODE        167   DOF  6
   INSTANCE: ROOF-1                                                                          
  CORRESPONDING RESIDUAL MOMENT     4.566E-10
 LARGEST INCREMENT OF ROTATION      0.100       AT NODE        143   DOF  6
   INSTANCE: ROOF-1                                                                          
 LARGEST CORRECTION TO ROTATION     1.143E-15   AT NODE        157   DOF  4
   INSTANCE: ROOF-1                                                                          
          THE MOMENT    EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED  0.900    
 STEP TIME COMPLETED       0.900    ,  TOTAL TIME COMPLETED        0.900    


  INCREMENT    10 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  0.100    
 
	SYMMETRIC DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  1260
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      7.497e+06
        SOLVER ELAPSED TIME:  2ms

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                      1.171E+03   TIME AVG. FORCE        637.    
 LARGEST SCALED RESIDUAL FORCE      2.215E-10   AT NODE        158   DOF  2
   INSTANCE: ROOF-1                                                                          
  CORRESPONDING RESIDUAL FORCE      2.215E-10
 LARGEST INCREMENT OF DISP.        -0.974       AT NODE        158   DOF  2
   INSTANCE: ROOF-1                                                                          
 LARGEST CORRECTION TO DISP.        7.243E-15   AT NODE        167   DOF  2
   INSTANCE: ROOF-1                                                                          
          THE FORCE     EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 AVERAGE MOMENT                     2.132E+03   TIME AVG. MOMENT      1.171E+03
 LARGEST SCALED RESIDUAL MOMENT    -2.947E-10   AT NODE        109   DOF  6
   INSTANCE: ROOF-1                                                                          
  CORRESPONDING RESIDUAL MOMENT    -2.947E-10
 LARGEST INCREMENT OF ROTATION      0.100       AT NODE        143   DOF  6
   INSTANCE: ROOF-1                                                                          
 LARGEST CORRECTION TO ROTATION    -1.958E-15   AT NODE        166   DOF  4
   INSTANCE: ROOF-1                                                                          
          THE MOMENT    EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  0.100    ,  FRACTION OF STEP COMPLETED   1.00    
 STEP TIME COMPLETED        1.00    ,  TOTAL TIME COMPLETED         1.00    


          THE ANALYSIS HAS BEEN COMPLETED



     ANALYSIS SUMMARY:
     TOTAL OF         10  INCREMENTS
                       0  CUTBACKS IN AUTOMATIC INCREMENTATION
                      10  ITERATIONS INCLUDING CONTACT ITERATIONS IF PRESENT
                      10  PASSES THROUGH THE EQUATION SOLVER OF WHICH 
                       1  INVOLVE MATRIX DECOMPOSITION, INCLUDING
                       0  DECOMPOSITION(S) OF THE MASS MATRIX
                       1  REORDERING OF EQUATIONS TO MINIMIZE WAVEFRONT
                       0  ADDITIONAL RESIDUAL EVALUATIONS FOR LINE SEARCHES
                       0  ADDITIONAL OPERATOR EVALUATIONS FOR LINE SEARCHES
                       0  WARNING MESSAGES DURING USER INPUT PROCESSING
                       0  WARNING MESSAGES DURING ANALYSIS
                       0  ANALYSIS WARNINGS ARE NUMERICAL PROBLEM MESSAGES
                       0  ANALYSIS WARNINGS ARE NEGATIVE EIGENVALUE MESSAGES
                       0  ERROR MESSAGES



     JOB TIME SUMMARY
       USER TIME (SEC)      =     0.20    
       SYSTEM TIME (SEC)    =     0.10    
       TOTAL CPU TIME (SEC) =     0.30    
       WALLCLOCK TIME (SEC) =            0
       MEMORY PEAK (GB)     =            0
