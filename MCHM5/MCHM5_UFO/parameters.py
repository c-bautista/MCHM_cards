# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 10.4.1 for Linux x86 (64-bit) (April 11, 2016)
# Date: Mon 3 Feb 2020 13:54:27



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00255,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 2.8,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 150,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

M4 = Parameter(name = 'M4',
               nature = 'external',
               type = 'real',
               value = 2802.87,
               texname = '\\text{M4}',
               lhablock = 'FRBlock',
               lhacode = [ 1 ])

M1 = Parameter(name = 'M1',
               nature = 'external',
               type = 'real',
               value = 998.06,
               texname = '\\text{M1}',
               lhablock = 'FRBlock',
               lhacode = [ 2 ])

yL1 = Parameter(name = 'yL1',
                nature = 'external',
                type = 'real',
                value = 2.369,
                texname = '\\text{yL1}',
                lhablock = 'FRBlock',
                lhacode = [ 3 ])

yL4 = Parameter(name = 'yL4',
                nature = 'external',
                type = 'real',
                value = 2.369,
                texname = '\\text{yL4}',
                lhablock = 'FRBlock',
                lhacode = [ 4 ])

yR1 = Parameter(name = 'yR1',
                nature = 'external',
                type = 'real',
                value = 1.6819,
                texname = '\\text{yR1}',
                lhablock = 'FRBlock',
                lhacode = [ 5 ])

yR4 = Parameter(name = 'yR4',
                nature = 'external',
                type = 'real',
                value = 1.6819,
                texname = '\\text{yR4}',
                lhablock = 'FRBlock',
                lhacode = [ 6 ])

fs = Parameter(name = 'fs',
               nature = 'external',
               type = 'real',
               value = 1535.8,
               texname = '\\text{fs}',
               lhablock = 'FRBlock',
               lhacode = [ 7 ])

mtLS = Parameter(name = 'mtLS',
                 nature = 'external',
                 type = 'real',
                 value = 173,
                 texname = '\\text{mtLS}',
                 lhablock = 'FRBlock',
                 lhacode = [ 8 ])

mtHS = Parameter(name = 'mtHS',
                 nature = 'external',
                 type = 'real',
                 value = 150,
                 texname = '\\text{mtHS}',
                 lhablock = 'FRBlock',
                 lhacode = [ 9 ])

mbLS = Parameter(name = 'mbLS',
                 nature = 'external',
                 type = 'real',
                 value = 4.7,
                 texname = '\\text{mbLS}',
                 lhablock = 'FRBlock',
                 lhacode = [ 10 ])

mbHS = Parameter(name = 'mbHS',
                 nature = 'external',
                 type = 'real',
                 value = 2.8,
                 texname = '\\text{mbHS}',
                 lhablock = 'FRBlock',
                 lhacode = [ 11 ])

RUTL1x1 = Parameter(name = 'RUTL1x1',
                    nature = 'external',
                    type = 'real',
                    value = -0.6068339626696729,
                    texname = '\\text{RUTL1x1}',
                    lhablock = 'MIXTL',
                    lhacode = [ 1, 1 ])

RUTL1x2 = Parameter(name = 'RUTL1x2',
                    nature = 'external',
                    type = 'real',
                    value = -0.7869314849693338,
                    texname = '\\text{RUTL1x2}',
                    lhablock = 'MIXTL',
                    lhacode = [ 1, 2 ])

RUTL1x3 = Parameter(name = 'RUTL1x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.0030415159010769763,
                    texname = '\\text{RUTL1x3}',
                    lhablock = 'MIXTL',
                    lhacode = [ 1, 3 ])

RUTL1x4 = Parameter(name = 'RUTL1x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.11172344828013898,
                    texname = '\\text{RUTL1x4}',
                    lhablock = 'MIXTL',
                    lhacode = [ 1, 4 ])

RUTL2x1 = Parameter(name = 'RUTL2x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.05804577470031187,
                    texname = '\\text{RUTL2x1}',
                    lhablock = 'MIXTL',
                    lhacode = [ 2, 1 ])

RUTL2x2 = Parameter(name = 'RUTL2x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.06336311546391363,
                    texname = '\\text{RUTL2x2}',
                    lhablock = 'MIXTL',
                    lhacode = [ 2, 2 ])

RUTL2x3 = Parameter(name = 'RUTL2x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.6217246832359056,
                    texname = '\\text{RUTL2x3}',
                    lhablock = 'MIXTL',
                    lhacode = [ 2, 3 ])

RUTL2x4 = Parameter(name = 'RUTL2x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.7785076890393313,
                    texname = '\\text{RUTL2x4}',
                    lhablock = 'MIXTL',
                    lhacode = [ 2, 4 ])

RUTL3x1 = Parameter(name = 'RUTL3x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.04900861790192012,
                    texname = '\\text{RUTL3x1}',
                    lhablock = 'MIXTL',
                    lhacode = [ 3, 1 ])

RUTL3x2 = Parameter(name = 'RUTL3x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.05290841810402719,
                    texname = '\\text{RUTL3x2}',
                    lhablock = 'MIXTL',
                    lhacode = [ 3, 2 ])

RUTL3x3 = Parameter(name = 'RUTL3x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.7832297509428008,
                    texname = '\\text{RUTL3x3}',
                    lhablock = 'MIXTL',
                    lhacode = [ 3, 3 ])

RUTL3x4 = Parameter(name = 'RUTL3x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.6175354337227552,
                    texname = '\\text{RUTL3x4}',
                    lhablock = 'MIXTL',
                    lhacode = [ 3, 4 ])

RUTL4x1 = Parameter(name = 'RUTL4x1',
                    nature = 'external',
                    type = 'real',
                    value = -0.7911898540561594,
                    texname = '\\text{RUTL4x1}',
                    lhablock = 'MIXTL',
                    lhacode = [ 4, 1 ])

RUTL4x2 = Parameter(name = 'RUTL4x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.6114937880767032,
                    texname = '\\text{RUTL4x2}',
                    lhablock = 'MIXTL',
                    lhacode = [ 4, 2 ])

RUTL4x3 = Parameter(name = 'RUTL4x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.0005698019957574852,
                    texname = '\\text{RUTL4x3}',
                    lhablock = 'MIXTL',
                    lhacode = [ 4, 3 ])

RUTL4x4 = Parameter(name = 'RUTL4x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.009676637219809558,
                    texname = '\\text{RUTL4x4}',
                    lhablock = 'MIXTL',
                    lhacode = [ 4, 4 ])

IUTL1x1 = Parameter(name = 'IUTL1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL1x1}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 1, 1 ])

IUTL1x2 = Parameter(name = 'IUTL1x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL1x2}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 1, 2 ])

IUTL1x3 = Parameter(name = 'IUTL1x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL1x3}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 1, 3 ])

IUTL1x4 = Parameter(name = 'IUTL1x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL1x4}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 1, 4 ])

IUTL2x1 = Parameter(name = 'IUTL2x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL2x1}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 2, 1 ])

IUTL2x2 = Parameter(name = 'IUTL2x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL2x2}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 2, 2 ])

IUTL2x3 = Parameter(name = 'IUTL2x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL2x3}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 2, 3 ])

IUTL2x4 = Parameter(name = 'IUTL2x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL2x4}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 2, 4 ])

IUTL3x1 = Parameter(name = 'IUTL3x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL3x1}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 3, 1 ])

IUTL3x2 = Parameter(name = 'IUTL3x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL3x2}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 3, 2 ])

IUTL3x3 = Parameter(name = 'IUTL3x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL3x3}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 3, 3 ])

IUTL3x4 = Parameter(name = 'IUTL3x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL3x4}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 3, 4 ])

IUTL4x1 = Parameter(name = 'IUTL4x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL4x1}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 4, 1 ])

IUTL4x2 = Parameter(name = 'IUTL4x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL4x2}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 4, 2 ])

IUTL4x3 = Parameter(name = 'IUTL4x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL4x3}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 4, 3 ])

IUTL4x4 = Parameter(name = 'IUTL4x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL4x4}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 4, 4 ])

RUTR1x1 = Parameter(name = 'RUTR1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.36875314468966625,
                    texname = '\\text{RUTR1x1}',
                    lhablock = 'MIXTR',
                    lhacode = [ 1, 1 ])

RUTR1x2 = Parameter(name = 'RUTR1x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.0806385730997745,
                    texname = '\\text{RUTR1x2}',
                    lhablock = 'MIXTR',
                    lhacode = [ 1, 2 ])

RUTR1x3 = Parameter(name = 'RUTR1x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.03836215258087133,
                    texname = '\\text{RUTR1x3}',
                    lhablock = 'MIXTR',
                    lhacode = [ 1, 3 ])

RUTR1x4 = Parameter(name = 'RUTR1x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.9252280173337147,
                    texname = '\\text{RUTR1x4}',
                    lhablock = 'MIXTR',
                    lhacode = [ 1, 4 ])

RUTR2x1 = Parameter(name = 'RUTR2x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.6888230094172278,
                    texname = '\\text{RUTR2x1}',
                    lhablock = 'MIXTR',
                    lhacode = [ 2, 1 ])

RUTR2x2 = Parameter(name = 'RUTR2x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.012186482881527395,
                    texname = '\\text{RUTR2x2}',
                    lhablock = 'MIXTR',
                    lhacode = [ 2, 2 ])

RUTR2x3 = Parameter(name = 'RUTR2x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.6585035980266212,
                    texname = '\\text{RUTR2x3}',
                    lhablock = 'MIXTR',
                    lhacode = [ 2, 3 ])

RUTR2x4 = Parameter(name = 'RUTR2x4',
                    nature = 'external',
                    type = 'real',
                    value = -0.30289827123700475,
                    texname = '\\text{RUTR2x4}',
                    lhablock = 'MIXTR',
                    lhacode = [ 2, 4 ])

RUTR3x1 = Parameter(name = 'RUTR3x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.6225512959987762,
                    texname = '\\text{RUTR3x1}',
                    lhablock = 'MIXTR',
                    lhacode = [ 3, 1 ])

RUTR3x2 = Parameter(name = 'RUTR3x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.00987543036423026,
                    texname = '\\text{RUTR3x2}',
                    lhablock = 'MIXTR',
                    lhacode = [ 3, 2 ])

RUTR3x3 = Parameter(name = 'RUTR3x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.7515900499139904,
                    texname = '\\text{RUTR3x3}',
                    lhablock = 'MIXTR',
                    lhacode = [ 3, 3 ])

RUTR3x4 = Parameter(name = 'RUTR3x4',
                    nature = 'external',
                    type = 'real',
                    value = -0.21781817324468183,
                    texname = '\\text{RUTR3x4}',
                    lhablock = 'MIXTR',
                    lhacode = [ 3, 4 ])

RUTR4x1 = Parameter(name = 'RUTR4x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.04442818732651099,
                    texname = '\\text{RUTR4x1}',
                    lhablock = 'MIXTR',
                    lhacode = [ 4, 1 ])

RUTR4x2 = Parameter(name = 'RUTR4x2',
                    nature = 'external',
                    type = 'real',
                    value = -0.9966199807542149,
                    texname = '\\text{RUTR4x2}',
                    lhablock = 'MIXTR',
                    lhacode = [ 4, 2 ])

RUTR4x3 = Parameter(name = 'RUTR4x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.003708571914002633,
                    texname = '\\text{RUTR4x3}',
                    lhablock = 'MIXTR',
                    lhacode = [ 4, 3 ])

RUTR4x4 = Parameter(name = 'RUTR4x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.06899997555584585,
                    texname = '\\text{RUTR4x4}',
                    lhablock = 'MIXTR',
                    lhacode = [ 4, 4 ])

IUTR1x1 = Parameter(name = 'IUTR1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR1x1}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 1, 1 ])

IUTR1x2 = Parameter(name = 'IUTR1x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR1x2}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 1, 2 ])

IUTR1x3 = Parameter(name = 'IUTR1x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR1x3}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 1, 3 ])

IUTR1x4 = Parameter(name = 'IUTR1x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR1x4}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 1, 4 ])

IUTR2x1 = Parameter(name = 'IUTR2x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR2x1}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 2, 1 ])

IUTR2x2 = Parameter(name = 'IUTR2x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR2x2}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 2, 2 ])

IUTR2x3 = Parameter(name = 'IUTR2x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR2x3}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 2, 3 ])

IUTR2x4 = Parameter(name = 'IUTR2x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR2x4}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 2, 4 ])

IUTR3x1 = Parameter(name = 'IUTR3x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR3x1}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 3, 1 ])

IUTR3x2 = Parameter(name = 'IUTR3x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR3x2}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 3, 2 ])

IUTR3x3 = Parameter(name = 'IUTR3x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR3x3}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 3, 3 ])

IUTR3x4 = Parameter(name = 'IUTR3x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR3x4}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 3, 4 ])

IUTR4x1 = Parameter(name = 'IUTR4x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR4x1}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 4, 1 ])

IUTR4x2 = Parameter(name = 'IUTR4x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR4x2}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 4, 2 ])

IUTR4x3 = Parameter(name = 'IUTR4x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR4x3}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 4, 3 ])

IUTR4x4 = Parameter(name = 'IUTR4x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR4x4}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 4, 4 ])

RUBL1x1 = Parameter(name = 'RUBL1x1',
                    nature = 'external',
                    type = 'real',
                    value = -0.6102799284894173,
                    texname = '\\text{RUBL1x1}',
                    lhablock = 'MIXBL',
                    lhacode = [ 1, 1 ])

RUBL1x2 = Parameter(name = 'RUBL1x2',
                    nature = 'external',
                    type = 'real',
                    value = -0.7921858423898724,
                    texname = '\\text{RUBL1x2}',
                    lhablock = 'MIXBL',
                    lhacode = [ 1, 2 ])

RUBL2x1 = Parameter(name = 'RUBL2x1',
                    nature = 'external',
                    type = 'real',
                    value = -0.7921858423898724,
                    texname = '\\text{RUBL2x1}',
                    lhablock = 'MIXBL',
                    lhacode = [ 2, 1 ])

RUBL2x2 = Parameter(name = 'RUBL2x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.6102799284894173,
                    texname = '\\text{RUBL2x2}',
                    lhablock = 'MIXBL',
                    lhacode = [ 2, 2 ])

IUBL1x1 = Parameter(name = 'IUBL1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBL1x1}',
                    lhablock = 'IMMIXBL',
                    lhacode = [ 1, 1 ])

IUBL1x2 = Parameter(name = 'IUBL1x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBL1x2}',
                    lhablock = 'IMMIXBL',
                    lhacode = [ 1, 2 ])

IUBL2x1 = Parameter(name = 'IUBL2x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBL2x1}',
                    lhablock = 'IMMIXBL',
                    lhacode = [ 2, 1 ])

IUBL2x2 = Parameter(name = 'IUBL2x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBL2x2}',
                    lhablock = 'IMMIXBL',
                    lhacode = [ 2, 2 ])

RUBR1x1 = Parameter(name = 'RUBR1x1',
                    nature = 'external',
                    type = 'real',
                    value = -0.9999991177043163,
                    texname = '\\text{RUBR1x1}',
                    lhablock = 'MIXBR',
                    lhacode = [ 1, 1 ])

RUBR1x2 = Parameter(name = 'RUBR1x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.001328378932748479,
                    texname = '\\text{RUBR1x2}',
                    lhablock = 'MIXBR',
                    lhacode = [ 1, 2 ])

RUBR2x1 = Parameter(name = 'RUBR2x1',
                    nature = 'external',
                    type = 'real',
                    value = -0.0013283789327482724,
                    texname = '\\text{RUBR2x1}',
                    lhablock = 'MIXBR',
                    lhacode = [ 2, 1 ])

RUBR2x2 = Parameter(name = 'RUBR2x2',
                    nature = 'external',
                    type = 'real',
                    value = -0.9999991177043162,
                    texname = '\\text{RUBR2x2}',
                    lhablock = 'MIXBR',
                    lhacode = [ 2, 2 ])

IUBR1x1 = Parameter(name = 'IUBR1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBR1x1}',
                    lhablock = 'IMMIXBR',
                    lhacode = [ 1, 1 ])

IUBR1x2 = Parameter(name = 'IUBR1x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBR1x2}',
                    lhablock = 'IMMIXBR',
                    lhacode = [ 1, 2 ])

IUBR2x1 = Parameter(name = 'IUBR2x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBR2x1}',
                    lhablock = 'IMMIXBR',
                    lhacode = [ 2, 1 ])

IUBR2x2 = Parameter(name = 'IUBR2x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBR2x2}',
                    lhablock = 'IMMIXBR',
                    lhacode = [ 2, 2 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MW = Parameter(name = 'MW',
               nature = 'external',
               type = 'real',
               value = 79.8244,
               texname = '\\text{MW}',
               lhablock = 'MASS',
               lhacode = [ 24 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00255,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 173,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MT4 = Parameter(name = 'MT4',
                nature = 'external',
                type = 'real',
                value = 2644.2491837757575,
                texname = '\\text{MT4}',
                lhablock = 'MASS',
                lhacode = [ 9000 ])

MX23 = Parameter(name = 'MX23',
                 nature = 'external',
                 type = 'real',
                 value = 2922.3968337490487,
                 texname = '\\text{MX23}',
                 lhablock = 'MASS',
                 lhacode = [ 9001 ])

MT1 = Parameter(name = 'MT1',
                nature = 'external',
                type = 'real',
                value = 4589.426760607948,
                texname = '\\text{MT1}',
                lhablock = 'MASS',
                lhacode = [ 9002 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.700000000000474,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MB4 = Parameter(name = 'MB4',
                nature = 'external',
                type = 'real',
                value = 4592.75718599764,
                texname = '\\text{MB4}',
                lhablock = 'MASS',
                lhacode = [ 10000 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WT4 = Parameter(name = 'WT4',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WT4}',
                lhablock = 'DECAY',
                lhacode = [ 9000 ])

WX23 = Parameter(name = 'WX23',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WX23}',
                 lhablock = 'DECAY',
                 lhacode = [ 9001 ])

WT1 = Parameter(name = 'WT1',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WT1}',
                lhablock = 'DECAY',
                lhacode = [ 9002 ])

Wb = Parameter(name = 'Wb',
               nature = 'external',
               type = 'real',
               value = 1,
               texname = '\\text{Wb}',
               lhablock = 'DECAY',
               lhacode = [ 5 ])

WB4 = Parameter(name = 'WB4',
                nature = 'external',
                type = 'real',
                value = 1,
                texname = '\\text{WB4}',
                lhablock = 'DECAY',
                lhacode = [ 10000 ])

WX53 = Parameter(name = 'WX53',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WX53}',
                 lhablock = 'DECAY',
                 lhacode = [ 11000 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '0.23369836056172644',
                texname = '\\text{sw2}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MX53 = Parameter(name = 'MX53',
                 nature = 'internal',
                 type = 'real',
                 value = 'M4',
                 texname = '\\text{MX53}')

cb = Parameter(name = 'cb',
               nature = 'internal',
               type = 'real',
               value = '(MB*cmath.sqrt(M4**2 - MB**2 + fs**2*yL4**2))/cmath.sqrt(M4**2 - MB**2)',
               texname = '\\text{cb}')

MT51x1 = Parameter(name = 'MT51x1',
                   nature = 'internal',
                   type = 'real',
                   value = '0',
                   texname = '\\text{MT51x1}')

MT52x2 = Parameter(name = 'MT52x2',
                   nature = 'internal',
                   type = 'real',
                   value = '-M4',
                   texname = '\\text{MT52x2}')

MT52x3 = Parameter(name = 'MT52x3',
                   nature = 'internal',
                   type = 'real',
                   value = '0',
                   texname = '\\text{MT52x3}')

MT52x4 = Parameter(name = 'MT52x4',
                   nature = 'internal',
                   type = 'real',
                   value = '0',
                   texname = '\\text{MT52x4}')

MT53x2 = Parameter(name = 'MT53x2',
                   nature = 'internal',
                   type = 'real',
                   value = '0',
                   texname = '\\text{MT53x2}')

MT53x3 = Parameter(name = 'MT53x3',
                   nature = 'internal',
                   type = 'real',
                   value = '-M4',
                   texname = '\\text{MT53x3}')

MT53x4 = Parameter(name = 'MT53x4',
                   nature = 'internal',
                   type = 'real',
                   value = '0',
                   texname = '\\text{MT53x4}')

MT54x2 = Parameter(name = 'MT54x2',
                   nature = 'internal',
                   type = 'real',
                   value = '0',
                   texname = '\\text{MT54x2}')

MT54x3 = Parameter(name = 'MT54x3',
                   nature = 'internal',
                   type = 'real',
                   value = '0',
                   texname = '\\text{MT54x3}')

MT54x4 = Parameter(name = 'MT54x4',
                   nature = 'internal',
                   type = 'real',
                   value = '-M1',
                   texname = '\\text{MT54x4}')

MB51x2 = Parameter(name = 'MB51x2',
                   nature = 'internal',
                   type = 'real',
                   value = 'fs*yL4',
                   texname = '\\text{MB51x2}')

MB52x1 = Parameter(name = 'MB52x1',
                   nature = 'internal',
                   type = 'real',
                   value = '0',
                   texname = '\\text{MB52x1}')

MB52x2 = Parameter(name = 'MB52x2',
                   nature = 'internal',
                   type = 'real',
                   value = '-M4',
                   texname = '\\text{MB52x2}')

UTL1x1 = Parameter(name = 'UTL1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL1x1 + RUTL1x1',
                   texname = '\\text{UTL1x1}')

UTL1x2 = Parameter(name = 'UTL1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL1x2 + RUTL1x2',
                   texname = '\\text{UTL1x2}')

UTL1x3 = Parameter(name = 'UTL1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL1x3 + RUTL1x3',
                   texname = '\\text{UTL1x3}')

UTL1x4 = Parameter(name = 'UTL1x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL1x4 + RUTL1x4',
                   texname = '\\text{UTL1x4}')

UTL2x1 = Parameter(name = 'UTL2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL2x1 + RUTL2x1',
                   texname = '\\text{UTL2x1}')

UTL2x2 = Parameter(name = 'UTL2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL2x2 + RUTL2x2',
                   texname = '\\text{UTL2x2}')

UTL2x3 = Parameter(name = 'UTL2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL2x3 + RUTL2x3',
                   texname = '\\text{UTL2x3}')

UTL2x4 = Parameter(name = 'UTL2x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL2x4 + RUTL2x4',
                   texname = '\\text{UTL2x4}')

UTL3x1 = Parameter(name = 'UTL3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL3x1 + RUTL3x1',
                   texname = '\\text{UTL3x1}')

UTL3x2 = Parameter(name = 'UTL3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL3x2 + RUTL3x2',
                   texname = '\\text{UTL3x2}')

UTL3x3 = Parameter(name = 'UTL3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL3x3 + RUTL3x3',
                   texname = '\\text{UTL3x3}')

UTL3x4 = Parameter(name = 'UTL3x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL3x4 + RUTL3x4',
                   texname = '\\text{UTL3x4}')

UTL4x1 = Parameter(name = 'UTL4x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL4x1 + RUTL4x1',
                   texname = '\\text{UTL4x1}')

UTL4x2 = Parameter(name = 'UTL4x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL4x2 + RUTL4x2',
                   texname = '\\text{UTL4x2}')

UTL4x3 = Parameter(name = 'UTL4x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL4x3 + RUTL4x3',
                   texname = '\\text{UTL4x3}')

UTL4x4 = Parameter(name = 'UTL4x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL4x4 + RUTL4x4',
                   texname = '\\text{UTL4x4}')

UTR1x1 = Parameter(name = 'UTR1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR1x1 + RUTR1x1',
                   texname = '\\text{UTR1x1}')

UTR1x2 = Parameter(name = 'UTR1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR1x2 + RUTR1x2',
                   texname = '\\text{UTR1x2}')

UTR1x3 = Parameter(name = 'UTR1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR1x3 + RUTR1x3',
                   texname = '\\text{UTR1x3}')

UTR1x4 = Parameter(name = 'UTR1x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR1x4 + RUTR1x4',
                   texname = '\\text{UTR1x4}')

UTR2x1 = Parameter(name = 'UTR2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR2x1 + RUTR2x1',
                   texname = '\\text{UTR2x1}')

UTR2x2 = Parameter(name = 'UTR2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR2x2 + RUTR2x2',
                   texname = '\\text{UTR2x2}')

UTR2x3 = Parameter(name = 'UTR2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR2x3 + RUTR2x3',
                   texname = '\\text{UTR2x3}')

UTR2x4 = Parameter(name = 'UTR2x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR2x4 + RUTR2x4',
                   texname = '\\text{UTR2x4}')

UTR3x1 = Parameter(name = 'UTR3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR3x1 + RUTR3x1',
                   texname = '\\text{UTR3x1}')

UTR3x2 = Parameter(name = 'UTR3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR3x2 + RUTR3x2',
                   texname = '\\text{UTR3x2}')

UTR3x3 = Parameter(name = 'UTR3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR3x3 + RUTR3x3',
                   texname = '\\text{UTR3x3}')

UTR3x4 = Parameter(name = 'UTR3x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR3x4 + RUTR3x4',
                   texname = '\\text{UTR3x4}')

UTR4x1 = Parameter(name = 'UTR4x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR4x1 + RUTR4x1',
                   texname = '\\text{UTR4x1}')

UTR4x2 = Parameter(name = 'UTR4x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR4x2 + RUTR4x2',
                   texname = '\\text{UTR4x2}')

UTR4x3 = Parameter(name = 'UTR4x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR4x3 + RUTR4x3',
                   texname = '\\text{UTR4x3}')

UTR4x4 = Parameter(name = 'UTR4x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR4x4 + RUTR4x4',
                   texname = '\\text{UTR4x4}')

UBL1x1 = Parameter(name = 'UBL1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBL1x1 + RUBL1x1',
                   texname = '\\text{UBL1x1}')

UBL1x2 = Parameter(name = 'UBL1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBL1x2 + RUBL1x2',
                   texname = '\\text{UBL1x2}')

UBL2x1 = Parameter(name = 'UBL2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBL2x1 + RUBL2x1',
                   texname = '\\text{UBL2x1}')

UBL2x2 = Parameter(name = 'UBL2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBL2x2 + RUBL2x2',
                   texname = '\\text{UBL2x2}')

UBR1x1 = Parameter(name = 'UBR1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBR1x1 + RUBR1x1',
                   texname = '\\text{UBR1x1}')

UBR1x2 = Parameter(name = 'UBR1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBR1x2 + RUBR1x2',
                   texname = '\\text{UBR1x2}')

UBR2x1 = Parameter(name = 'UBR2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBR2x1 + RUBR2x1',
                   texname = '\\text{UBR2x1}')

UBR2x2 = Parameter(name = 'UBR2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBR2x2 + RUBR2x2',
                   texname = '\\text{UBR2x2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

MB51x1 = Parameter(name = 'MB51x1',
                   nature = 'internal',
                   type = 'real',
                   value = 'cb',
                   texname = '\\text{MB51x1}')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(159.6488*sw)/ee',
                texname = '\\text{vev}')

xi = Parameter(name = 'xi',
               nature = 'internal',
               type = 'real',
               value = 'vev**2/fs**2',
               texname = '\\xi')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vev',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vev',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vev',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vev',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vev',
               texname = '\\text{ys}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vev',
                texname = '\\text{yup}')

MT51x2 = Parameter(name = 'MT51x2',
                   nature = 'internal',
                   type = 'real',
                   value = '(fs*yL4*(1 + cmath.sqrt(1 - xi)))/2.',
                   texname = '\\text{MT51x2}')

MT51x3 = Parameter(name = 'MT51x3',
                   nature = 'internal',
                   type = 'real',
                   value = '-(fs*yL4*(-1 + cmath.sqrt(1 - xi)))/2.',
                   texname = '\\text{MT51x3}')

MT51x4 = Parameter(name = 'MT51x4',
                   nature = 'internal',
                   type = 'real',
                   value = '-((fs*yL1*cmath.sqrt(xi))/cmath.sqrt(2))',
                   texname = '\\text{MT51x4}')

MT52x1 = Parameter(name = 'MT52x1',
                   nature = 'internal',
                   type = 'real',
                   value = '(fs*yR4*cmath.sqrt(xi))/cmath.sqrt(2)',
                   texname = '\\text{MT52x1}')

MT53x1 = Parameter(name = 'MT53x1',
                   nature = 'internal',
                   type = 'real',
                   value = '-((fs*yR4*cmath.sqrt(xi))/cmath.sqrt(2))',
                   texname = '\\text{MT53x1}')

MT54x1 = Parameter(name = 'MT54x1',
                   nature = 'internal',
                   type = 'real',
                   value = 'fs*yR1*cmath.sqrt(1 - xi)',
                   texname = '\\text{MT54x1}')

WH = Parameter(name = 'WH',
               nature = 'internal',
               type = 'real',
               value = '0.004088*((0.11078*(1 - 2*xi)**2)/(1 - xi) + 0.8850100000000001*(1 - xi))',
               texname = '\\text{WH}')

