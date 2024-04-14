C ======================================================================
C Function to compute the generalized (gamma) DSGZ yield stress
C ======================================================================
      function sigmaY(
C       variables
     1  eqep, doteqep, temp, if_tc,
C       parameters of the constitutive law
     2  paraK, paragamma,
     3  paraC1, paraC2, paraC3, paraC4,
     4  paraa, paraalpha, param)
      include 'vaba_param.inc'
C     <1>
      funcf = (exp(-paraC1*eqep)+eqep**paraC2)*
     1        (1-exp(-paraalpha*eqep))
C     <2>
      funch = (doteqep**param)*exp(paraa/temp)
C     <3>
      funcq = (eqep*exp(1-eqep/(paraC3*funch)))/(paraC3*funch)
      funcr = exp((log(funch)-paraC4)*eqep)
C     <4> return the yield stress
      if (if_tc .eq. int(1)) then
        sigmaY = paraK/(1+paragamma/3)*
     1           (funcf+(funcq-funcf)*funcr)*funch
      else if (if_tc .eq. int(-1)) then
        sigmaY = paraK/(1-paragamma/3)*
     1           (funcf+(funcq-funcf)*funcr)*funch
      else if (if_tc .eq. int(0)) then
        sigmaY = paraK*
     1           (funcf+(funcq-funcf)*funcr)*funch
      end if
      return
      end
C ======================================================================
C Function to calculate the direvative of yield stress w.r.t.
C equivalent plastic strain; in an analytical way
C ======================================================================
      function sigmaYeqepANA(
C       variables
     1  eqep, doteqep, temp, if_tc,
C       parameters of the constitutive law
     2  paraK, paragamma,
     3  paraC1, paraC2, paraC3, paraC4,
     4  paraa, paraalpha, param)
      include 'vaba_param.inc'
      funcf = (exp(-paraC1*eqep)+eqep**paraC2)*
     1        (1-exp(-paraalpha*eqep))
      funch = (doteqep**param)*exp(paraa/temp)
      funcq = (eqep*exp(1-eqep/(paraC3*funch)))/(paraC3*funch)
      funcr = exp((log(funch)-paraC4)*eqep)
C
      pdfuncf = (-paraC1*exp(-paraC1*eqep)+paraC2*eqep**(paraC2-1))*
     1          (1-exp(-paraalpha*eqep))+
     2          (exp(-paraC1*eqep)+eqep**paraC2)*
     3          paraalpha*exp(-paraalpha*eqep)
C     return the yield stress w.r.t. eqep
      !if (eqep .gt. 0.0) then
        if (if_tc .eq. int(1)) then
          sigmaYeqepANA = paraK/(1+paragamma/3)*
     1                    (pdfuncf+
     2                     (funcq/eqep-funcq/(paraC3*funch)-pdfuncf)*
     3                     funcr+
     4                     (funcq-funcf)*log(funcr)/eqep*funcr)*
     5                    funch
        else if (if_tc .eq. int(-1)) then
          sigmaYeqepANA = paraK/(1-paragamma/3)*
     1                    (pdfuncf+
     2                     (funcq/eqep-funcq/(paraC3*funch)-pdfuncf)*
     3                     funcr+
     4                     (funcq-funcf)*log(funcr)/eqep*funcr)*
     5                    funch
        else if (if_tc .eq. int(0)) then
          sigmaYeqepANA = paraK*
     1                    (pdfuncf+
     2                     (funcq/eqep-funcq/(paraC3*funch)-pdfuncf)*
     3                     funcr+
     4                     (funcq-funcf)*log(funcr)/eqep*funcr)*
     5                    funch
        end if
      !else
        !sigmaYeqep = 0.0
      !end if
      return
      end
C ======================================================================
C Function to calculate the direvative of yield stress w.r.t.
C equivalent plastic strain rate; in an analytical way
C ======================================================================
      function sigmaYdoteqepANA(
C       variables
     1  eqep, doteqep, temp, if_tc,
C       parameters of the constitutive law
     2  paraK, paragamma,
     3  paraC1, paraC2, paraC3, paraC4,
     4  paraa, paraalpha, param)
      include 'vaba_param.inc'
      funcf = (exp(-paraC1*eqep)+eqep**paraC2)*
     1        (1-exp(-paraalpha*eqep))
      funch = (doteqep**param)*exp(paraa/temp)
      funcq = (eqep*exp(1-eqep/(paraC3*funch)))/(paraC3*funch)
      funcr = exp((log(funch)-paraC4)*eqep)
      if (if_tc .eq. int(1)) then
        sigY = paraK/(1+paragamma/3)*
     1         (funcf+(funcq-funcf)*funcr)*funch
      else if (if_tc .eq. int(-1)) then
        sigY = paraK/(1-paragamma/3)*
     1         (funcf+(funcq-funcf)*funcr)*funch
      else if (if_tc .eq. int(0)) then
        sigY = paraK*
     1         (funcf+(funcq-funcf)*funcr)*funch
      end if
C     return the yield stress w.r.t. doteqep
      !if (doteqep .gt. 0.0) then
        if (if_tc .eq. int(1)) then
          sigmaYdoteqepANA = paraK/(1+paragamma/3)*param/doteqep*(
     1                       funcq*(eqep/(paraC3*funch)-1+eqep)-
     2                       funcf*eqep)*funcr*funch+
     3                       param/doteqep*sigY
        else if (if_tc .eq. int(-1)) then
          sigmaYdoteqepANA = paraK/(1-paragamma/3)*param/doteqep*(
     1                       funcq*(eqep/(paraC3*funch)-1+eqep)-
     2                       funcf*eqep)*funcr*funch+
     3                       param/doteqep*sigY
        else if (if_tc .eq. int(0)) then
          sigmaYdoteqepANA = paraK*param/doteqep*(
     1                       funcq*(eqep/(paraC3*funch)-1+eqep)-
     2                       funcf*eqep)*funcr*funch+
     3                       param/doteqep*sigY
        end if
      !else
        !sigmaYdoteqepANA = 0.0
      !end if
      return
      end
C ======================================================================
C Function to calculate the direvative of yield stress w.r.t.
C absolute temperature; in an analytical way
C ======================================================================
      function sigmaYtempANA(
C       variables
     1  eqep, doteqep, temp, if_tc,
C       parameters of the constitutive law
     2  paraK, paragamma,
     3  paraC1, paraC2, paraC3, paraC4,
     4  paraa, paraalpha, param)
      include 'vaba_param.inc'
      funcf = (exp(-paraC1*eqep)+eqep**paraC2)*
     1        (1-exp(-paraalpha*eqep))
      funch = (doteqep**param)*exp(paraa/temp)
      funcq = (eqep*exp(1-eqep/(paraC3*funch)))/(paraC3*funch)
      funcr = exp((log(funch)-paraC4)*eqep)
      if (if_tc .eq. int(1)) then
        sigY = paraK/(1+paragamma/3)*
     1         (funcf+(funcq-funcf)*funcr)*funch
      else if (if_tc .eq. int(-1)) then
        sigY = paraK/(1-paragamma/3)*
     1         (funcf+(funcq-funcf)*funcr)*funch
      else if (if_tc .eq. int(0)) then
        sigY = paraK*
     1         (funcf+(funcq-funcf)*funcr)*funch
      end if
C     return the yield stress w.r.t. temp
      if (if_tc .eq. int(1)) then
        sigmaYtempANA = paraK/(1+paragamma/3)*(-paraa/temp**2)*(
     1                  funcq*(eqep/(paraC3*funch)-1+eqep)-
     2                  funcf*eqep)*funcr*funch+
     3                  (-paraa/temp**2)*sigY
      else if (if_tc .eq. int(-1)) then
        sigmaYtempANA = paraK/(1-paragamma/3)*(-paraa/temp**2)*(
     1                  funcq*(eqep/(paraC3*funch)-1+eqep)-
     2                  funcf*eqep)*funcr*funch+
     3                  (-paraa/temp**2)*sigY
      else if (if_tc .eq. int(0)) then
        sigmaYtempANA = paraK*(-paraa/temp**2)*(
     1                  funcq*(eqep/(paraC3*funch)-1+eqep)-
     2                  funcf*eqep)*funcr*funch+
     3                  (-paraa/temp**2)*sigY
      end if
      return
      end
C ======================================================================
C Function to estimate the direvative of yield stress w.r.t.
C equivalent plastic strain; in a numerical way
C ======================================================================
      function sigmaYeqepNUM(
C       variables
     1  sigy, eqep, doteqep, temp, if_tc,
C       parameters of the constitutive law
     2  paraK, paragamma,
     3  paraC1, paraC2, paraC3, paraC4,
     4  paraa, paraalpha, param)
      include 'vaba_param.inc'
C     <1> forward equivalent plastic strain with increment
      Deltaeqep = 1.0e-01
      if (j_sys_Dimension .eq. 2) Deltaeqep = 1.0e-08
      if (j_sys_Dimension .eq. 3) Deltaeqep = 1.0e-08
      eqepForward = eqep+Deltaeqep
C     <2> calculate the forward yield stress
      sigyForward = sigmaY(eqepForward, doteqep, temp, if_tc,
     1                     paraK, paragamma,
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
     1  sigy, eqep, doteqep, temp, if_tc,
C       parameters of the constitutive law
     2  paraK, paragamma,
     3  paraC1, paraC2, paraC3, paraC4,
     4  paraa, paraalpha, param)
      include 'vaba_param.inc'
C     <1> forward equivalent plastic strain rate with increment
      Deltadoteqep = 1.0e-01
      if (j_sys_Dimension .eq. 2) Deltadoteqep = 1.0e-08
      if (j_sys_Dimension .eq. 3) Deltadoteqep = 1.0e-08
      doteqepForward = doteqep+Deltadoteqep
C     <2> calculate the forward yield stress
      sigyForward = sigmaY(eqep, doteqepForward, temp, if_tc,
     1                     paraK, paragamma,
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
     1  sigy, eqep, doteqep, temp, if_tc,
C       parameters of the constitutive law
     2  paraK, paragamma,
     3  paraC1, paraC2, paraC3, paraC4,
     4  paraa, paraalpha, param)
      include 'vaba_param.inc'
C     <1> forward temperature with increment
      Deltatemp = 1.0e-01
      if (j_sys_Dimension .eq. 2) Deltatemp = 1.0e-08
      if (j_sys_Dimension .eq. 3) Deltatemp = 1.0e-08
      tempForward = temp+Deltatemp
C     <2> calculate the forward yield stress
      sigyForward = sigmaY(eqep, doteqep, tempForward, if_tc,
     1                     paraK, paragamma,
     2                     paraC1, paraC2, paraC3, paraC4,
     3                     paraa, paraalpha, param)
C     <3> return the yield stress w.r.t. Deltatemp
      sigmaYtempNUM = (sigyForward-sigy)/Deltatemp
      return
      end
