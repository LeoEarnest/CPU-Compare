# CPU-Compare
A program that can compare CPUs' multiple cores performance
This program can calculate the theory performance of Intel 7th Core CPU.
Based on a simplify fact that the performace of Intel CPUs are nearly unchange after Hasewell.
So the performance of them can be simplify as the following formular:
                Performance=Core number X Hyperthread coeffcient X max frequency of all cores X Architecture Coefficient.(if CPU supports Hyperthread technology,the coefficient is 1.25,otherwise it is 1,for Architecture Coefficient,Lake series=1.1 ; Well series=1)
# Support
Now only support two CPU to compare.
Support Intel CPU from 6th,7th,8th,9th core CPU.
