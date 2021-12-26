# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 10.4.1 for Linux x86 (64-bit) (April 11, 2016)
# Date: Mon 3 Feb 2020 13:54:28


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = '(5*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_6 = Coupling(name = 'GC_6',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_7 = Coupling(name = 'GC_7',
                value = '-G',
                order = {'QCD':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'complex(0,1)*G',
                order = {'QCD':1})

GC_9 = Coupling(name = 'GC_9',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_11 = Coupling(name = 'GC_11',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_12 = Coupling(name = 'GC_12',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '(cw*ee*complex(0,1))/sw',
                 order = {'QED':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '(-2*cw*ee**2*complex(0,1))/sw',
                 order = {'QED':2})

GC_15 = Coupling(name = 'GC_15',
                 value = '(ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_16 = Coupling(name = 'GC_16',
                 value = '(-2*ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '(ee*complex(0,1)*sw)/cw',
                 order = {'QED':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '-(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_19 = Coupling(name = 'GC_19',
                 value = '(cw*ee*complex(0,1))/(2.*sw) - (ee*complex(0,1)*sw)/(6.*cw)',
                 order = {'QED':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '-(ee*complex(0,1))/(2.*cw*sw) + (ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '-(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                 order = {'QED':1})

GC_23 = Coupling(name = 'GC_23',
                 value = '(ee*complex(0,1))/(2.*cw*sw) - (5*ee*complex(0,1)*sw)/(3.*cw)',
                 order = {'QED':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '(ee*complex(0,1)*UTL1x2)/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL1x3)/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UTL1x2*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL1x3*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '(ee*complex(0,1)*UTL2x2)/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL2x3)/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UTL2x2*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL2x3*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '(ee*complex(0,1)*UTL3x2)/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL3x3)/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UTL3x2*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL3x3*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '(ee*complex(0,1)*UTL4x2)/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL4x3)/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UTL4x2*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL4x3*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '(ee*complex(0,1)*UTR1x2)/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTR1x3)/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UTR1x2*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTR1x3*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '(ee*complex(0,1)*UTR2x2)/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTR2x3)/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UTR2x2*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTR2x3*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '(ee*complex(0,1)*UTR3x2)/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTR3x3)/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UTR3x2*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTR3x3*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '(ee*complex(0,1)*UTR4x2)/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTR4x3)/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UTR4x2*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTR4x3*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '(ee**2*complex(0,1)*vev*cmath.sqrt(1 - xi))/(2.*cw**2) + (ee**2*complex(0,1)*vev*cmath.sqrt(1 - xi))/(2.*sw**2)',
                 order = {'QED':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '(ee**2*complex(0,1)*vev*cmath.sqrt(1 - xi))/(2.*sw**2)',
                 order = {'QED':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '(ee**2*complex(0,1))/(2.*sw**2) - (ee**2*complex(0,1)*xi)/sw**2',
                 order = {'QED':2})

GC_35 = Coupling(name = 'GC_35',
                 value = '(ee**2*complex(0,1))/(2.*cw**2) + (ee**2*complex(0,1))/(2.*sw**2) - (ee**2*complex(0,1)*xi)/cw**2 - (ee**2*complex(0,1)*xi)/sw**2',
                 order = {'QED':2})

GC_36 = Coupling(name = 'GC_36',
                 value = '(-3*complex(0,1)*MH**2)/(vev*cmath.sqrt(1 - xi)) + (6*complex(0,1)*MH**2*xi)/(vev*cmath.sqrt(1 - xi))',
                 order = {'QED':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '(3*complex(0,1)*MH**2)/(vev**2*(-1 + xi)) - (28*complex(0,1)*MH**2*xi)/(vev**2*(-1 + xi)) + (28*complex(0,1)*MH**2*xi**2)/(vev**2*(-1 + xi))',
                 order = {'QED':2})

GC_38 = Coupling(name = 'GC_38',
                 value = '-((complex(0,1)*ye)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '-((complex(0,1)*ym)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '(mbLS/mbHS)*(-((complex(0,1)*ymb*cmath.sqrt(1 - xi))/vev))',
                 order = {'QED':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                 order = {'QED':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '-(ee*complex(0,1)*UBL2x1*complexconjugate(UBL1x1))/(2.*cw*sw) + (ee*complex(0,1)*sw*UBL2x1*complexconjugate(UBL1x1))/(3.*cw) - (ee*complex(0,1)*UBL2x2*complexconjugate(UBL1x2))/(2.*cw*sw) + (ee*complex(0,1)*sw*UBL2x2*complexconjugate(UBL1x2))/(3.*cw)',
                 order = {'QED':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '(ee*complex(0,1)*UTL1x1*complexconjugate(UBL1x1))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL1x2*complexconjugate(UBL1x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL1x3*complexconjugate(UBL1x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL1x2*complexconjugate(UBL1x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UTL1x3*complexconjugate(UBL1x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '(ee*complex(0,1)*UTL2x1*complexconjugate(UBL1x1))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL2x2*complexconjugate(UBL1x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL2x3*complexconjugate(UBL1x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL2x2*complexconjugate(UBL1x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UTL2x3*complexconjugate(UBL1x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '(ee*complex(0,1)*UTL3x1*complexconjugate(UBL1x1))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL3x2*complexconjugate(UBL1x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL3x3*complexconjugate(UBL1x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL3x2*complexconjugate(UBL1x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UTL3x3*complexconjugate(UBL1x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '(ee*complex(0,1)*UTL4x1*complexconjugate(UBL1x1))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL4x2*complexconjugate(UBL1x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL4x3*complexconjugate(UBL1x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL4x2*complexconjugate(UBL1x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UTL4x3*complexconjugate(UBL1x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '-(ee*complex(0,1)*UBL1x1*complexconjugate(UBL2x1))/(2.*cw*sw) + (ee*complex(0,1)*sw*UBL1x1*complexconjugate(UBL2x1))/(3.*cw) - (ee*complex(0,1)*UBL1x2*complexconjugate(UBL2x2))/(2.*cw*sw) + (ee*complex(0,1)*sw*UBL1x2*complexconjugate(UBL2x2))/(3.*cw)',
                 order = {'QED':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '(ee*complex(0,1)*UTL1x1*complexconjugate(UBL2x1))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL1x2*complexconjugate(UBL2x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL1x3*complexconjugate(UBL2x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL1x2*complexconjugate(UBL2x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UTL1x3*complexconjugate(UBL2x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '(ee*complex(0,1)*UTL2x1*complexconjugate(UBL2x1))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL2x2*complexconjugate(UBL2x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL2x3*complexconjugate(UBL2x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL2x2*complexconjugate(UBL2x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UTL2x3*complexconjugate(UBL2x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_50 = Coupling(name = 'GC_50',
                 value = '(ee*complex(0,1)*UTL3x1*complexconjugate(UBL2x1))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL3x2*complexconjugate(UBL2x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL3x3*complexconjugate(UBL2x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL3x2*complexconjugate(UBL2x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UTL3x3*complexconjugate(UBL2x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '(ee*complex(0,1)*UTL4x1*complexconjugate(UBL2x1))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL4x2*complexconjugate(UBL2x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL4x3*complexconjugate(UBL2x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTL4x2*complexconjugate(UBL2x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UTL4x3*complexconjugate(UBL2x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '(ee*complex(0,1)*sw*UBR2x1*complexconjugate(UBR1x1))/(3.*cw) - (ee*complex(0,1)*UBR2x2*complexconjugate(UBR1x2))/(2.*cw*sw) + (ee*complex(0,1)*sw*UBR2x2*complexconjugate(UBR1x2))/(3.*cw)',
                 order = {'QED':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '(ee*complex(0,1)*UTR1x2*complexconjugate(UBR1x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTR1x3*complexconjugate(UBR1x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTR1x2*complexconjugate(UBR1x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UTR1x3*complexconjugate(UBR1x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '(ee*complex(0,1)*UTR2x2*complexconjugate(UBR1x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTR2x3*complexconjugate(UBR1x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTR2x2*complexconjugate(UBR1x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UTR2x3*complexconjugate(UBR1x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '(ee*complex(0,1)*UTR3x2*complexconjugate(UBR1x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTR3x3*complexconjugate(UBR1x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTR3x2*complexconjugate(UBR1x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UTR3x3*complexconjugate(UBR1x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '(ee*complex(0,1)*UTR4x2*complexconjugate(UBR1x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTR4x3*complexconjugate(UBR1x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTR4x2*complexconjugate(UBR1x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UTR4x3*complexconjugate(UBR1x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '(ee*complex(0,1)*sw*UBR1x1*complexconjugate(UBR2x1))/(3.*cw) - (ee*complex(0,1)*UBR1x2*complexconjugate(UBR2x2))/(2.*cw*sw) + (ee*complex(0,1)*sw*UBR1x2*complexconjugate(UBR2x2))/(3.*cw)',
                 order = {'QED':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '(ee*complex(0,1)*sw)/(3.*cw) - (ee*complex(0,1)*UBR2x2*complexconjugate(UBR2x2))/(2.*cw*sw)',
                 order = {'QED':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '-(ee*complex(0,1))/(2.*cw*sw) + (ee*complex(0,1)*sw)/(3.*cw) + (ee*complex(0,1)*UBR2x2*complexconjugate(UBR2x2))/(2.*cw*sw)',
                 order = {'QED':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '(ee*complex(0,1)*UTR1x2*complexconjugate(UBR2x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTR1x3*complexconjugate(UBR2x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTR1x2*complexconjugate(UBR2x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UTR1x3*complexconjugate(UBR2x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '(ee*complex(0,1)*UTR2x2*complexconjugate(UBR2x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTR2x3*complexconjugate(UBR2x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTR2x2*complexconjugate(UBR2x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UTR2x3*complexconjugate(UBR2x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '(ee*complex(0,1)*UTR3x2*complexconjugate(UBR2x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTR3x3*complexconjugate(UBR2x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTR3x2*complexconjugate(UBR2x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UTR3x3*complexconjugate(UBR2x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '(ee*complex(0,1)*UTR4x2*complexconjugate(UBR2x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTR4x3*complexconjugate(UBR2x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UTR4x2*complexconjugate(UBR2x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UTR4x3*complexconjugate(UBR2x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '(ee*complex(0,1)*complexconjugate(UTL1x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(UTL1x3))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(UTL1x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(UTL1x3)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '(ee*complex(0,1)*UBL1x1*complexconjugate(UTL1x1))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBL1x2*complexconjugate(UTL1x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBL1x2*complexconjugate(UTL1x3))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBL1x2*complexconjugate(UTL1x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UBL1x2*complexconjugate(UTL1x3)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '(ee*complex(0,1)*UBL2x1*complexconjugate(UTL1x1))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBL2x2*complexconjugate(UTL1x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBL2x2*complexconjugate(UTL1x3))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBL2x2*complexconjugate(UTL1x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UBL2x2*complexconjugate(UTL1x3)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '(ee*complex(0,1)*UTL2x1*complexconjugate(UTL1x1))/(2.*cw*sw) - (2*ee*complex(0,1)*sw*UTL2x1*complexconjugate(UTL1x1))/(3.*cw) - (2*ee*complex(0,1)*sw*UTL2x2*complexconjugate(UTL1x2))/(3.*cw) - (2*ee*complex(0,1)*sw*UTL2x3*complexconjugate(UTL1x3))/(3.*cw) - (2*ee*complex(0,1)*sw*UTL2x4*complexconjugate(UTL1x4))/(3.*cw) + (ee*complex(0,1)*UTL2x2*complexconjugate(UTL1x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTL2x3*complexconjugate(UTL1x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                 order = {'QED':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '(ee*complex(0,1)*UTL3x1*complexconjugate(UTL1x1))/(2.*cw*sw) - (2*ee*complex(0,1)*sw*UTL3x1*complexconjugate(UTL1x1))/(3.*cw) - (2*ee*complex(0,1)*sw*UTL3x2*complexconjugate(UTL1x2))/(3.*cw) - (2*ee*complex(0,1)*sw*UTL3x3*complexconjugate(UTL1x3))/(3.*cw) - (2*ee*complex(0,1)*sw*UTL3x4*complexconjugate(UTL1x4))/(3.*cw) + (ee*complex(0,1)*UTL3x2*complexconjugate(UTL1x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTL3x3*complexconjugate(UTL1x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                 order = {'QED':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '(ee*complex(0,1)*UTL4x1*complexconjugate(UTL1x1))/(2.*cw*sw) - (2*ee*complex(0,1)*sw*UTL4x1*complexconjugate(UTL1x1))/(3.*cw) - (2*ee*complex(0,1)*sw*UTL4x2*complexconjugate(UTL1x2))/(3.*cw) - (2*ee*complex(0,1)*sw*UTL4x3*complexconjugate(UTL1x3))/(3.*cw) - (2*ee*complex(0,1)*sw*UTL4x4*complexconjugate(UTL1x4))/(3.*cw) + (ee*complex(0,1)*UTL4x2*complexconjugate(UTL1x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTL4x3*complexconjugate(UTL1x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                 order = {'QED':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '(complex(0,1)*UTR1x2*yL4*complexconjugate(UTL1x1)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTR1x3*yL4*complexconjugate(UTL1x1)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTR1x1*yR1*complexconjugate(UTL1x4)*cmath.sqrt(1 - xi))/fs - (complex(0,1)*UTR1x4*yL1*complexconjugate(UTL1x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) + (complex(0,1)*UTR1x1*yR4*complexconjugate(UTL1x2)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTR1x1*yR4*complexconjugate(UTL1x3)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                 order = {'QED':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '(complex(0,1)*UTR2x2*yL4*complexconjugate(UTL1x1)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTR2x3*yL4*complexconjugate(UTL1x1)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTR2x1*yR1*complexconjugate(UTL1x4)*cmath.sqrt(1 - xi))/fs - (complex(0,1)*UTR2x4*yL1*complexconjugate(UTL1x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) + (complex(0,1)*UTR2x1*yR4*complexconjugate(UTL1x2)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTR2x1*yR4*complexconjugate(UTL1x3)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                 order = {'QED':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '(complex(0,1)*UTR3x2*yL4*complexconjugate(UTL1x1)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTR3x3*yL4*complexconjugate(UTL1x1)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTR3x1*yR1*complexconjugate(UTL1x4)*cmath.sqrt(1 - xi))/fs - (complex(0,1)*UTR3x4*yL1*complexconjugate(UTL1x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) + (complex(0,1)*UTR3x1*yR4*complexconjugate(UTL1x2)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTR3x1*yR4*complexconjugate(UTL1x3)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                 order = {'QED':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '(complex(0,1)*UTR4x2*yL4*complexconjugate(UTL1x1)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTR4x3*yL4*complexconjugate(UTL1x1)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTR4x1*yR1*complexconjugate(UTL1x4)*cmath.sqrt(1 - xi))/fs - (complex(0,1)*UTR4x4*yL1*complexconjugate(UTL1x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) + (complex(0,1)*UTR4x1*yR4*complexconjugate(UTL1x2)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTR4x1*yR4*complexconjugate(UTL1x3)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                 order = {'QED':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '(mtLS/mtHS)*((complex(0,1)*UTR1x4*yL1*complexconjugate(UTL1x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) - (complex(0,1)*UTR1x1*yR4*complexconjugate(UTL1x2)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR1x1*yR4*complexconjugate(UTL1x3)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR1x2*yL4*complexconjugate(UTL1x1)*cmath.sqrt(xi))/2. - (complex(0,1)*UTR1x3*yL4*complexconjugate(UTL1x1)*cmath.sqrt(xi))/2. + complex(0,1)*UTR1x1*yR1*complexconjugate(UTL1x4)*cmath.sqrt(xi))',
                 order = {'QED':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '(complex(0,1)*UTR2x4*yL1*complexconjugate(UTL1x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) - (complex(0,1)*UTR2x1*yR4*complexconjugate(UTL1x2)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR2x1*yR4*complexconjugate(UTL1x3)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR2x2*yL4*complexconjugate(UTL1x1)*cmath.sqrt(xi))/2. - (complex(0,1)*UTR2x3*yL4*complexconjugate(UTL1x1)*cmath.sqrt(xi))/2. + complex(0,1)*UTR2x1*yR1*complexconjugate(UTL1x4)*cmath.sqrt(xi)',
                 order = {'QED':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '(complex(0,1)*UTR3x4*yL1*complexconjugate(UTL1x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) - (complex(0,1)*UTR3x1*yR4*complexconjugate(UTL1x2)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR3x1*yR4*complexconjugate(UTL1x3)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR3x2*yL4*complexconjugate(UTL1x1)*cmath.sqrt(xi))/2. - (complex(0,1)*UTR3x3*yL4*complexconjugate(UTL1x1)*cmath.sqrt(xi))/2. + complex(0,1)*UTR3x1*yR1*complexconjugate(UTL1x4)*cmath.sqrt(xi)',
                 order = {'QED':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '(complex(0,1)*UTR4x4*yL1*complexconjugate(UTL1x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) - (complex(0,1)*UTR4x1*yR4*complexconjugate(UTL1x2)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR4x1*yR4*complexconjugate(UTL1x3)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR4x2*yL4*complexconjugate(UTL1x1)*cmath.sqrt(xi))/2. - (complex(0,1)*UTR4x3*yL4*complexconjugate(UTL1x1)*cmath.sqrt(xi))/2. + complex(0,1)*UTR4x1*yR1*complexconjugate(UTL1x4)*cmath.sqrt(xi)',
                 order = {'QED':1})

GC_78 = Coupling(name = 'GC_78',
                 value = '(ee*complex(0,1)*complexconjugate(UTL2x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(UTL2x3))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(UTL2x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(UTL2x3)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '(ee*complex(0,1)*UBL1x1*complexconjugate(UTL2x1))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBL1x2*complexconjugate(UTL2x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBL1x2*complexconjugate(UTL2x3))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBL1x2*complexconjugate(UTL2x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UBL1x2*complexconjugate(UTL2x3)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '(ee*complex(0,1)*UBL2x1*complexconjugate(UTL2x1))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBL2x2*complexconjugate(UTL2x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBL2x2*complexconjugate(UTL2x3))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBL2x2*complexconjugate(UTL2x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UBL2x2*complexconjugate(UTL2x3)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '(ee*complex(0,1)*UTL1x1*complexconjugate(UTL2x1))/(2.*cw*sw) - (2*ee*complex(0,1)*sw*UTL1x1*complexconjugate(UTL2x1))/(3.*cw) - (2*ee*complex(0,1)*sw*UTL1x2*complexconjugate(UTL2x2))/(3.*cw) - (2*ee*complex(0,1)*sw*UTL1x3*complexconjugate(UTL2x3))/(3.*cw) - (2*ee*complex(0,1)*sw*UTL1x4*complexconjugate(UTL2x4))/(3.*cw) + (ee*complex(0,1)*UTL1x2*complexconjugate(UTL2x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTL1x3*complexconjugate(UTL2x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                 order = {'QED':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '(ee*complex(0,1))/(2.*cw*sw) - (2*ee*complex(0,1)*sw)/(3.*cw) - (ee*complex(0,1)*UTL2x2*complexconjugate(UTL2x2))/(2.*cw*sw) - (ee*complex(0,1)*UTL2x3*complexconjugate(UTL2x3))/(2.*cw*sw) - (ee*complex(0,1)*UTL2x4*complexconjugate(UTL2x4))/(2.*cw*sw) + (ee*complex(0,1)*UTL2x2*complexconjugate(UTL2x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTL2x3*complexconjugate(UTL2x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                 order = {'QED':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '-(ee*complex(0,1)*UTL3x2*complexconjugate(UTL2x2))/(2.*cw*sw) - (ee*complex(0,1)*UTL3x3*complexconjugate(UTL2x3))/(2.*cw*sw) - (ee*complex(0,1)*UTL3x4*complexconjugate(UTL2x4))/(2.*cw*sw) + (ee*complex(0,1)*UTL3x2*complexconjugate(UTL2x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTL3x3*complexconjugate(UTL2x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                 order = {'QED':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '-(ee*complex(0,1)*UTL4x2*complexconjugate(UTL2x2))/(2.*cw*sw) - (ee*complex(0,1)*UTL4x3*complexconjugate(UTL2x3))/(2.*cw*sw) - (ee*complex(0,1)*UTL4x4*complexconjugate(UTL2x4))/(2.*cw*sw) + (ee*complex(0,1)*UTL4x2*complexconjugate(UTL2x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTL4x3*complexconjugate(UTL2x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                 order = {'QED':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '(complex(0,1)*UTR1x2*yL4*complexconjugate(UTL2x1)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTR1x3*yL4*complexconjugate(UTL2x1)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTR1x1*yR1*complexconjugate(UTL2x4)*cmath.sqrt(1 - xi))/fs - (complex(0,1)*UTR1x4*yL1*complexconjugate(UTL2x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) + (complex(0,1)*UTR1x1*yR4*complexconjugate(UTL2x2)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTR1x1*yR4*complexconjugate(UTL2x3)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                 order = {'QED':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '(complex(0,1)*UTR2x2*yL4*complexconjugate(UTL2x1)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTR2x3*yL4*complexconjugate(UTL2x1)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTR2x1*yR1*complexconjugate(UTL2x4)*cmath.sqrt(1 - xi))/fs - (complex(0,1)*UTR2x4*yL1*complexconjugate(UTL2x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) + (complex(0,1)*UTR2x1*yR4*complexconjugate(UTL2x2)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTR2x1*yR4*complexconjugate(UTL2x3)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                 order = {'QED':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '(complex(0,1)*UTR3x2*yL4*complexconjugate(UTL2x1)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTR3x3*yL4*complexconjugate(UTL2x1)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTR3x1*yR1*complexconjugate(UTL2x4)*cmath.sqrt(1 - xi))/fs - (complex(0,1)*UTR3x4*yL1*complexconjugate(UTL2x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) + (complex(0,1)*UTR3x1*yR4*complexconjugate(UTL2x2)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTR3x1*yR4*complexconjugate(UTL2x3)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                 order = {'QED':1})

GC_88 = Coupling(name = 'GC_88',
                 value = '(complex(0,1)*UTR4x2*yL4*complexconjugate(UTL2x1)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTR4x3*yL4*complexconjugate(UTL2x1)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTR4x1*yR1*complexconjugate(UTL2x4)*cmath.sqrt(1 - xi))/fs - (complex(0,1)*UTR4x4*yL1*complexconjugate(UTL2x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) + (complex(0,1)*UTR4x1*yR4*complexconjugate(UTL2x2)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTR4x1*yR4*complexconjugate(UTL2x3)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                 order = {'QED':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '(complex(0,1)*UTR1x4*yL1*complexconjugate(UTL2x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) - (complex(0,1)*UTR1x1*yR4*complexconjugate(UTL2x2)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR1x1*yR4*complexconjugate(UTL2x3)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR1x2*yL4*complexconjugate(UTL2x1)*cmath.sqrt(xi))/2. - (complex(0,1)*UTR1x3*yL4*complexconjugate(UTL2x1)*cmath.sqrt(xi))/2. + complex(0,1)*UTR1x1*yR1*complexconjugate(UTL2x4)*cmath.sqrt(xi)',
                 order = {'QED':1})

GC_90 = Coupling(name = 'GC_90',
                 value = '(complex(0,1)*UTR2x4*yL1*complexconjugate(UTL2x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) - (complex(0,1)*UTR2x1*yR4*complexconjugate(UTL2x2)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR2x1*yR4*complexconjugate(UTL2x3)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR2x2*yL4*complexconjugate(UTL2x1)*cmath.sqrt(xi))/2. - (complex(0,1)*UTR2x3*yL4*complexconjugate(UTL2x1)*cmath.sqrt(xi))/2. + complex(0,1)*UTR2x1*yR1*complexconjugate(UTL2x4)*cmath.sqrt(xi)',
                 order = {'QED':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '(complex(0,1)*UTR3x4*yL1*complexconjugate(UTL2x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) - (complex(0,1)*UTR3x1*yR4*complexconjugate(UTL2x2)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR3x1*yR4*complexconjugate(UTL2x3)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR3x2*yL4*complexconjugate(UTL2x1)*cmath.sqrt(xi))/2. - (complex(0,1)*UTR3x3*yL4*complexconjugate(UTL2x1)*cmath.sqrt(xi))/2. + complex(0,1)*UTR3x1*yR1*complexconjugate(UTL2x4)*cmath.sqrt(xi)',
                 order = {'QED':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '(complex(0,1)*UTR4x4*yL1*complexconjugate(UTL2x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) - (complex(0,1)*UTR4x1*yR4*complexconjugate(UTL2x2)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR4x1*yR4*complexconjugate(UTL2x3)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR4x2*yL4*complexconjugate(UTL2x1)*cmath.sqrt(xi))/2. - (complex(0,1)*UTR4x3*yL4*complexconjugate(UTL2x1)*cmath.sqrt(xi))/2. + complex(0,1)*UTR4x1*yR1*complexconjugate(UTL2x4)*cmath.sqrt(xi)',
                 order = {'QED':1})

GC_93 = Coupling(name = 'GC_93',
                 value = '(ee*complex(0,1)*complexconjugate(UTL3x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(UTL3x3))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(UTL3x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(UTL3x3)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_94 = Coupling(name = 'GC_94',
                 value = '(ee*complex(0,1)*UBL1x1*complexconjugate(UTL3x1))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBL1x2*complexconjugate(UTL3x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBL1x2*complexconjugate(UTL3x3))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBL1x2*complexconjugate(UTL3x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UBL1x2*complexconjugate(UTL3x3)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '(ee*complex(0,1)*UBL2x1*complexconjugate(UTL3x1))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBL2x2*complexconjugate(UTL3x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBL2x2*complexconjugate(UTL3x3))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBL2x2*complexconjugate(UTL3x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UBL2x2*complexconjugate(UTL3x3)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '(ee*complex(0,1)*UTL1x1*complexconjugate(UTL3x1))/(2.*cw*sw) - (2*ee*complex(0,1)*sw*UTL1x1*complexconjugate(UTL3x1))/(3.*cw) - (2*ee*complex(0,1)*sw*UTL1x2*complexconjugate(UTL3x2))/(3.*cw) - (2*ee*complex(0,1)*sw*UTL1x3*complexconjugate(UTL3x3))/(3.*cw) - (2*ee*complex(0,1)*sw*UTL1x4*complexconjugate(UTL3x4))/(3.*cw) + (ee*complex(0,1)*UTL1x2*complexconjugate(UTL3x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTL1x3*complexconjugate(UTL3x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                 order = {'QED':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '-(ee*complex(0,1)*UTL2x2*complexconjugate(UTL3x2))/(2.*cw*sw) - (ee*complex(0,1)*UTL2x3*complexconjugate(UTL3x3))/(2.*cw*sw) - (ee*complex(0,1)*UTL2x4*complexconjugate(UTL3x4))/(2.*cw*sw) + (ee*complex(0,1)*UTL2x2*complexconjugate(UTL3x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTL2x3*complexconjugate(UTL3x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                 order = {'QED':1})

GC_98 = Coupling(name = 'GC_98',
                 value = '(ee*complex(0,1))/(2.*cw*sw) - (2*ee*complex(0,1)*sw)/(3.*cw) - (ee*complex(0,1)*UTL3x2*complexconjugate(UTL3x2))/(2.*cw*sw) - (ee*complex(0,1)*UTL3x3*complexconjugate(UTL3x3))/(2.*cw*sw) - (ee*complex(0,1)*UTL3x4*complexconjugate(UTL3x4))/(2.*cw*sw) + (ee*complex(0,1)*UTL3x2*complexconjugate(UTL3x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTL3x3*complexconjugate(UTL3x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '-(ee*complex(0,1)*UTL4x2*complexconjugate(UTL3x2))/(2.*cw*sw) - (ee*complex(0,1)*UTL4x3*complexconjugate(UTL3x3))/(2.*cw*sw) - (ee*complex(0,1)*UTL4x4*complexconjugate(UTL3x4))/(2.*cw*sw) + (ee*complex(0,1)*UTL4x2*complexconjugate(UTL3x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTL4x3*complexconjugate(UTL3x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                 order = {'QED':1})

GC_100 = Coupling(name = 'GC_100',
                  value = '(complex(0,1)*UTR1x2*yL4*complexconjugate(UTL3x1)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTR1x3*yL4*complexconjugate(UTL3x1)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTR1x1*yR1*complexconjugate(UTL3x4)*cmath.sqrt(1 - xi))/fs - (complex(0,1)*UTR1x4*yL1*complexconjugate(UTL3x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) + (complex(0,1)*UTR1x1*yR4*complexconjugate(UTL3x2)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTR1x1*yR4*complexconjugate(UTL3x3)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '(complex(0,1)*UTR2x2*yL4*complexconjugate(UTL3x1)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTR2x3*yL4*complexconjugate(UTL3x1)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTR2x1*yR1*complexconjugate(UTL3x4)*cmath.sqrt(1 - xi))/fs - (complex(0,1)*UTR2x4*yL1*complexconjugate(UTL3x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) + (complex(0,1)*UTR2x1*yR4*complexconjugate(UTL3x2)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTR2x1*yR4*complexconjugate(UTL3x3)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                  order = {'QED':1})

GC_102 = Coupling(name = 'GC_102',
                  value = '(complex(0,1)*UTR3x2*yL4*complexconjugate(UTL3x1)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTR3x3*yL4*complexconjugate(UTL3x1)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTR3x1*yR1*complexconjugate(UTL3x4)*cmath.sqrt(1 - xi))/fs - (complex(0,1)*UTR3x4*yL1*complexconjugate(UTL3x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) + (complex(0,1)*UTR3x1*yR4*complexconjugate(UTL3x2)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTR3x1*yR4*complexconjugate(UTL3x3)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                  order = {'QED':1})

GC_103 = Coupling(name = 'GC_103',
                  value = '(complex(0,1)*UTR4x2*yL4*complexconjugate(UTL3x1)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTR4x3*yL4*complexconjugate(UTL3x1)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTR4x1*yR1*complexconjugate(UTL3x4)*cmath.sqrt(1 - xi))/fs - (complex(0,1)*UTR4x4*yL1*complexconjugate(UTL3x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) + (complex(0,1)*UTR4x1*yR4*complexconjugate(UTL3x2)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTR4x1*yR4*complexconjugate(UTL3x3)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                  order = {'QED':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '(complex(0,1)*UTR1x4*yL1*complexconjugate(UTL3x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) - (complex(0,1)*UTR1x1*yR4*complexconjugate(UTL3x2)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR1x1*yR4*complexconjugate(UTL3x3)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR1x2*yL4*complexconjugate(UTL3x1)*cmath.sqrt(xi))/2. - (complex(0,1)*UTR1x3*yL4*complexconjugate(UTL3x1)*cmath.sqrt(xi))/2. + complex(0,1)*UTR1x1*yR1*complexconjugate(UTL3x4)*cmath.sqrt(xi)',
                  order = {'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '(complex(0,1)*UTR2x4*yL1*complexconjugate(UTL3x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) - (complex(0,1)*UTR2x1*yR4*complexconjugate(UTL3x2)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR2x1*yR4*complexconjugate(UTL3x3)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR2x2*yL4*complexconjugate(UTL3x1)*cmath.sqrt(xi))/2. - (complex(0,1)*UTR2x3*yL4*complexconjugate(UTL3x1)*cmath.sqrt(xi))/2. + complex(0,1)*UTR2x1*yR1*complexconjugate(UTL3x4)*cmath.sqrt(xi)',
                  order = {'QED':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '(complex(0,1)*UTR3x4*yL1*complexconjugate(UTL3x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) - (complex(0,1)*UTR3x1*yR4*complexconjugate(UTL3x2)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR3x1*yR4*complexconjugate(UTL3x3)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR3x2*yL4*complexconjugate(UTL3x1)*cmath.sqrt(xi))/2. - (complex(0,1)*UTR3x3*yL4*complexconjugate(UTL3x1)*cmath.sqrt(xi))/2. + complex(0,1)*UTR3x1*yR1*complexconjugate(UTL3x4)*cmath.sqrt(xi)',
                  order = {'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '(complex(0,1)*UTR4x4*yL1*complexconjugate(UTL3x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) - (complex(0,1)*UTR4x1*yR4*complexconjugate(UTL3x2)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR4x1*yR4*complexconjugate(UTL3x3)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR4x2*yL4*complexconjugate(UTL3x1)*cmath.sqrt(xi))/2. - (complex(0,1)*UTR4x3*yL4*complexconjugate(UTL3x1)*cmath.sqrt(xi))/2. + complex(0,1)*UTR4x1*yR1*complexconjugate(UTL3x4)*cmath.sqrt(xi)',
                  order = {'QED':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '(ee*complex(0,1)*complexconjugate(UTL4x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(UTL4x3))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(UTL4x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(UTL4x3)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_109 = Coupling(name = 'GC_109',
                  value = '(ee*complex(0,1)*UBL1x1*complexconjugate(UTL4x1))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBL1x2*complexconjugate(UTL4x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBL1x2*complexconjugate(UTL4x3))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBL1x2*complexconjugate(UTL4x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UBL1x2*complexconjugate(UTL4x3)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '(ee*complex(0,1)*UBL2x1*complexconjugate(UTL4x1))/(sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBL2x2*complexconjugate(UTL4x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBL2x2*complexconjugate(UTL4x3))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBL2x2*complexconjugate(UTL4x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UBL2x2*complexconjugate(UTL4x3)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_111 = Coupling(name = 'GC_111',
                  value = '(ee*complex(0,1)*UTL1x1*complexconjugate(UTL4x1))/(2.*cw*sw) - (2*ee*complex(0,1)*sw*UTL1x1*complexconjugate(UTL4x1))/(3.*cw) - (2*ee*complex(0,1)*sw*UTL1x2*complexconjugate(UTL4x2))/(3.*cw) - (2*ee*complex(0,1)*sw*UTL1x3*complexconjugate(UTL4x3))/(3.*cw) - (2*ee*complex(0,1)*sw*UTL1x4*complexconjugate(UTL4x4))/(3.*cw) + (ee*complex(0,1)*UTL1x2*complexconjugate(UTL4x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTL1x3*complexconjugate(UTL4x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                  order = {'QED':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '-(ee*complex(0,1)*UTL2x2*complexconjugate(UTL4x2))/(2.*cw*sw) - (ee*complex(0,1)*UTL2x3*complexconjugate(UTL4x3))/(2.*cw*sw) - (ee*complex(0,1)*UTL2x4*complexconjugate(UTL4x4))/(2.*cw*sw) + (ee*complex(0,1)*UTL2x2*complexconjugate(UTL4x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTL2x3*complexconjugate(UTL4x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                  order = {'QED':1})

GC_113 = Coupling(name = 'GC_113',
                  value = '-(ee*complex(0,1)*UTL3x2*complexconjugate(UTL4x2))/(2.*cw*sw) - (ee*complex(0,1)*UTL3x3*complexconjugate(UTL4x3))/(2.*cw*sw) - (ee*complex(0,1)*UTL3x4*complexconjugate(UTL4x4))/(2.*cw*sw) + (ee*complex(0,1)*UTL3x2*complexconjugate(UTL4x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTL3x3*complexconjugate(UTL4x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                  order = {'QED':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '(ee*complex(0,1))/(2.*cw*sw) - (2*ee*complex(0,1)*sw)/(3.*cw) - (ee*complex(0,1)*UTL4x2*complexconjugate(UTL4x2))/(2.*cw*sw) - (ee*complex(0,1)*UTL4x3*complexconjugate(UTL4x3))/(2.*cw*sw) - (ee*complex(0,1)*UTL4x4*complexconjugate(UTL4x4))/(2.*cw*sw) + (ee*complex(0,1)*UTL4x2*complexconjugate(UTL4x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTL4x3*complexconjugate(UTL4x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                  order = {'QED':1})

GC_115 = Coupling(name = 'GC_115',
                  value = '-((ee*complex(0,1))/(cw*sw)) + (ee*complex(0,1)*UTL2x2*complexconjugate(UTL2x2))/(2.*cw*sw) + (ee*complex(0,1)*UTL2x3*complexconjugate(UTL2x3))/(2.*cw*sw) + (ee*complex(0,1)*UTL2x4*complexconjugate(UTL2x4))/(2.*cw*sw) + (ee*complex(0,1)*UTL3x2*complexconjugate(UTL3x2))/(2.*cw*sw) + (ee*complex(0,1)*UTL3x3*complexconjugate(UTL3x3))/(2.*cw*sw) + (ee*complex(0,1)*UTL3x4*complexconjugate(UTL3x4))/(2.*cw*sw) + (ee*complex(0,1)*UTL4x2*complexconjugate(UTL4x2))/(2.*cw*sw) + (ee*complex(0,1)*UTL4x3*complexconjugate(UTL4x3))/(2.*cw*sw) + (ee*complex(0,1)*UTL4x4*complexconjugate(UTL4x4))/(2.*cw*sw) - (ee*complex(0,1)*UTL2x2*complexconjugate(UTL2x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) + (ee*complex(0,1)*UTL2x3*complexconjugate(UTL2x3)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTL3x2*complexconjugate(UTL3x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) + (ee*complex(0,1)*UTL3x3*complexconjugate(UTL3x3)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTL4x2*complexconjugate(UTL4x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) + (ee*complex(0,1)*UTL4x3*complexconjugate(UTL4x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                  order = {'QED':1})

GC_116 = Coupling(name = 'GC_116',
                  value = '(complex(0,1)*UTR1x2*yL4*complexconjugate(UTL4x1)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTR1x3*yL4*complexconjugate(UTL4x1)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTR1x1*yR1*complexconjugate(UTL4x4)*cmath.sqrt(1 - xi))/fs - (complex(0,1)*UTR1x4*yL1*complexconjugate(UTL4x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) + (complex(0,1)*UTR1x1*yR4*complexconjugate(UTL4x2)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTR1x1*yR4*complexconjugate(UTL4x3)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                  order = {'QED':1})

GC_117 = Coupling(name = 'GC_117',
                  value = '(complex(0,1)*UTR2x2*yL4*complexconjugate(UTL4x1)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTR2x3*yL4*complexconjugate(UTL4x1)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTR2x1*yR1*complexconjugate(UTL4x4)*cmath.sqrt(1 - xi))/fs - (complex(0,1)*UTR2x4*yL1*complexconjugate(UTL4x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) + (complex(0,1)*UTR2x1*yR4*complexconjugate(UTL4x2)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTR2x1*yR4*complexconjugate(UTL4x3)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                  order = {'QED':1})

GC_118 = Coupling(name = 'GC_118',
                  value = '(complex(0,1)*UTR3x2*yL4*complexconjugate(UTL4x1)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTR3x3*yL4*complexconjugate(UTL4x1)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTR3x1*yR1*complexconjugate(UTL4x4)*cmath.sqrt(1 - xi))/fs - (complex(0,1)*UTR3x4*yL1*complexconjugate(UTL4x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) + (complex(0,1)*UTR3x1*yR4*complexconjugate(UTL4x2)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTR3x1*yR4*complexconjugate(UTL4x3)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                  order = {'QED':1})

GC_119 = Coupling(name = 'GC_119',
                  value = '(complex(0,1)*UTR4x2*yL4*complexconjugate(UTL4x1)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTR4x3*yL4*complexconjugate(UTL4x1)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTR4x1*yR1*complexconjugate(UTL4x4)*cmath.sqrt(1 - xi))/fs - (complex(0,1)*UTR4x4*yL1*complexconjugate(UTL4x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) + (complex(0,1)*UTR4x1*yR4*complexconjugate(UTL4x2)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTR4x1*yR4*complexconjugate(UTL4x3)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                  order = {'QED':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '(complex(0,1)*UTR1x4*yL1*complexconjugate(UTL4x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) - (complex(0,1)*UTR1x1*yR4*complexconjugate(UTL4x2)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR1x1*yR4*complexconjugate(UTL4x3)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR1x2*yL4*complexconjugate(UTL4x1)*cmath.sqrt(xi))/2. - (complex(0,1)*UTR1x3*yL4*complexconjugate(UTL4x1)*cmath.sqrt(xi))/2. + complex(0,1)*UTR1x1*yR1*complexconjugate(UTL4x4)*cmath.sqrt(xi)',
                  order = {'QED':1})

GC_121 = Coupling(name = 'GC_121',
                  value = '(complex(0,1)*UTR2x4*yL1*complexconjugate(UTL4x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) - (complex(0,1)*UTR2x1*yR4*complexconjugate(UTL4x2)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR2x1*yR4*complexconjugate(UTL4x3)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR2x2*yL4*complexconjugate(UTL4x1)*cmath.sqrt(xi))/2. - (complex(0,1)*UTR2x3*yL4*complexconjugate(UTL4x1)*cmath.sqrt(xi))/2. + complex(0,1)*UTR2x1*yR1*complexconjugate(UTL4x4)*cmath.sqrt(xi)',
                  order = {'QED':1})

GC_122 = Coupling(name = 'GC_122',
                  value = '(complex(0,1)*UTR3x4*yL1*complexconjugate(UTL4x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) - (complex(0,1)*UTR3x1*yR4*complexconjugate(UTL4x2)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR3x1*yR4*complexconjugate(UTL4x3)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR3x2*yL4*complexconjugate(UTL4x1)*cmath.sqrt(xi))/2. - (complex(0,1)*UTR3x3*yL4*complexconjugate(UTL4x1)*cmath.sqrt(xi))/2. + complex(0,1)*UTR3x1*yR1*complexconjugate(UTL4x4)*cmath.sqrt(xi)',
                  order = {'QED':1})

GC_123 = Coupling(name = 'GC_123',
                  value = '(complex(0,1)*UTR4x4*yL1*complexconjugate(UTL4x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) - (complex(0,1)*UTR4x1*yR4*complexconjugate(UTL4x2)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR4x1*yR4*complexconjugate(UTL4x3)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTR4x2*yL4*complexconjugate(UTL4x1)*cmath.sqrt(xi))/2. - (complex(0,1)*UTR4x3*yL4*complexconjugate(UTL4x1)*cmath.sqrt(xi))/2. + complex(0,1)*UTR4x1*yR1*complexconjugate(UTL4x4)*cmath.sqrt(xi)',
                  order = {'QED':1})

GC_124 = Coupling(name = 'GC_124',
                  value = '(ee*complex(0,1)*complexconjugate(UTR1x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(UTR1x3))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(UTR1x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(UTR1x3)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_125 = Coupling(name = 'GC_125',
                  value = '(ee*complex(0,1)*UBR1x2*complexconjugate(UTR1x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBR1x2*complexconjugate(UTR1x3))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBR1x2*complexconjugate(UTR1x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UBR1x2*complexconjugate(UTR1x3)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_126 = Coupling(name = 'GC_126',
                  value = '(ee*complex(0,1)*UBR2x2*complexconjugate(UTR1x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBR2x2*complexconjugate(UTR1x3))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBR2x2*complexconjugate(UTR1x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UBR2x2*complexconjugate(UTR1x3)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_127 = Coupling(name = 'GC_127',
                  value = '(-2*ee*complex(0,1)*sw*UTR2x1*complexconjugate(UTR1x1))/(3.*cw) - (2*ee*complex(0,1)*sw*UTR2x2*complexconjugate(UTR1x2))/(3.*cw) - (2*ee*complex(0,1)*sw*UTR2x3*complexconjugate(UTR1x3))/(3.*cw) - (2*ee*complex(0,1)*sw*UTR2x4*complexconjugate(UTR1x4))/(3.*cw) + (ee*complex(0,1)*UTR2x2*complexconjugate(UTR1x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTR2x3*complexconjugate(UTR1x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                  order = {'QED':1})

GC_128 = Coupling(name = 'GC_128',
                  value = '(-2*ee*complex(0,1)*sw*UTR3x1*complexconjugate(UTR1x1))/(3.*cw) - (2*ee*complex(0,1)*sw*UTR3x2*complexconjugate(UTR1x2))/(3.*cw) - (2*ee*complex(0,1)*sw*UTR3x3*complexconjugate(UTR1x3))/(3.*cw) - (2*ee*complex(0,1)*sw*UTR3x4*complexconjugate(UTR1x4))/(3.*cw) + (ee*complex(0,1)*UTR3x2*complexconjugate(UTR1x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTR3x3*complexconjugate(UTR1x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                  order = {'QED':1})

GC_129 = Coupling(name = 'GC_129',
                  value = '(-2*ee*complex(0,1)*sw*UTR4x1*complexconjugate(UTR1x1))/(3.*cw) - (2*ee*complex(0,1)*sw*UTR4x2*complexconjugate(UTR1x2))/(3.*cw) - (2*ee*complex(0,1)*sw*UTR4x3*complexconjugate(UTR1x3))/(3.*cw) - (2*ee*complex(0,1)*sw*UTR4x4*complexconjugate(UTR1x4))/(3.*cw) + (ee*complex(0,1)*UTR4x2*complexconjugate(UTR1x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTR4x3*complexconjugate(UTR1x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                  order = {'QED':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '(mtLS/mtHS)*(-((complex(0,1)*UTL1x2*yR4*complexconjugate(UTR1x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2)) + (complex(0,1)*UTL1x3*yR4*complexconjugate(UTR1x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTL1x1*yL1*complexconjugate(UTR1x4)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + complex(0,1)*UTL1x4*yR1*complexconjugate(UTR1x1)*cmath.sqrt(xi) + (complex(0,1)*UTL1x1*yL4*complexconjugate(UTR1x2)*cmath.sqrt(xi))/2. - (complex(0,1)*UTL1x1*yL4*complexconjugate(UTR1x3)*cmath.sqrt(xi))/2.)',
                  order = {'QED':1})

GC_131 = Coupling(name = 'GC_131',
                  value = '-((complex(0,1)*UTL2x2*yR4*complexconjugate(UTR1x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2)) + (complex(0,1)*UTL2x3*yR4*complexconjugate(UTR1x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTL2x1*yL1*complexconjugate(UTR1x4)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + complex(0,1)*UTL2x4*yR1*complexconjugate(UTR1x1)*cmath.sqrt(xi) + (complex(0,1)*UTL2x1*yL4*complexconjugate(UTR1x2)*cmath.sqrt(xi))/2. - (complex(0,1)*UTL2x1*yL4*complexconjugate(UTR1x3)*cmath.sqrt(xi))/2.',
                  order = {'QED':1})

GC_132 = Coupling(name = 'GC_132',
                  value = '-((complex(0,1)*UTL3x2*yR4*complexconjugate(UTR1x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2)) + (complex(0,1)*UTL3x3*yR4*complexconjugate(UTR1x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTL3x1*yL1*complexconjugate(UTR1x4)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + complex(0,1)*UTL3x4*yR1*complexconjugate(UTR1x1)*cmath.sqrt(xi) + (complex(0,1)*UTL3x1*yL4*complexconjugate(UTR1x2)*cmath.sqrt(xi))/2. - (complex(0,1)*UTL3x1*yL4*complexconjugate(UTR1x3)*cmath.sqrt(xi))/2.',
                  order = {'QED':1})

GC_133 = Coupling(name = 'GC_133',
                  value = '-((complex(0,1)*UTL4x2*yR4*complexconjugate(UTR1x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2)) + (complex(0,1)*UTL4x3*yR4*complexconjugate(UTR1x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTL4x1*yL1*complexconjugate(UTR1x4)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + complex(0,1)*UTL4x4*yR1*complexconjugate(UTR1x1)*cmath.sqrt(xi) + (complex(0,1)*UTL4x1*yL4*complexconjugate(UTR1x2)*cmath.sqrt(xi))/2. - (complex(0,1)*UTL4x1*yL4*complexconjugate(UTR1x3)*cmath.sqrt(xi))/2.',
                  order = {'QED':1})

GC_134 = Coupling(name = 'GC_134',
                  value = '(complex(0,1)*UTL1x4*yR1*complexconjugate(UTR1x1)*cmath.sqrt(1 - xi))/fs + (complex(0,1)*UTL1x1*yL4*complexconjugate(UTR1x2)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTL1x1*yL4*complexconjugate(UTR1x3)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTL1x2*yR4*complexconjugate(UTR1x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL1x3*yR4*complexconjugate(UTR1x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL1x1*yL1*complexconjugate(UTR1x4)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                  order = {'QED':1})

GC_135 = Coupling(name = 'GC_135',
                  value = '(complex(0,1)*UTL2x4*yR1*complexconjugate(UTR1x1)*cmath.sqrt(1 - xi))/fs + (complex(0,1)*UTL2x1*yL4*complexconjugate(UTR1x2)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTL2x1*yL4*complexconjugate(UTR1x3)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTL2x2*yR4*complexconjugate(UTR1x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL2x3*yR4*complexconjugate(UTR1x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL2x1*yL1*complexconjugate(UTR1x4)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                  order = {'QED':1})

GC_136 = Coupling(name = 'GC_136',
                  value = '(complex(0,1)*UTL3x4*yR1*complexconjugate(UTR1x1)*cmath.sqrt(1 - xi))/fs + (complex(0,1)*UTL3x1*yL4*complexconjugate(UTR1x2)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTL3x1*yL4*complexconjugate(UTR1x3)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTL3x2*yR4*complexconjugate(UTR1x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL3x3*yR4*complexconjugate(UTR1x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL3x1*yL1*complexconjugate(UTR1x4)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                  order = {'QED':1})

GC_137 = Coupling(name = 'GC_137',
                  value = '(complex(0,1)*UTL4x4*yR1*complexconjugate(UTR1x1)*cmath.sqrt(1 - xi))/fs + (complex(0,1)*UTL4x1*yL4*complexconjugate(UTR1x2)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTL4x1*yL4*complexconjugate(UTR1x3)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTL4x2*yR4*complexconjugate(UTR1x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL4x3*yR4*complexconjugate(UTR1x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL4x1*yL1*complexconjugate(UTR1x4)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                  order = {'QED':1})

GC_138 = Coupling(name = 'GC_138',
                  value = '(ee*complex(0,1)*complexconjugate(UTR2x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(UTR2x3))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(UTR2x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(UTR2x3)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_139 = Coupling(name = 'GC_139',
                  value = '(ee*complex(0,1)*UBR1x2*complexconjugate(UTR2x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBR1x2*complexconjugate(UTR2x3))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBR1x2*complexconjugate(UTR2x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UBR1x2*complexconjugate(UTR2x3)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_140 = Coupling(name = 'GC_140',
                  value = '(ee*complex(0,1)*UBR2x2*complexconjugate(UTR2x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBR2x2*complexconjugate(UTR2x3))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBR2x2*complexconjugate(UTR2x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UBR2x2*complexconjugate(UTR2x3)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_141 = Coupling(name = 'GC_141',
                  value = '(-2*ee*complex(0,1)*sw)/(3.*cw) + (ee*complex(0,1)*UTR2x2*complexconjugate(UTR2x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTR2x3*complexconjugate(UTR2x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                  order = {'QED':1})

GC_142 = Coupling(name = 'GC_142',
                  value = '(ee*complex(0,1)*UTR3x2*complexconjugate(UTR2x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTR3x3*complexconjugate(UTR2x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                  order = {'QED':1})

GC_143 = Coupling(name = 'GC_143',
                  value = '(ee*complex(0,1)*UTR4x2*complexconjugate(UTR2x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTR4x3*complexconjugate(UTR2x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                  order = {'QED':1})

GC_144 = Coupling(name = 'GC_144',
                  value = '(-2*ee*complex(0,1)*sw*UTR1x1*complexconjugate(UTR2x1))/(3.*cw) - (2*ee*complex(0,1)*sw*UTR1x2*complexconjugate(UTR2x2))/(3.*cw) - (2*ee*complex(0,1)*sw*UTR1x3*complexconjugate(UTR2x3))/(3.*cw) - (2*ee*complex(0,1)*sw*UTR1x4*complexconjugate(UTR2x4))/(3.*cw) + (ee*complex(0,1)*UTR1x2*complexconjugate(UTR2x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTR1x3*complexconjugate(UTR2x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                  order = {'QED':1})

GC_145 = Coupling(name = 'GC_145',
                  value = '-((complex(0,1)*UTL1x2*yR4*complexconjugate(UTR2x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2)) + (complex(0,1)*UTL1x3*yR4*complexconjugate(UTR2x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTL1x1*yL1*complexconjugate(UTR2x4)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + complex(0,1)*UTL1x4*yR1*complexconjugate(UTR2x1)*cmath.sqrt(xi) + (complex(0,1)*UTL1x1*yL4*complexconjugate(UTR2x2)*cmath.sqrt(xi))/2. - (complex(0,1)*UTL1x1*yL4*complexconjugate(UTR2x3)*cmath.sqrt(xi))/2.',
                  order = {'QED':1})

GC_146 = Coupling(name = 'GC_146',
                  value = '-((complex(0,1)*UTL2x2*yR4*complexconjugate(UTR2x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2)) + (complex(0,1)*UTL2x3*yR4*complexconjugate(UTR2x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTL2x1*yL1*complexconjugate(UTR2x4)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + complex(0,1)*UTL2x4*yR1*complexconjugate(UTR2x1)*cmath.sqrt(xi) + (complex(0,1)*UTL2x1*yL4*complexconjugate(UTR2x2)*cmath.sqrt(xi))/2. - (complex(0,1)*UTL2x1*yL4*complexconjugate(UTR2x3)*cmath.sqrt(xi))/2.',
                  order = {'QED':1})

GC_147 = Coupling(name = 'GC_147',
                  value = '-((complex(0,1)*UTL3x2*yR4*complexconjugate(UTR2x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2)) + (complex(0,1)*UTL3x3*yR4*complexconjugate(UTR2x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTL3x1*yL1*complexconjugate(UTR2x4)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + complex(0,1)*UTL3x4*yR1*complexconjugate(UTR2x1)*cmath.sqrt(xi) + (complex(0,1)*UTL3x1*yL4*complexconjugate(UTR2x2)*cmath.sqrt(xi))/2. - (complex(0,1)*UTL3x1*yL4*complexconjugate(UTR2x3)*cmath.sqrt(xi))/2.',
                  order = {'QED':1})

GC_148 = Coupling(name = 'GC_148',
                  value = '-((complex(0,1)*UTL4x2*yR4*complexconjugate(UTR2x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2)) + (complex(0,1)*UTL4x3*yR4*complexconjugate(UTR2x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTL4x1*yL1*complexconjugate(UTR2x4)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + complex(0,1)*UTL4x4*yR1*complexconjugate(UTR2x1)*cmath.sqrt(xi) + (complex(0,1)*UTL4x1*yL4*complexconjugate(UTR2x2)*cmath.sqrt(xi))/2. - (complex(0,1)*UTL4x1*yL4*complexconjugate(UTR2x3)*cmath.sqrt(xi))/2.',
                  order = {'QED':1})

GC_149 = Coupling(name = 'GC_149',
                  value = '(complex(0,1)*UTL1x4*yR1*complexconjugate(UTR2x1)*cmath.sqrt(1 - xi))/fs + (complex(0,1)*UTL1x1*yL4*complexconjugate(UTR2x2)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTL1x1*yL4*complexconjugate(UTR2x3)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTL1x2*yR4*complexconjugate(UTR2x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL1x3*yR4*complexconjugate(UTR2x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL1x1*yL1*complexconjugate(UTR2x4)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                  order = {'QED':1})

GC_150 = Coupling(name = 'GC_150',
                  value = '(complex(0,1)*UTL2x4*yR1*complexconjugate(UTR2x1)*cmath.sqrt(1 - xi))/fs + (complex(0,1)*UTL2x1*yL4*complexconjugate(UTR2x2)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTL2x1*yL4*complexconjugate(UTR2x3)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTL2x2*yR4*complexconjugate(UTR2x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL2x3*yR4*complexconjugate(UTR2x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL2x1*yL1*complexconjugate(UTR2x4)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                  order = {'QED':1})

GC_151 = Coupling(name = 'GC_151',
                  value = '(complex(0,1)*UTL3x4*yR1*complexconjugate(UTR2x1)*cmath.sqrt(1 - xi))/fs + (complex(0,1)*UTL3x1*yL4*complexconjugate(UTR2x2)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTL3x1*yL4*complexconjugate(UTR2x3)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTL3x2*yR4*complexconjugate(UTR2x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL3x3*yR4*complexconjugate(UTR2x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL3x1*yL1*complexconjugate(UTR2x4)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                  order = {'QED':1})

GC_152 = Coupling(name = 'GC_152',
                  value = '(complex(0,1)*UTL4x4*yR1*complexconjugate(UTR2x1)*cmath.sqrt(1 - xi))/fs + (complex(0,1)*UTL4x1*yL4*complexconjugate(UTR2x2)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTL4x1*yL4*complexconjugate(UTR2x3)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTL4x2*yR4*complexconjugate(UTR2x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL4x3*yR4*complexconjugate(UTR2x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL4x1*yL1*complexconjugate(UTR2x4)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                  order = {'QED':1})

GC_153 = Coupling(name = 'GC_153',
                  value = '(ee*complex(0,1)*complexconjugate(UTR3x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(UTR3x3))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(UTR3x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(UTR3x3)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_154 = Coupling(name = 'GC_154',
                  value = '(ee*complex(0,1)*UBR1x2*complexconjugate(UTR3x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBR1x2*complexconjugate(UTR3x3))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBR1x2*complexconjugate(UTR3x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UBR1x2*complexconjugate(UTR3x3)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_155 = Coupling(name = 'GC_155',
                  value = '(ee*complex(0,1)*UBR2x2*complexconjugate(UTR3x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBR2x2*complexconjugate(UTR3x3))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBR2x2*complexconjugate(UTR3x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UBR2x2*complexconjugate(UTR3x3)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_156 = Coupling(name = 'GC_156',
                  value = '(ee*complex(0,1)*UTR2x2*complexconjugate(UTR3x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTR2x3*complexconjugate(UTR3x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                  order = {'QED':1})

GC_157 = Coupling(name = 'GC_157',
                  value = '(-2*ee*complex(0,1)*sw)/(3.*cw) + (ee*complex(0,1)*UTR3x2*complexconjugate(UTR3x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTR3x3*complexconjugate(UTR3x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                  order = {'QED':1})

GC_158 = Coupling(name = 'GC_158',
                  value = '(ee*complex(0,1)*UTR4x2*complexconjugate(UTR3x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTR4x3*complexconjugate(UTR3x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                  order = {'QED':1})

GC_159 = Coupling(name = 'GC_159',
                  value = '(-2*ee*complex(0,1)*sw*UTR1x1*complexconjugate(UTR3x1))/(3.*cw) - (2*ee*complex(0,1)*sw*UTR1x2*complexconjugate(UTR3x2))/(3.*cw) - (2*ee*complex(0,1)*sw*UTR1x3*complexconjugate(UTR3x3))/(3.*cw) - (2*ee*complex(0,1)*sw*UTR1x4*complexconjugate(UTR3x4))/(3.*cw) + (ee*complex(0,1)*UTR1x2*complexconjugate(UTR3x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTR1x3*complexconjugate(UTR3x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                  order = {'QED':1})

GC_160 = Coupling(name = 'GC_160',
                  value = '-((complex(0,1)*UTL1x2*yR4*complexconjugate(UTR3x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2)) + (complex(0,1)*UTL1x3*yR4*complexconjugate(UTR3x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTL1x1*yL1*complexconjugate(UTR3x4)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + complex(0,1)*UTL1x4*yR1*complexconjugate(UTR3x1)*cmath.sqrt(xi) + (complex(0,1)*UTL1x1*yL4*complexconjugate(UTR3x2)*cmath.sqrt(xi))/2. - (complex(0,1)*UTL1x1*yL4*complexconjugate(UTR3x3)*cmath.sqrt(xi))/2.',
                  order = {'QED':1})

GC_161 = Coupling(name = 'GC_161',
                  value = '-((complex(0,1)*UTL2x2*yR4*complexconjugate(UTR3x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2)) + (complex(0,1)*UTL2x3*yR4*complexconjugate(UTR3x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTL2x1*yL1*complexconjugate(UTR3x4)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + complex(0,1)*UTL2x4*yR1*complexconjugate(UTR3x1)*cmath.sqrt(xi) + (complex(0,1)*UTL2x1*yL4*complexconjugate(UTR3x2)*cmath.sqrt(xi))/2. - (complex(0,1)*UTL2x1*yL4*complexconjugate(UTR3x3)*cmath.sqrt(xi))/2.',
                  order = {'QED':1})

GC_162 = Coupling(name = 'GC_162',
                  value = '-((complex(0,1)*UTL3x2*yR4*complexconjugate(UTR3x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2)) + (complex(0,1)*UTL3x3*yR4*complexconjugate(UTR3x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTL3x1*yL1*complexconjugate(UTR3x4)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + complex(0,1)*UTL3x4*yR1*complexconjugate(UTR3x1)*cmath.sqrt(xi) + (complex(0,1)*UTL3x1*yL4*complexconjugate(UTR3x2)*cmath.sqrt(xi))/2. - (complex(0,1)*UTL3x1*yL4*complexconjugate(UTR3x3)*cmath.sqrt(xi))/2.',
                  order = {'QED':1})

GC_163 = Coupling(name = 'GC_163',
                  value = '-((complex(0,1)*UTL4x2*yR4*complexconjugate(UTR3x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2)) + (complex(0,1)*UTL4x3*yR4*complexconjugate(UTR3x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTL4x1*yL1*complexconjugate(UTR3x4)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + complex(0,1)*UTL4x4*yR1*complexconjugate(UTR3x1)*cmath.sqrt(xi) + (complex(0,1)*UTL4x1*yL4*complexconjugate(UTR3x2)*cmath.sqrt(xi))/2. - (complex(0,1)*UTL4x1*yL4*complexconjugate(UTR3x3)*cmath.sqrt(xi))/2.',
                  order = {'QED':1})

GC_164 = Coupling(name = 'GC_164',
                  value = '(complex(0,1)*UTL1x4*yR1*complexconjugate(UTR3x1)*cmath.sqrt(1 - xi))/fs + (complex(0,1)*UTL1x1*yL4*complexconjugate(UTR3x2)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTL1x1*yL4*complexconjugate(UTR3x3)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTL1x2*yR4*complexconjugate(UTR3x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL1x3*yR4*complexconjugate(UTR3x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL1x1*yL1*complexconjugate(UTR3x4)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                  order = {'QED':1})

GC_165 = Coupling(name = 'GC_165',
                  value = '(complex(0,1)*UTL2x4*yR1*complexconjugate(UTR3x1)*cmath.sqrt(1 - xi))/fs + (complex(0,1)*UTL2x1*yL4*complexconjugate(UTR3x2)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTL2x1*yL4*complexconjugate(UTR3x3)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTL2x2*yR4*complexconjugate(UTR3x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL2x3*yR4*complexconjugate(UTR3x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL2x1*yL1*complexconjugate(UTR3x4)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                  order = {'QED':1})

GC_166 = Coupling(name = 'GC_166',
                  value = '(complex(0,1)*UTL3x4*yR1*complexconjugate(UTR3x1)*cmath.sqrt(1 - xi))/fs + (complex(0,1)*UTL3x1*yL4*complexconjugate(UTR3x2)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTL3x1*yL4*complexconjugate(UTR3x3)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTL3x2*yR4*complexconjugate(UTR3x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL3x3*yR4*complexconjugate(UTR3x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL3x1*yL1*complexconjugate(UTR3x4)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                  order = {'QED':1})

GC_167 = Coupling(name = 'GC_167',
                  value = '(complex(0,1)*UTL4x4*yR1*complexconjugate(UTR3x1)*cmath.sqrt(1 - xi))/fs + (complex(0,1)*UTL4x1*yL4*complexconjugate(UTR3x2)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTL4x1*yL4*complexconjugate(UTR3x3)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTL4x2*yR4*complexconjugate(UTR3x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL4x3*yR4*complexconjugate(UTR3x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL4x1*yL1*complexconjugate(UTR3x4)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                  order = {'QED':1})

GC_168 = Coupling(name = 'GC_168',
                  value = '(ee*complex(0,1)*complexconjugate(UTR4x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(UTR4x3))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*complexconjugate(UTR4x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*complexconjugate(UTR4x3)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_169 = Coupling(name = 'GC_169',
                  value = '(ee*complex(0,1)*UBR1x2*complexconjugate(UTR4x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBR1x2*complexconjugate(UTR4x3))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBR1x2*complexconjugate(UTR4x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UBR1x2*complexconjugate(UTR4x3)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_170 = Coupling(name = 'GC_170',
                  value = '(ee*complex(0,1)*UBR2x2*complexconjugate(UTR4x2))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBR2x2*complexconjugate(UTR4x3))/(2.*sw*cmath.sqrt(2)) + (ee*complex(0,1)*UBR2x2*complexconjugate(UTR4x2)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2)) - (ee*complex(0,1)*UBR2x2*complexconjugate(UTR4x3)*cmath.sqrt(1 - xi))/(2.*sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_171 = Coupling(name = 'GC_171',
                  value = '(ee*complex(0,1)*UTR2x2*complexconjugate(UTR4x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTR2x3*complexconjugate(UTR4x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                  order = {'QED':1})

GC_172 = Coupling(name = 'GC_172',
                  value = '(ee*complex(0,1)*UTR3x2*complexconjugate(UTR4x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTR3x3*complexconjugate(UTR4x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                  order = {'QED':1})

GC_173 = Coupling(name = 'GC_173',
                  value = '(-2*ee*complex(0,1)*sw)/(3.*cw) + (ee*complex(0,1)*UTR4x2*complexconjugate(UTR4x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTR4x3*complexconjugate(UTR4x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                  order = {'QED':1})

GC_174 = Coupling(name = 'GC_174',
                  value = '-(ee*complex(0,1)*UTR2x2*complexconjugate(UTR2x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) + (ee*complex(0,1)*UTR2x3*complexconjugate(UTR2x3)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTR3x2*complexconjugate(UTR3x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) + (ee*complex(0,1)*UTR3x3*complexconjugate(UTR3x3)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTR4x2*complexconjugate(UTR4x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) + (ee*complex(0,1)*UTR4x3*complexconjugate(UTR4x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                  order = {'QED':1})

GC_175 = Coupling(name = 'GC_175',
                  value = '(-2*ee*complex(0,1)*sw*UTR1x1*complexconjugate(UTR4x1))/(3.*cw) - (2*ee*complex(0,1)*sw*UTR1x2*complexconjugate(UTR4x2))/(3.*cw) - (2*ee*complex(0,1)*sw*UTR1x3*complexconjugate(UTR4x3))/(3.*cw) - (2*ee*complex(0,1)*sw*UTR1x4*complexconjugate(UTR4x4))/(3.*cw) + (ee*complex(0,1)*UTR1x2*complexconjugate(UTR4x2)*cmath.sqrt(1 - xi))/(2.*cw*sw) - (ee*complex(0,1)*UTR1x3*complexconjugate(UTR4x3)*cmath.sqrt(1 - xi))/(2.*cw*sw)',
                  order = {'QED':1})

GC_176 = Coupling(name = 'GC_176',
                  value = '-((complex(0,1)*UTL1x2*yR4*complexconjugate(UTR4x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2)) + (complex(0,1)*UTL1x3*yR4*complexconjugate(UTR4x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTL1x1*yL1*complexconjugate(UTR4x4)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + complex(0,1)*UTL1x4*yR1*complexconjugate(UTR4x1)*cmath.sqrt(xi) + (complex(0,1)*UTL1x1*yL4*complexconjugate(UTR4x2)*cmath.sqrt(xi))/2. - (complex(0,1)*UTL1x1*yL4*complexconjugate(UTR4x3)*cmath.sqrt(xi))/2.',
                  order = {'QED':1})

GC_177 = Coupling(name = 'GC_177',
                  value = '-((complex(0,1)*UTL2x2*yR4*complexconjugate(UTR4x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2)) + (complex(0,1)*UTL2x3*yR4*complexconjugate(UTR4x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTL2x1*yL1*complexconjugate(UTR4x4)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + complex(0,1)*UTL2x4*yR1*complexconjugate(UTR4x1)*cmath.sqrt(xi) + (complex(0,1)*UTL2x1*yL4*complexconjugate(UTR4x2)*cmath.sqrt(xi))/2. - (complex(0,1)*UTL2x1*yL4*complexconjugate(UTR4x3)*cmath.sqrt(xi))/2.',
                  order = {'QED':1})

GC_178 = Coupling(name = 'GC_178',
                  value = '-((complex(0,1)*UTL3x2*yR4*complexconjugate(UTR4x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2)) + (complex(0,1)*UTL3x3*yR4*complexconjugate(UTR4x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTL3x1*yL1*complexconjugate(UTR4x4)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + complex(0,1)*UTL3x4*yR1*complexconjugate(UTR4x1)*cmath.sqrt(xi) + (complex(0,1)*UTL3x1*yL4*complexconjugate(UTR4x2)*cmath.sqrt(xi))/2. - (complex(0,1)*UTL3x1*yL4*complexconjugate(UTR4x3)*cmath.sqrt(xi))/2.',
                  order = {'QED':1})

GC_179 = Coupling(name = 'GC_179',
                  value = '-((complex(0,1)*UTL4x2*yR4*complexconjugate(UTR4x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2)) + (complex(0,1)*UTL4x3*yR4*complexconjugate(UTR4x1)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + (complex(0,1)*UTL4x1*yL1*complexconjugate(UTR4x4)*cmath.sqrt(1 - xi))/cmath.sqrt(2) + complex(0,1)*UTL4x4*yR1*complexconjugate(UTR4x1)*cmath.sqrt(xi) + (complex(0,1)*UTL4x1*yL4*complexconjugate(UTR4x2)*cmath.sqrt(xi))/2. - (complex(0,1)*UTL4x1*yL4*complexconjugate(UTR4x3)*cmath.sqrt(xi))/2.',
                  order = {'QED':1})

GC_180 = Coupling(name = 'GC_180',
                  value = '(complex(0,1)*UTL1x4*yR1*complexconjugate(UTR4x1)*cmath.sqrt(1 - xi))/fs + (complex(0,1)*UTL1x1*yL4*complexconjugate(UTR4x2)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTL1x1*yL4*complexconjugate(UTR4x3)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTL1x2*yR4*complexconjugate(UTR4x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL1x3*yR4*complexconjugate(UTR4x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL1x1*yL1*complexconjugate(UTR4x4)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                  order = {'QED':1})

GC_181 = Coupling(name = 'GC_181',
                  value = '(complex(0,1)*UTL2x4*yR1*complexconjugate(UTR4x1)*cmath.sqrt(1 - xi))/fs + (complex(0,1)*UTL2x1*yL4*complexconjugate(UTR4x2)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTL2x1*yL4*complexconjugate(UTR4x3)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTL2x2*yR4*complexconjugate(UTR4x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL2x3*yR4*complexconjugate(UTR4x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL2x1*yL1*complexconjugate(UTR4x4)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                  order = {'QED':1})

GC_182 = Coupling(name = 'GC_182',
                  value = '(complex(0,1)*UTL3x4*yR1*complexconjugate(UTR4x1)*cmath.sqrt(1 - xi))/fs + (complex(0,1)*UTL3x1*yL4*complexconjugate(UTR4x2)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTL3x1*yL4*complexconjugate(UTR4x3)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTL3x2*yR4*complexconjugate(UTR4x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL3x3*yR4*complexconjugate(UTR4x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL3x1*yL1*complexconjugate(UTR4x4)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                  order = {'QED':1})

GC_183 = Coupling(name = 'GC_183',
                  value = '(complex(0,1)*UTL4x4*yR1*complexconjugate(UTR4x1)*cmath.sqrt(1 - xi))/fs + (complex(0,1)*UTL4x1*yL4*complexconjugate(UTR4x2)*cmath.sqrt(1 - xi))/(2.*fs) - (complex(0,1)*UTL4x1*yL4*complexconjugate(UTR4x3)*cmath.sqrt(1 - xi))/(2.*fs) + (complex(0,1)*UTL4x2*yR4*complexconjugate(UTR4x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL4x3*yR4*complexconjugate(UTR4x1)*cmath.sqrt(xi))/(fs*cmath.sqrt(2)) - (complex(0,1)*UTL4x1*yL1*complexconjugate(UTR4x4)*cmath.sqrt(xi))/(fs*cmath.sqrt(2))',
                  order = {'QED':1})

