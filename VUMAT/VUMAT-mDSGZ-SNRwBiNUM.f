C ======================================================================
C Abaqus/Explicit Vectorized User Material Subroutine (VUMAT).
C For: "modified (C0) DSGZ" model.
C All rights of reproduction or distribution in any form are reserved.
C By Huadian Zhang @ OleMiss.
C
C Reference: Dr. Pantalé @ Toulouse University (github.com/pantale)
C
C J2 Mises Plasticity with modified DSGZ for
C 2D plane strain, 2D axisymmetric, and 3D cases.
C
C Elastic predictor, radial corrector algorithm.
C
C *Use numerical solution by adding a small increment.
C *Safe version of Newton-Raphson (Bisection embedded).
C
C The state variables are stored as:
C      STATE(*,1) = equivalent plastic strain
C      STATE(*,2) = equivalent plastic strain rate
C      STATE(*,3) = last value of Gamma
C      STATE(*,4) = yield stress of the material
C      STATE(*,5) = temperature due to plastic strain without conduction
C      STATE(*,6) = total number of Newton-Raphson iterations
C      STATE(*,7) = total number of bissection operations
C ======================================================================
C
C ======================================================================
C Function to compute the modified (C0) DSGZ yield stress
C ======================================================================
      function sigmaY(
C       variables
     1  eqep, doteqep, temp,
C       parameters of the constitutive law
     2  paraK, paraC0,
     3  paraC1, paraC2, paraC3, paraC4,
     4  paraa, paraalpha, param)
      include 'vaba_param.inc'
C     <1>
      funcf = (exp(paraC0*eqep)+eqep**paraC1-paraC2)*
     1        (1-exp(-paraalpha*eqep))
C     <2>
      funch = (doteqep**param)*exp(paraa/temp)
C     <3>
      funcq = (eqep*exp(1-eqep/(paraC2*funch)))/(paraC3*funch)
      funcr = exp((log(funch)-paraC4)*eqep)
C     <4> return the yield stress
      sigmaY = paraK*(funcf+(funcq-funcf)*funcr)*funch
      return
      end
C ======================================================================
C Function to estimate the direvative of yield stress w.r.t.
C equivalent plastic strain; in a numerical way
C ======================================================================
      function sigmaYeqepNUM(
C       variables
     1  sigy, eqep, doteqep, temp,
C       parameters of the constitutive law
     2  paraK, paraC0,
     3  paraC1, paraC2, paraC3, paraC4,
     4  paraa, paraalpha, param)
      include 'vaba_param.inc'
C     <1> forward equivalent plastic strain with increment
      Deltaeqep = 1.0e-01
      if (j_sys_Dimension .eq. 2) Deltaeqep = 1.0e-08
      if (j_sys_Dimension .eq. 3) Deltaeqep = 1.0e-08
      eqepForward = eqep+Deltaeqep
C     <2> calculate the forward yield stress
      sigyForward = sigmaY(eqepForward, doteqep, temp,
     1                     paraK, paraC0,
     2                     paraC1, paraC2, paraC3, paraC4,
     3                     paraa, paraalpha, param)
C     <3> return the yield stress w.r.t. Deltaeqep
      sigmaYeqepNUM = (sigyForward-sigy)/Deltaeqep
      return
      end
C ======================================================================
C Function to estimate the direvative of yield stress w.r.t.
C equivalent plastic strain rate; in a numerical way
C ======================================================================
      function sigmaYdoteqepNUM(
C       variables
     1  sigy, eqep, doteqep, temp,
C       parameters of the constitutive law
     2  paraK, paraC0,
     3  paraC1, paraC2, paraC3, paraC4,
     4  paraa, paraalpha, param)
      include 'vaba_param.inc'
C     <1> forward equivalent plastic strain rate with increment
      Deltadoteqep = 1.0e-01
      if (j_sys_Dimension .eq. 2) Deltadoteqep = 1.0e-08
      if (j_sys_Dimension .eq. 3) Deltadoteqep = 1.0e-08
      doteqepForward = doteqep+Deltadoteqep
C     <2> calculate the forward yield stress
      sigyForward = sigmaY(eqep, doteqepForward, temp,
     1                     paraK, paraC0,
     2                     paraC1, paraC2, paraC3, paraC4,
     3                     paraa, paraalpha, param)
C     <3> return the yield stress w.r.t. Deltadoteqep
      sigmaYdoteqepNUM = (sigyForward-sigy)/Deltadoteqep
      return
      end
C ======================================================================
C Function to estimate the direvative of yield stress w.r.t.
C absolute temperature; in a numerical way
C ======================================================================
      function sigmaYtempNUM(
C       variables
     1  sigy, eqep, doteqep, temp,
C       parameters of the constitutive law
     2  paraK, paraC0,
     3  paraC1, paraC2, paraC3, paraC4,
     4  paraa, paraalpha, param)
      include 'vaba_param.inc'
C     <1> forward temperature with increment
      Deltatemp = 1.0e-01
      if (j_sys_Dimension .eq. 2) Deltatemp = 1.0e-08
      if (j_sys_Dimension .eq. 3) Deltatemp = 1.0e-08
      tempForward = temp+Deltatemp
C     <2> calculate the forward yield stress
      sigyForward = sigmaY(eqep, doteqep, tempForward,
     1                     paraK, paraC0,
     2                     paraC1, paraC2, paraC3, paraC4,
     3                     paraa, paraalpha, param)
C     <3> return the yield stress w.r.t. Deltatemp
      sigmaYtempNUM = (sigyForward-sigy)/Deltatemp
      return
      end
C
C ======================================================================
C
      subroutine vumat(
C Read only (unmodifiable) variables -
     1  nblock, ndir, nshr, nstatev, nfieldv, nprops, jInfoArray,
     2  stepTime, totalTime, dtArray, cmname, coordMp, charLength,
     3  props, density, strainInc, relSpinInc,
     4  tempOld, stretchOld, defgradOld, fieldOld,
     5  stressOld, stateOld, enerInternOld, enerInelasOld,
     6  tempNew, stretchNew, defgradNew, fieldNew,
C Write only (modifiable) variables -
     7  stressNew, stateNew, enerInternNew, enerInelasNew)
C
      include 'vaba_param.inc'
C
C All arrays dimensioned by (*) are not used in this algorithm
      dimension props(nprops), density(nblock),
     1  coordMp(nblock,*), charLength(nblock), dtArray(*),
     2  strainInc(nblock,ndir+nshr), relSpinInc(nblock,nshr),
     3  tempOld(nblock), stretchOld(nblock,ndir+nshr),
     4  defgradOld(nblock,ndir+2*nshr), fieldOld(nblock,nfieldv),
     5  stressOld(nblock,ndir+nshr), stateOld(nblock,nstatev),
     6  enerInternOld(nblock), enerInelasOld(nblock),
     7  tempNew(nblock), stretchNew(nblock,ndir+nshr),
     8  defgradNew(nblock,ndir+2*nshr), fieldNew(nblock,nfieldv),
     9  stressNew(nblock,ndir+nshr), stateNew(nblock,nstatev),
     1  enerInternNew(nblock), enerInelasNew(nblock),
     2  jInfoArray(*)
C
      parameter(
     *  i_info_AnnealFlag = 1,
     *  i_info_Intpt = 2, ! Integration station number
     *  i_info_layer = 3, ! Layer number
     *  i_info_kspt = 4, ! Section point number in current layer
     *  i_info_effModDefn = 5, ! =1 if propK/ShearMod need to be defined
     *  i_info_ElemNumStartLoc = 6) ! Start loc of user element number
C
      parameter(
     1  itMax = 10000,
     2  TolSP = 1.0e-8,
     3  TolDP = 1.0e-12,
     4  neednprops = 15,
     5  neednstatev = 7,
     6  GammaInit = 1.0e-8, ! eqepInit???
     7  sqrt23 = 0.81649658092772603273242802490196,
     8  sqrt32 = 1.22474487139158904909864203735294)
C
      character*80 cmname
C
      lanneal = jInfoArray(i_info_AnnealFlag)
      dt = dtArray(1)
C
C ======================================================================
C
      propE        = props(1)
      propnu       = props(2)
      paraK        = props(3)
      paraC0       = props(4)
      paraC1       = props(5)
      paraC2       = props(6)
      paraC3       = props(7)
      paraC4       = props(8)
      paraa        = props(9)
      paraalpha    = props(10)
      param        = props(11)
      propTaylorQ  = props(12)
      proprho0     = props(13)
      propCp       = props(14)
      mCoupled     = props(15)
C
      propG2 = propE/(1.0+propnu)
      proplambda = propnu*propG2/(1.0-2.0*propnu)
      propK = propE/(3.0*(1.0-2.0*propnu))
      heatFr = propTaylorQ/(proprho0*propCp)
C
C     Newton-Raphson tolerance for solver: explicit or explicit_dp
      TolNR = TolSP
      if (j_sys_Dimension .eq. 2) TolNR = TolDP
      if (j_sys_Dimension .eq. 3) TolNR = TolDP
C
C     initial increment;
C     only compute the elastic portion;
C     only for the Abaqus internal use
      if (stepTime .eq. 0.0) then
C       check number of material properties
        if (nprops .ne. neednprops) then
          write(*,*) "ERROR:"
          write(*,*) "VUMAT needs ", neednprops," material propreties."
          write(*,*) "While ", nprops," are declared in the .inp file."
          call EXIT(-1)
        end if
C       check number of state variables
        if (nstatev .ne. neednstatev) then
          write(*,*) "VUMAT needs ", neednstatev," state variables"
          write(*,*) "While ", nstatev," are declared in the .inp file."
          call EXIT(-1)
        end if
C       print proprerties & parameters for debug purpose
        write(*,*) "Material properties and DSGZ parameters"
        write(*,*) "  Elastic properties:"
        write(*,*) "    E        = ", propE
        write(*,*) "    nu       = ", propnu
        write(*,*) "  DSGZ parameters:"
        write(*,*) "    K        = ", paraK
        write(*,*) "    C0       = ", paraC0
        write(*,*) "    C1       = ", paraC1
        write(*,*) "    C2       = ", paraC2
        write(*,*) "    C3       = ", paraC3
        write(*,*) "    C4       = ", paraC4
        write(*,*) "    a        = ", paraa
        write(*,*) "    alpha    = ", paraalpha
        write(*,*) "    m        = ", param
        write(*,*) "  Other properties:"
        write(*,*) "    TQ       = ", propTaylorQ
        write(*,*) "    rho0     = ", proprho0
        write(*,*) "    propCp   = ", propCp
        write(*,*) "    mcoupled = ", mCoupled
        write(*,*) "  Solution-dependent state variables:"
        write(*,*) "    SDV1:      ", stateOld(1,1)
        write(*,*) "    SDV2:      ", stateOld(1,2)
        write(*,*) "    SDV3:      ", stateOld(1,3)
        write(*,*) "    SDV4:      ", stateOld(1,4)
        write(*,*) "    SDV5:      ", stateOld(1,5)
        write(*,*) "    SDV6:      ", stateOld(1,6)
        write(*,*) "    SDV7:      ", stateOld(1,7)
        write(*,*) "  General parameters:"
        write(*,*) "    TolNR:     ", TolNR
        write(*,*) "  e(TolNR):     ", epsilon(TolNR)
C       check Newton-Raphson tolerance
        if (TolNR .lt. epsilon(TolNR)) then
          write(*,*) "Newton-Raphson tolerance is smaller than machine."
          write(*,*) "Please change tolerance definition in parameters."
          write(*,*) "VUMAT aborted."
          call EXIT(-1)
        end if
C
        do 100 k = 1, nblock
C         trace of the equivalent plastic strain increment tensor; init
          trDeltaeqep0 = strainInc(k,1)+strainInc(k,2)+strainInc(k,3)
C         new stress tensor subjected to elastic behavior
          stressNew(k,1) = stressOld(k,1)+
     1                     propG2*strainInc(k,1)+
     2                     proplambda*trDeltaeqep0
          stressNew(k,2) = stressOld(k,2)+
     1                     propG2*strainInc(k,2)+
     2                     proplambda*trDeltaeqep0
          stressNew(k,3) = stressOld(k,3)+
     1                     propG2*strainInc(k,3)+
     2                     proplambda*trDeltaeqep0
          stressNew(k,4) = stressOld(k,4)+
     1                     propG2*strainInc(k,4)
          if (nshr .gt. 1) then
            stressNew(k,5) = stressOld(k,5)+
     1                       propG2*strainInc(k,5)
            stressNew(k,6) = stressOld(k,6)+
     1                       propG2*strainInc(k,6)
          end if
  100   continue
C
C     regular increment;
C     radial return algorithm
      else
C
        do 101 k = 1, nblock
C         trace of the equivalent plastic strain increment tensor
          trDeltaeqep = strainInc(k,1)+strainInc(k,2)+strainInc(k,3)
C         current pressure and deviatoric stress tensor
          p0 = (stressOld(k,1)+stressOld(k,2)+stressOld(k,3))/3.0
          s11 = stressOld(k,1)-p0
          s22 = stressOld(k,2)-p0
          s33 = stressOld(k,3)-p0
          s12 = stressOld(k,4)
          if (nshr .gt. 1) then
            s23 = stressOld(k,5)
            s31 = stressOld(k,6)
          end if
C         current stress norm
          if (nshr .eq. 1) then
            Snorm0 = sqrt(s11*s11+s22*s22+s33*s33+
     1               2.0*s12*s12)
          else
            Snorm0 = sqrt(s11*s11+s22*s22+s33*s33+
     1               2.0*(s12*s12+s23*s23+s31*s31))
          end if
C         new pressure and deviatoric stress tensor
          p1 = p0+propK*trDeltaeqep
          s11 = s11+propG2*(strainInc(k,1)-trDeltaeqep/3.0)
          s22 = s22+propG2*(strainInc(k,2)-trDeltaeqep/3.0)
          s33 = s33+propG2*(strainInc(k,3)-trDeltaeqep/3.0)
          s12 = s12+propG2*strainInc(k,4)
          if (nshr .gt. 1) then
            s23 = s23+propG2*strainInc(k,5)
            s31 = s31+propG2*strainInc(k,6)
          end if
C         new stress norm
          if (nshr .eq. 1) then
            Snorm = sqrt(s11*s11+s22*s22+s33*s33+
     1              2.0*s12*s12)
          else
            Snorm = sqrt(s11*s11+s22*s22+s33*s33+
     1              2.0*(s12*s12+s23*s23+s31*s31))
          end if
C         trial von Mises/J2 equivalent stress
          Strial = sqrt32*Snorm
C         ==========plastic flow==========
C         current temperature at the beginning of the increment
          if (mCoupled .eq. 0) then
            tempInit = stateOld(k,5)
            if (stateOld(k,1) .eq. 0.0 .or. stateOld(k,2) .eq. 0.0) then
              tempInit = tempOld(k)
            end if
          else
            tempInit = tempOld(k)
          end if
          temp = tempInit
C         transfer old plastic strain and its increment per "element"
          eqep = stateOld(k,1)
          doteqep = stateOld(k,2)
C         initialize Gamma value
          Gamma = 0.0
C         current yield stress
          yield = stateOld(k,4)
C         if the yield stress is zero, compute the first yield stress
C         using the default initial value of Gamma
          if (yield .eq. 0.0) then
            yield = sigmaY(GammaInit, GammaInit/dt, temp,
     1                     paraK, paraC0,
     2                     paraC1, paraC2, paraC3, paraC4,
     3                     paraa, paraalpha, param)
          end if
C
          iterate = 0
          iBissection = 0
C         ==========plastic corrector==========
          if (Strial .gt. yield) then
            GammaMin = 0.0
            GammaMax = Strial/(sqrt32*propG2)
            Gamma = stateOld(k,3)
C           at 1st plastic increment
            if (Gamma .eq. 0.0) Gamma = 0.5*GammaMax
C           default initial value of Gamma
            if (eqep .eq. 0.0) Gamma = sqrt32*GammaInit
C           update eqep, doteqep, and temp for the next loop
            eqep = stateOld(k,1)+sqrt23*Gamma
            doteqep = sqrt23*Gamma/dt
            temp = tempInit+0.5*Gamma*heatFr*(sqrt23*yield+Snorm0)
C           Newton-Raphson iteration loop
            indexNR = 1
            do while (indexNR .eq. 1)
              yield = sigmaY(eqep, doteqep, temp,
     1                       paraK, paraC0,
     2                       paraC1, paraC2, paraC3, paraC4,
     3                       paraa, paraalpha, param)
C             radial return equation for isotropic case
              funcGamma = Strial-sqrt32*propG2*Gamma-yield
C
              sigmaYeqep = sigmaYeqepNUM(
     1                     yield, eqep, doteqep, temp,
     2                     paraK, paraC0,
     3                     paraC1, paraC2, paraC3, paraC4,
     4                     paraa, paraalpha, param)
              sigmaYdoteqep = sigmaYdoteqepNUM(
     1                        yield, eqep, doteqep, temp,
     2                        paraK, paraC0,
     3                        paraC1, paraC2, paraC3, paraC4,
     4                        paraa, paraalpha, param)
              sigmaYtemp = sigmaYtempNUM(
     1                     yield, eqep, doteqep, temp,
     2                     paraK, paraC0,
     3                     paraC1, paraC2, paraC3, paraC4,
     4                     paraa, paraalpha, param)
C
              pdsigmaYsum = sigmaYeqep+
     1                      sigmaYdoteqep/dt+
     2                      heatFr*yield*sigmaYtemp
C
              dfuncGamma = -sqrt32*propG2-sqrt23*pdsigmaYsum
              DeltaGamma = -funcGamma/dfuncGamma
C             adjust the range for root searching
              if (funcGamma .lt. 0.0) then
                GammaMax = Gamma
              else
                GammaMin = Gamma
              endif
C             update Gamma
              Gamma = Gamma+DeltaGamma
C             do one bisection step if root is outside of the range
              if ((GammaMax-Gamma)*(Gamma-GammaMin) .lt. 0.0) then
                DeltaGamma = 0.5*(GammaMax-GammaMin)
                Gamma = GammaMin+DeltaGamma
                iBissection = iBissection+1
              end if
C             end of NR iteration if converged
              if (abs(DeltaGamma) .lt. tolNR) indexNR = 0
C             update eqep, doteqep, and temp for the next loop
              eqep = stateOld(k,1)+sqrt23*Gamma
              doteqep = sqrt23*Gamma/dt
              temp = tempInit+0.5*Gamma*heatFr*(sqrt23*yield+Snorm0)
C
              iterate = iterate + 1
C             stop if NR is not convergence
              if (iterate .gt. itMax) then
                write(*,*) "No convergence reached for Newton-Raphson"
                write(*,*) "after", iterate, "iterations."
                write(*,*) "Time", stepTime, dt
                write(*,*) "yield", yield
                write(*,*) "Precision", abs(funcGamma/yield)
                write(*,*) "Strial", Strial
                write(*,*) "Gamma0", stateOld(k,3)
                write(*,*) "Gamma", Gamma
                write(*,*) "Gamma M", GammaMin, GammaMax
                write(*,*) "DeltaGamma", DeltaGamma
                write(*,*) "eqep0", stateOld(k,1)+sqrt23*stateOld(k,3)
                write(*,*) "deqep0", sqrt23*stateOld(k,3)/dt
                write(*,*) "eqep", eqep
                write(*,*) "doteqep", doteqep
                write(*,*) "temp", temp
                write(*,*) "sigmaYeqep", sigmaYeqep
                write(*,*) "sigmaYdoteqep", sigmaYdoteqep
                write(*,*) "sigmaYtemp", sigmaYtemp
                write(*,*) "old sdv1", stateOld(k,1)
                write(*,*) "old sdv2", stateOld(k,2)
                write(*,*) "old sdv3", stateOld(k,3)
                write(*,*) "old sdv4", stateOld(k,4)
                write(*,*) "old sdv5", stateOld(k,5)
                write(*,*) "old sdv6", stateOld(k,6)
                write(*,*) "old sdv7", stateOld(k,7)
                call EXIT(-1)
              end if
            end do
C           new deviatoric stress tensor
            plcor = (1.0-propG2*Gamma/Snorm)
            s11 = s11*plcor
            s22 = s22*plcor
            s33 = s33*plcor
            s12 = s12*plcor
            if (nshr .gt. 1) then
              s23 = s23*plcor
              s31 = s31*plcor
            end if
          end if
C ======================================================================
C         store new SDVs
          stateNew(k,1) = eqep
          stateNew(k,2) = doteqep
          stateNew(k,3) = Gamma
          stateNew(k,4) = yield
          stateNew(k,6) = stateOld(k,6)+iterate
          stateNew(k,7) = stateOld(k,7)+iBissection
C         store new stress tensor
          stressNew(k,1) = s11+p1
          stressNew(k,2) = s22+p1
          stressNew(k,3) = s33+p1
          stressNew(k,4) = s12
          if (nshr .gt. 1) then
            stressNew(k,5) = s23
            stressNew(k,6) = s31
          end if
C         new strain energy
          if (nshr .eq. 1) then
            eIEInc = 0.5*(
     1               (stressOld(k,1)+stressNew(k,1))*strainInc(k,1)+
     2               (stressOld(k,2)+stressNew(k,2))*strainInc(k,2)+
     3               (stressOld(k,3)+stressNew(k,3))*strainInc(k,3)+
     4           2.0*(stressOld(k,4)+stressNew(k,4))*strainInc(k,4))
          else
            eIEInc = 0.5*(
     1               (stressOld(k,1)+stressNew(k,1))*strainInc(k,1)+
     2               (stressOld(k,2)+stressNew(k,2))*strainInc(k,2)+
     3               (stressOld(k,3)+stressNew(k,3))*strainInc(k,3)+
     4           2.0*(stressOld(k,4)+stressNew(k,4))*strainInc(k,4)+
     5           2.0*(stressOld(k,5)+stressNew(k,5))*strainInc(k,5)+
     6           2.0*(stressOld(k,6)+stressNew(k,6))*strainInc(k,6))
          end if
C         store new specific internal energy
          enerInternNew(k) = enerInternOld(k)+eIEInc/density(k)
C         new dissipated inelastic energy
          if (Gamma .eq. 0.0) then
C           transfer old inelastic energy and temperature
            enerInelasNew(k) = enerInelasOld(k)
            stateNew(k,5) = tempInit
          else
            if (nshr .eq. 1) then
              plWorkInc = 0.5*Gamma*(
     1                    sqrt(s11*s11+s22*s22+s33*s33+
     2                    2.0*s12*s12)+
     3                    Snorm0)
            else
              plWorkInc = 0.5*Gamma*(
     1                    sqrt(s11*s11+s22*s22+s33*s33+
     2                    2.0*(s12*s12+s23*s23+s31*s31))+
     3                    Snorm0)
            end if
C           store new inelastic specific energy and temperature
            enerInelasNew(k) = enerInelasOld(k)+plWorkInc/density(k)
            stateNew(k,5) = tempInit+heatFr*plWorkInc
          end if
  101   continue
      end if
      return
      end
