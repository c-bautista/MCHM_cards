# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 10.4.1 for Linux x86 (64-bit) (April 11, 2016)
# Date: Sat 23 Nov 2019 17:03:27



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

M9 = Parameter(name = 'M9',
               nature = 'external',
               type = 'real',
               value = 2713.93,
               texname = '\\text{M9}',
               lhablock = 'FRBlock',
               lhacode = [ 1 ])

M4 = Parameter(name = 'M4',
               nature = 'external',
               type = 'real',
               value = -2511.79,
               texname = '\\text{M4}',
               lhablock = 'FRBlock',
               lhacode = [ 2 ])

M1 = Parameter(name = 'M1',
               nature = 'external',
               type = 'real',
               value = -1579.22,
               texname = '\\text{M1}',
               lhablock = 'FRBlock',
               lhacode = [ 3 ])

yL1 = Parameter(name = 'yL1',
                nature = 'external',
                type = 'real',
                value = 2.71401,
                texname = '\\text{yL1}',
                lhablock = 'FRBlock',
                lhacode = [ 4 ])

yL4 = Parameter(name = 'yL4',
                nature = 'external',
                type = 'real',
                value = 2.71401,
                texname = '\\text{yL4}',
                lhablock = 'FRBlock',
                lhacode = [ 5 ])

yL9 = Parameter(name = 'yL9',
                nature = 'external',
                type = 'real',
                value = 2.71401,
                texname = '\\text{yL9}',
                lhablock = 'FRBlock',
                lhacode = [ 6 ])

yR1 = Parameter(name = 'yR1',
                nature = 'external',
                type = 'real',
                value = 2.46322,
                texname = '\\text{yR1}',
                lhablock = 'FRBlock',
                lhacode = [ 7 ])

yR4 = Parameter(name = 'yR4',
                nature = 'external',
                type = 'real',
                value = 2.46322,
                texname = '\\text{yR4}',
                lhablock = 'FRBlock',
                lhacode = [ 8 ])

yR9 = Parameter(name = 'yR9',
                nature = 'external',
                type = 'real',
                value = 2.46322,
                texname = '\\text{yR9}',
                lhablock = 'FRBlock',
                lhacode = [ 9 ])

fs = Parameter(name = 'fs',
               nature = 'external',
               type = 'real',
               value = 1298.33,
               texname = '\\text{fs}',
               lhablock = 'FRBlock',
               lhacode = [ 10 ])

mtLS = Parameter(name = 'mtLS',
                 nature = 'external',
                 type = 'real',
                 value = 173,
                 texname = '\\text{mtLS}',
                 lhablock = 'FRBlock',
                 lhacode = [ 11 ])

mtHS = Parameter(name = 'mtHS',
                 nature = 'external',
                 type = 'real',
                 value = 150,
                 texname = '\\text{mtHS}',
                 lhablock = 'FRBlock',
                 lhacode = [ 12 ])

mbLS = Parameter(name = 'mbLS',
                 nature = 'external',
                 type = 'real',
                 value = 4.7,
                 texname = '\\text{mbLS}',
                 lhablock = 'FRBlock',
                 lhacode = [ 13 ])

mbHS = Parameter(name = 'mbHS',
                 nature = 'external',
                 type = 'real',
                 value = 2.8,
                 texname = '\\text{mbHS}',
                 lhablock = 'FRBlock',
                 lhacode = [ 14 ])

RUTL1x1 = Parameter(name = 'RUTL1x1',
                    nature = 'external',
                    type = 'real',
                    value = -0.5754728717459984,
                    texname = '\\text{RUTL1x1}',
                    lhablock = 'MIXTL',
                    lhacode = [ 1, 1 ])

RUTL1x2 = Parameter(name = 'RUTL1x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.7809575571348873,
                    texname = '\\text{RUTL1x2}',
                    lhablock = 'MIXTL',
                    lhacode = [ 1, 2 ])

RUTL1x3 = Parameter(name = 'RUTL1x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.014534939005077257,
                    texname = '\\text{RUTL1x3}',
                    lhablock = 'MIXTL',
                    lhacode = [ 1, 3 ])

RUTL1x4 = Parameter(name = 'RUTL1x4',
                    nature = 'external',
                    type = 'real',
                    value = -0.18511665805037034,
                    texname = '\\text{RUTL1x4}',
                    lhablock = 'MIXTL',
                    lhacode = [ 1, 4 ])

RUTL1x5 = Parameter(name = 'RUTL1x5',
                    nature = 'external',
                    type = 'real',
                    value = -0.0018892592175551103,
                    texname = '\\text{RUTL1x5}',
                    lhablock = 'MIXTL',
                    lhacode = [ 1, 5 ])

RUTL1x6 = Parameter(name = 'RUTL1x6',
                    nature = 'external',
                    type = 'real',
                    value = -0.06917646793410785,
                    texname = '\\text{RUTL1x6}',
                    lhablock = 'MIXTL',
                    lhacode = [ 1, 6 ])

RUTL1x7 = Parameter(name = 'RUTL1x7',
                    nature = 'external',
                    type = 'real',
                    value = 0.14024219508577082,
                    texname = '\\text{RUTL1x7}',
                    lhablock = 'MIXTL',
                    lhacode = [ 1, 7 ])

RUTL2x1 = Parameter(name = 'RUTL2x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.02932643208602863,
                    texname = '\\text{RUTL2x1}',
                    lhablock = 'MIXTL',
                    lhacode = [ 2, 1 ])

RUTL2x2 = Parameter(name = 'RUTL2x2',
                    nature = 'external',
                    type = 'real',
                    value = -0.0234750624144605,
                    texname = '\\text{RUTL2x2}',
                    lhablock = 'MIXTL',
                    lhacode = [ 2, 2 ])

RUTL2x3 = Parameter(name = 'RUTL2x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.9434215905877995,
                    texname = '\\text{RUTL2x3}',
                    lhablock = 'MIXTL',
                    lhacode = [ 2, 3 ])

RUTL2x4 = Parameter(name = 'RUTL2x4',
                    nature = 'external',
                    type = 'real',
                    value = -0.32174802163668326,
                    texname = '\\text{RUTL2x4}',
                    lhablock = 'MIXTL',
                    lhacode = [ 2, 4 ])

RUTL2x5 = Parameter(name = 'RUTL2x5',
                    nature = 'external',
                    type = 'real',
                    value = -0.01731782105033212,
                    texname = '\\text{RUTL2x5}',
                    lhablock = 'MIXTL',
                    lhacode = [ 2, 5 ])

RUTL2x6 = Parameter(name = 'RUTL2x6',
                    nature = 'external',
                    type = 'real',
                    value = 0.03746532253926969,
                    texname = '\\text{RUTL2x6}',
                    lhablock = 'MIXTL',
                    lhacode = [ 2, 6 ])

RUTL2x7 = Parameter(name = 'RUTL2x7',
                    nature = 'external',
                    type = 'real',
                    value = -0.05761282402820701,
                    texname = '\\text{RUTL2x7}',
                    lhablock = 'MIXTL',
                    lhacode = [ 2, 7 ])

RUTL3x1 = Parameter(name = 'RUTL3x1',
                    nature = 'external',
                    type = 'real',
                    value = -0.03293493337395816,
                    texname = '\\text{RUTL3x1}',
                    lhablock = 'MIXTL',
                    lhacode = [ 3, 1 ])

RUTL3x2 = Parameter(name = 'RUTL3x2',
                    nature = 'external',
                    type = 'real',
                    value = -0.1928948155522064,
                    texname = '\\text{RUTL3x2}',
                    lhablock = 'MIXTL',
                    lhacode = [ 3, 2 ])

RUTL3x3 = Parameter(name = 'RUTL3x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.1004305893820719,
                    texname = '\\text{RUTL3x3}',
                    lhablock = 'MIXTL',
                    lhacode = [ 3, 3 ])

RUTL3x4 = Parameter(name = 'RUTL3x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.09429299149598902,
                    texname = '\\text{RUTL3x4}',
                    lhablock = 'MIXTL',
                    lhacode = [ 3, 4 ])

RUTL3x5 = Parameter(name = 'RUTL3x5',
                    nature = 'external',
                    type = 'real',
                    value = 0.10131375979835516,
                    texname = '\\text{RUTL3x5}',
                    lhablock = 'MIXTL',
                    lhacode = [ 3, 5 ])

RUTL3x6 = Parameter(name = 'RUTL3x6',
                    nature = 'external',
                    type = 'real',
                    value = -0.4718982047844593,
                    texname = '\\text{RUTL3x6}',
                    lhablock = 'MIXTL',
                    lhacode = [ 3, 6 ])

RUTL3x7 = Parameter(name = 'RUTL3x7',
                    nature = 'external',
                    type = 'real',
                    value = 0.8424826497706439,
                    texname = '\\text{RUTL3x7}',
                    lhablock = 'MIXTL',
                    lhacode = [ 3, 7 ])

RUTL4x1 = Parameter(name = 'RUTL4x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.0014412527262182505,
                    texname = '\\text{RUTL4x1}',
                    lhablock = 'MIXTL',
                    lhacode = [ 4, 1 ])

RUTL4x2 = Parameter(name = 'RUTL4x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.03091739472220212,
                    texname = '\\text{RUTL4x2}',
                    lhablock = 'MIXTL',
                    lhacode = [ 4, 2 ])

RUTL4x3 = Parameter(name = 'RUTL4x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.019035825066492103,
                    texname = '\\text{RUTL4x3}',
                    lhablock = 'MIXTL',
                    lhacode = [ 4, 3 ])

RUTL4x4 = Parameter(name = 'RUTL4x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.018885561651769387,
                    texname = '\\text{RUTL4x4}',
                    lhablock = 'MIXTL',
                    lhacode = [ 4, 4 ])

RUTL4x5 = Parameter(name = 'RUTL4x5',
                    nature = 'external',
                    type = 'real',
                    value = 0.9063735560098464,
                    texname = '\\text{RUTL4x5}',
                    lhablock = 'MIXTL',
                    lhacode = [ 4, 5 ])

RUTL4x6 = Parameter(name = 'RUTL4x6',
                    nature = 'external',
                    type = 'real',
                    value = -0.3125346590242277,
                    texname = '\\text{RUTL4x6}',
                    lhablock = 'MIXTL',
                    lhacode = [ 4, 6 ])

RUTL4x7 = Parameter(name = 'RUTL4x7',
                    nature = 'external',
                    type = 'real',
                    value = -0.2813042379595115,
                    texname = '\\text{RUTL4x7}',
                    lhablock = 'MIXTL',
                    lhacode = [ 4, 7 ])

RUTL5x1 = Parameter(name = 'RUTL5x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUTL5x1}',
                    lhablock = 'MIXTL',
                    lhacode = [ 5, 1 ])

RUTL5x2 = Parameter(name = 'RUTL5x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.7410241481987496e-14,
                    texname = '\\text{RUTL5x2}',
                    lhablock = 'MIXTL',
                    lhacode = [ 5, 2 ])

RUTL5x3 = Parameter(name = 'RUTL5x3',
                    nature = 'external',
                    type = 'real',
                    value = -1.8258743775088806e-14,
                    texname = '\\text{RUTL5x3}',
                    lhablock = 'MIXTL',
                    lhacode = [ 5, 3 ])

RUTL5x4 = Parameter(name = 'RUTL5x4',
                    nature = 'external',
                    type = 'real',
                    value = 1.781006871787875e-14,
                    texname = '\\text{RUTL5x4}',
                    lhablock = 'MIXTL',
                    lhacode = [ 5, 4 ])

RUTL5x5 = Parameter(name = 'RUTL5x5',
                    nature = 'external',
                    type = 'real',
                    value = -0.408248290463164,
                    texname = '\\text{RUTL5x5}',
                    lhablock = 'MIXTL',
                    lhacode = [ 5, 5 ])

RUTL5x6 = Parameter(name = 'RUTL5x6',
                    nature = 'external',
                    type = 'real',
                    value = -0.8164965809279814,
                    texname = '\\text{RUTL5x6}',
                    lhablock = 'MIXTL',
                    lhacode = [ 5, 6 ])

RUTL5x7 = Parameter(name = 'RUTL5x7',
                    nature = 'external',
                    type = 'real',
                    value = -0.4082482904640511,
                    texname = '\\text{RUTL5x7}',
                    lhablock = 'MIXTL',
                    lhacode = [ 5, 7 ])

RUTL6x1 = Parameter(name = 'RUTL6x1',
                    nature = 'external',
                    type = 'real',
                    value = -0.12939286395254934,
                    texname = '\\text{RUTL6x1}',
                    lhablock = 'MIXTL',
                    lhacode = [ 6, 1 ])

RUTL6x2 = Parameter(name = 'RUTL6x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.14791116931136655,
                    texname = '\\text{RUTL6x2}',
                    lhablock = 'MIXTL',
                    lhacode = [ 6, 2 ])

RUTL6x3 = Parameter(name = 'RUTL6x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.31495601501665893,
                    texname = '\\text{RUTL6x3}',
                    lhablock = 'MIXTL',
                    lhacode = [ 6, 3 ])

RUTL6x4 = Parameter(name = 'RUTL6x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.9230214241938154,
                    texname = '\\text{RUTL6x4}',
                    lhablock = 'MIXTL',
                    lhacode = [ 6, 4 ])

RUTL6x5 = Parameter(name = 'RUTL6x5',
                    nature = 'external',
                    type = 'real',
                    value = -0.035179069605664776,
                    texname = '\\text{RUTL6x5}',
                    lhablock = 'MIXTL',
                    lhacode = [ 6, 5 ])

RUTL6x6 = Parameter(name = 'RUTL6x6',
                    nature = 'external',
                    type = 'real',
                    value = 0.05585404402219653,
                    texname = '\\text{RUTL6x6}',
                    lhablock = 'MIXTL',
                    lhacode = [ 6, 6 ])

RUTL6x7 = Parameter(name = 'RUTL6x7',
                    nature = 'external',
                    type = 'real',
                    value = -0.07652901843872753,
                    texname = '\\text{RUTL6x7}',
                    lhablock = 'MIXTL',
                    lhacode = [ 6, 7 ])

RUTL7x1 = Parameter(name = 'RUTL7x1',
                    nature = 'external',
                    type = 'real',
                    value = -0.8063136077097466,
                    texname = '\\text{RUTL7x1}',
                    lhablock = 'MIXTL',
                    lhacode = [ 7, 1 ])

RUTL7x2 = Parameter(name = 'RUTL7x2',
                    nature = 'external',
                    type = 'real',
                    value = -0.5740315376598777,
                    texname = '\\text{RUTL7x2}',
                    lhablock = 'MIXTL',
                    lhacode = [ 7, 2 ])

RUTL7x3 = Parameter(name = 'RUTL7x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.009923741539321917,
                    texname = '\\text{RUTL7x3}',
                    lhablock = 'MIXTL',
                    lhacode = [ 7, 3 ])

RUTL7x4 = Parameter(name = 'RUTL7x4',
                    nature = 'external',
                    type = 'real',
                    value = -0.031522234695506676,
                    texname = '\\text{RUTL7x4}',
                    lhablock = 'MIXTL',
                    lhacode = [ 7, 4 ])

RUTL7x5 = Parameter(name = 'RUTL7x5',
                    nature = 'external',
                    type = 'real',
                    value = 0.00384567430345915,
                    texname = '\\text{RUTL7x5}',
                    lhablock = 'MIXTL',
                    lhacode = [ 7, 5 ])

RUTL7x6 = Parameter(name = 'RUTL7x6',
                    nature = 'external',
                    type = 'real',
                    value = 0.06048798409838865,
                    texname = '\\text{RUTL7x6}',
                    lhablock = 'MIXTL',
                    lhacode = [ 7, 6 ])

RUTL7x7 = Parameter(name = 'RUTL7x7',
                    nature = 'external',
                    type = 'real',
                    value = -0.12482164250023652,
                    texname = '\\text{RUTL7x7}',
                    lhablock = 'MIXTL',
                    lhacode = [ 7, 7 ])

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

IUTL1x5 = Parameter(name = 'IUTL1x5',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL1x5}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 1, 5 ])

IUTL1x6 = Parameter(name = 'IUTL1x6',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL1x6}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 1, 6 ])

IUTL1x7 = Parameter(name = 'IUTL1x7',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL1x7}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 1, 7 ])

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

IUTL2x5 = Parameter(name = 'IUTL2x5',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL2x5}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 2, 5 ])

IUTL2x6 = Parameter(name = 'IUTL2x6',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL2x6}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 2, 6 ])

IUTL2x7 = Parameter(name = 'IUTL2x7',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL2x7}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 2, 7 ])

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

IUTL3x5 = Parameter(name = 'IUTL3x5',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL3x5}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 3, 5 ])

IUTL3x6 = Parameter(name = 'IUTL3x6',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL3x6}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 3, 6 ])

IUTL3x7 = Parameter(name = 'IUTL3x7',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL3x7}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 3, 7 ])

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

IUTL4x5 = Parameter(name = 'IUTL4x5',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL4x5}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 4, 5 ])

IUTL4x6 = Parameter(name = 'IUTL4x6',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL4x6}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 4, 6 ])

IUTL4x7 = Parameter(name = 'IUTL4x7',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL4x7}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 4, 7 ])

IUTL5x1 = Parameter(name = 'IUTL5x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL5x1}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 5, 1 ])

IUTL5x2 = Parameter(name = 'IUTL5x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL5x2}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 5, 2 ])

IUTL5x3 = Parameter(name = 'IUTL5x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL5x3}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 5, 3 ])

IUTL5x4 = Parameter(name = 'IUTL5x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL5x4}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 5, 4 ])

IUTL5x5 = Parameter(name = 'IUTL5x5',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL5x5}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 5, 5 ])

IUTL5x6 = Parameter(name = 'IUTL5x6',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL5x6}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 5, 6 ])

IUTL5x7 = Parameter(name = 'IUTL5x7',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL5x7}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 5, 7 ])

IUTL6x1 = Parameter(name = 'IUTL6x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL6x1}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 6, 1 ])

IUTL6x2 = Parameter(name = 'IUTL6x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL6x2}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 6, 2 ])

IUTL6x3 = Parameter(name = 'IUTL6x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL6x3}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 6, 3 ])

IUTL6x4 = Parameter(name = 'IUTL6x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL6x4}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 6, 4 ])

IUTL6x5 = Parameter(name = 'IUTL6x5',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL6x5}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 6, 5 ])

IUTL6x6 = Parameter(name = 'IUTL6x6',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL6x6}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 6, 6 ])

IUTL6x7 = Parameter(name = 'IUTL6x7',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL6x7}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 6, 7 ])

IUTL7x1 = Parameter(name = 'IUTL7x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL7x1}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 7, 1 ])

IUTL7x2 = Parameter(name = 'IUTL7x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL7x2}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 7, 2 ])

IUTL7x3 = Parameter(name = 'IUTL7x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL7x3}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 7, 3 ])

IUTL7x4 = Parameter(name = 'IUTL7x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL7x4}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 7, 4 ])

IUTL7x5 = Parameter(name = 'IUTL7x5',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL7x5}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 7, 5 ])

IUTL7x6 = Parameter(name = 'IUTL7x6',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL7x6}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 7, 6 ])

IUTL7x7 = Parameter(name = 'IUTL7x7',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTL7x7}',
                    lhablock = 'IMMIXTL',
                    lhacode = [ 7, 7 ])

RUTR1x1 = Parameter(name = 'RUTR1x1',
                    nature = 'external',
                    type = 'real',
                    value = -0.45652912852432137,
                    texname = '\\text{RUTR1x1}',
                    lhablock = 'MIXTR',
                    lhacode = [ 1, 1 ])

RUTR1x2 = Parameter(name = 'RUTR1x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.16764521944288338,
                    texname = '\\text{RUTR1x2}',
                    lhablock = 'MIXTR',
                    lhacode = [ 1, 2 ])

RUTR1x3 = Parameter(name = 'RUTR1x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.1201398810449317,
                    texname = '\\text{RUTR1x3}',
                    lhablock = 'MIXTR',
                    lhacode = [ 1, 3 ])

RUTR1x4 = Parameter(name = 'RUTR1x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.8653699240939069,
                    texname = '\\text{RUTR1x4}',
                    lhablock = 'MIXTR',
                    lhacode = [ 1, 4 ])

RUTR1x5 = Parameter(name = 'RUTR1x5',
                    nature = 'external',
                    type = 'real',
                    value = 0.010920269210435492,
                    texname = '\\text{RUTR1x5}',
                    lhablock = 'MIXTR',
                    lhacode = [ 1, 5 ])

RUTR1x6 = Parameter(name = 'RUTR1x6',
                    nature = 'external',
                    type = 'real',
                    value = -0.006992452456992212,
                    texname = '\\text{RUTR1x6}',
                    lhablock = 'MIXTR',
                    lhacode = [ 1, 6 ])

RUTR1x7 = Parameter(name = 'RUTR1x7',
                    nature = 'external',
                    type = 'real',
                    value = 0.003064635703548856,
                    texname = '\\text{RUTR1x7}',
                    lhablock = 'MIXTR',
                    lhacode = [ 1, 7 ])

RUTR2x1 = Parameter(name = 'RUTR2x1',
                    nature = 'external',
                    type = 'real',
                    value = -0.1476390713940654,
                    texname = '\\text{RUTR2x1}',
                    lhablock = 'MIXTR',
                    lhacode = [ 2, 1 ])

RUTR2x2 = Parameter(name = 'RUTR2x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.01615382907505915,
                    texname = '\\text{RUTR2x2}',
                    lhablock = 'MIXTR',
                    lhacode = [ 2, 2 ])

RUTR2x3 = Parameter(name = 'RUTR2x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.9626379187543723,
                    texname = '\\text{RUTR2x3}',
                    lhablock = 'MIXTR',
                    lhacode = [ 2, 3 ])

RUTR2x4 = Parameter(name = 'RUTR2x4',
                    nature = 'external',
                    type = 'real',
                    value = -0.21540252599015633,
                    texname = '\\text{RUTR2x4}',
                    lhablock = 'MIXTR',
                    lhacode = [ 2, 4 ])

RUTR2x5 = Parameter(name = 'RUTR2x5',
                    nature = 'external',
                    type = 'real',
                    value = 0.01918736322816988,
                    texname = '\\text{RUTR2x5}',
                    lhablock = 'MIXTR',
                    lhacode = [ 2, 5 ])

RUTR2x6 = Parameter(name = 'RUTR2x6',
                    nature = 'external',
                    type = 'real',
                    value = -0.037440568712398675,
                    texname = '\\text{RUTR2x6}',
                    lhablock = 'MIXTR',
                    lhacode = [ 2, 6 ])

RUTR2x7 = Parameter(name = 'RUTR2x7',
                    nature = 'external',
                    type = 'real',
                    value = 0.055693774196627126,
                    texname = '\\text{RUTR2x7}',
                    lhablock = 'MIXTR',
                    lhacode = [ 2, 7 ])

RUTR3x1 = Parameter(name = 'RUTR3x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.05017099967195486,
                    texname = '\\text{RUTR3x1}',
                    lhablock = 'MIXTR',
                    lhacode = [ 3, 1 ])

RUTR3x2 = Parameter(name = 'RUTR3x2',
                    nature = 'external',
                    type = 'real',
                    value = -0.22057332590094836,
                    texname = '\\text{RUTR3x2}',
                    lhablock = 'MIXTR',
                    lhacode = [ 3, 2 ])

RUTR3x3 = Parameter(name = 'RUTR3x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.09461925533941805,
                    texname = '\\text{RUTR3x3}',
                    lhablock = 'MIXTR',
                    lhacode = [ 3, 3 ])

RUTR3x4 = Parameter(name = 'RUTR3x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.06412245210600027,
                    texname = '\\text{RUTR3x4}',
                    lhablock = 'MIXTR',
                    lhacode = [ 3, 4 ])

RUTR3x5 = Parameter(name = 'RUTR3x5',
                    nature = 'external',
                    type = 'real',
                    value = -0.1019465989804537,
                    texname = '\\text{RUTR3x5}',
                    lhablock = 'MIXTR',
                    lhacode = [ 3, 5 ])

RUTR3x6 = Parameter(name = 'RUTR3x6',
                    nature = 'external',
                    type = 'real',
                    value = 0.47049809586459296,
                    texname = '\\text{RUTR3x6}',
                    lhablock = 'MIXTR',
                    lhacode = [ 3, 6 ])

RUTR3x7 = Parameter(name = 'RUTR3x7',
                    nature = 'external',
                    type = 'real',
                    value = -0.8390495927488129,
                    texname = '\\text{RUTR3x7}',
                    lhablock = 'MIXTR',
                    lhacode = [ 3, 7 ])

RUTR4x1 = Parameter(name = 'RUTR4x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.01129701182344097,
                    texname = '\\text{RUTR4x1}',
                    lhablock = 'MIXTR',
                    lhacode = [ 4, 1 ])

RUTR4x2 = Parameter(name = 'RUTR4x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.030406133841326687,
                    texname = '\\text{RUTR4x2}',
                    lhablock = 'MIXTR',
                    lhacode = [ 4, 2 ])

RUTR4x3 = Parameter(name = 'RUTR4x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.017570295459842622,
                    texname = '\\text{RUTR4x3}',
                    lhablock = 'MIXTR',
                    lhacode = [ 4, 3 ])

RUTR4x4 = Parameter(name = 'RUTR4x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.0106014183974103,
                    texname = '\\text{RUTR4x4}',
                    lhablock = 'MIXTR',
                    lhacode = [ 4, 4 ])

RUTR4x5 = Parameter(name = 'RUTR4x5',
                    nature = 'external',
                    type = 'real',
                    value = -0.9065057773482683,
                    texname = '\\text{RUTR4x5}',
                    lhablock = 'MIXTR',
                    lhacode = [ 4, 5 ])

RUTR4x6 = Parameter(name = 'RUTR4x6',
                    nature = 'external',
                    type = 'real',
                    value = 0.3127556060207054,
                    texname = '\\text{RUTR4x6}',
                    lhablock = 'MIXTR',
                    lhacode = [ 4, 6 ])

RUTR4x7 = Parameter(name = 'RUTR4x7',
                    nature = 'external',
                    type = 'real',
                    value = 0.280994565304978,
                    texname = '\\text{RUTR4x7}',
                    lhablock = 'MIXTR',
                    lhacode = [ 4, 7 ])

RUTR5x1 = Parameter(name = 'RUTR5x1',
                    nature = 'external',
                    type = 'real',
                    value = 1.0580945841720535e-14,
                    texname = '\\text{RUTR5x1}',
                    lhablock = 'MIXTR',
                    lhacode = [ 5, 1 ])

RUTR5x2 = Parameter(name = 'RUTR5x2',
                    nature = 'external',
                    type = 'real',
                    value = 1.6116316408728098e-14,
                    texname = '\\text{RUTR5x2}',
                    lhablock = 'MIXTR',
                    lhacode = [ 5, 2 ])

RUTR5x3 = Parameter(name = 'RUTR5x3',
                    nature = 'external',
                    type = 'real',
                    value = -1.673753276077733e-14,
                    texname = '\\text{RUTR5x3}',
                    lhablock = 'MIXTR',
                    lhacode = [ 5, 3 ])

RUTR5x4 = Parameter(name = 'RUTR5x4',
                    nature = 'external',
                    type = 'real',
                    value = 1.0378110352563621e-14,
                    texname = '\\text{RUTR5x4}',
                    lhablock = 'MIXTR',
                    lhacode = [ 5, 4 ])

RUTR5x5 = Parameter(name = 'RUTR5x5',
                    nature = 'external',
                    type = 'real',
                    value = 0.4082482904631639,
                    texname = '\\text{RUTR5x5}',
                    lhablock = 'MIXTR',
                    lhacode = [ 5, 5 ])

RUTR5x6 = Parameter(name = 'RUTR5x6',
                    nature = 'external',
                    type = 'real',
                    value = 0.8164965809279814,
                    texname = '\\text{RUTR5x6}',
                    lhablock = 'MIXTR',
                    lhacode = [ 5, 6 ])

RUTR5x7 = Parameter(name = 'RUTR5x7',
                    nature = 'external',
                    type = 'real',
                    value = 0.4082482904640511,
                    texname = '\\text{RUTR5x7}',
                    lhablock = 'MIXTR',
                    lhacode = [ 5, 7 ])

RUTR6x1 = Parameter(name = 'RUTR6x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.8690077613943022,
                    texname = '\\text{RUTR6x1}',
                    lhablock = 'MIXTR',
                    lhacode = [ 6, 1 ])

RUTR6x2 = Parameter(name = 'RUTR6x2',
                    nature = 'external',
                    type = 'real',
                    value = -0.017690337766747673,
                    texname = '\\text{RUTR6x2}',
                    lhablock = 'MIXTR',
                    lhacode = [ 6, 2 ])

RUTR6x3 = Parameter(name = 'RUTR6x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.22246719662773737,
                    texname = '\\text{RUTR6x3}',
                    lhablock = 'MIXTR',
                    lhacode = [ 6, 3 ])

RUTR6x4 = Parameter(name = 'RUTR6x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.42993733798605865,
                    texname = '\\text{RUTR6x4}',
                    lhablock = 'MIXTR',
                    lhacode = [ 6, 4 ])

RUTR6x5 = Parameter(name = 'RUTR6x5',
                    nature = 'external',
                    type = 'real',
                    value = 0.026221224997267013,
                    texname = '\\text{RUTR6x5}',
                    lhablock = 'MIXTR',
                    lhacode = [ 6, 5 ])

RUTR6x6 = Parameter(name = 'RUTR6x6',
                    nature = 'external',
                    type = 'real',
                    value = -0.053731365129478875,
                    texname = '\\text{RUTR6x6}',
                    lhablock = 'MIXTR',
                    lhacode = [ 6, 6 ])

RUTR6x7 = Parameter(name = 'RUTR6x7',
                    nature = 'external',
                    type = 'real',
                    value = 0.08124150526169001,
                    texname = '\\text{RUTR6x7}',
                    lhablock = 'MIXTR',
                    lhacode = [ 6, 7 ])

RUTR7x1 = Parameter(name = 'RUTR7x1',
                    nature = 'external',
                    type = 'real',
                    value = -0.10938289792725164,
                    texname = '\\text{RUTR7x1}',
                    lhablock = 'MIXTR',
                    lhacode = [ 7, 1 ])

RUTR7x2 = Parameter(name = 'RUTR7x2',
                    nature = 'external',
                    type = 'real',
                    value = -0.9600750288803878,
                    texname = '\\text{RUTR7x2}',
                    lhablock = 'MIXTR',
                    lhacode = [ 7, 2 ])

RUTR7x3 = Parameter(name = 'RUTR7x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.011894285174978763,
                    texname = '\\text{RUTR7x3}',
                    lhablock = 'MIXTR',
                    lhacode = [ 7, 3 ])

RUTR7x4 = Parameter(name = 'RUTR7x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.12516570113295777,
                    texname = '\\text{RUTR7x4}',
                    lhablock = 'MIXTR',
                    lhacode = [ 7, 4 ])

RUTR7x5 = Parameter(name = 'RUTR7x5',
                    nature = 'external',
                    type = 'real',
                    value = -0.0035411999093950732,
                    texname = '\\text{RUTR7x5}',
                    lhablock = 'MIXTR',
                    lhacode = [ 7, 5 ])

RUTR7x6 = Parameter(name = 'RUTR7x6',
                    nature = 'external',
                    type = 'real',
                    value = -0.0990507740897622,
                    texname = '\\text{RUTR7x6}',
                    lhablock = 'MIXTR',
                    lhacode = [ 7, 6 ])

RUTR7x7 = Parameter(name = 'RUTR7x7',
                    nature = 'external',
                    type = 'real',
                    value = 0.20164274808891952,
                    texname = '\\text{RUTR7x7}',
                    lhablock = 'MIXTR',
                    lhacode = [ 7, 7 ])

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

IUTR1x5 = Parameter(name = 'IUTR1x5',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR1x5}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 1, 5 ])

IUTR1x6 = Parameter(name = 'IUTR1x6',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR1x6}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 1, 6 ])

IUTR1x7 = Parameter(name = 'IUTR1x7',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR1x7}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 1, 7 ])

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

IUTR2x5 = Parameter(name = 'IUTR2x5',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR2x5}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 2, 5 ])

IUTR2x6 = Parameter(name = 'IUTR2x6',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR2x6}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 2, 6 ])

IUTR2x7 = Parameter(name = 'IUTR2x7',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR2x7}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 2, 7 ])

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

IUTR3x5 = Parameter(name = 'IUTR3x5',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR3x5}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 3, 5 ])

IUTR3x6 = Parameter(name = 'IUTR3x6',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR3x6}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 3, 6 ])

IUTR3x7 = Parameter(name = 'IUTR3x7',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR3x7}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 3, 7 ])

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

IUTR4x5 = Parameter(name = 'IUTR4x5',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR4x5}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 4, 5 ])

IUTR4x6 = Parameter(name = 'IUTR4x6',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR4x6}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 4, 6 ])

IUTR4x7 = Parameter(name = 'IUTR4x7',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR4x7}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 4, 7 ])

IUTR5x1 = Parameter(name = 'IUTR5x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR5x1}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 5, 1 ])

IUTR5x2 = Parameter(name = 'IUTR5x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR5x2}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 5, 2 ])

IUTR5x3 = Parameter(name = 'IUTR5x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR5x3}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 5, 3 ])

IUTR5x4 = Parameter(name = 'IUTR5x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR5x4}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 5, 4 ])

IUTR5x5 = Parameter(name = 'IUTR5x5',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR5x5}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 5, 5 ])

IUTR5x6 = Parameter(name = 'IUTR5x6',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR5x6}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 5, 6 ])

IUTR5x7 = Parameter(name = 'IUTR5x7',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR5x7}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 5, 7 ])

IUTR6x1 = Parameter(name = 'IUTR6x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR6x1}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 6, 1 ])

IUTR6x2 = Parameter(name = 'IUTR6x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR6x2}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 6, 2 ])

IUTR6x3 = Parameter(name = 'IUTR6x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR6x3}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 6, 3 ])

IUTR6x4 = Parameter(name = 'IUTR6x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR6x4}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 6, 4 ])

IUTR6x5 = Parameter(name = 'IUTR6x5',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR6x5}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 6, 5 ])

IUTR6x6 = Parameter(name = 'IUTR6x6',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR6x6}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 6, 6 ])

IUTR6x7 = Parameter(name = 'IUTR6x7',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR6x7}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 6, 7 ])

IUTR7x1 = Parameter(name = 'IUTR7x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR7x1}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 7, 1 ])

IUTR7x2 = Parameter(name = 'IUTR7x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR7x2}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 7, 2 ])

IUTR7x3 = Parameter(name = 'IUTR7x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR7x3}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 7, 3 ])

IUTR7x4 = Parameter(name = 'IUTR7x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR7x4}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 7, 4 ])

IUTR7x5 = Parameter(name = 'IUTR7x5',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR7x5}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 7, 5 ])

IUTR7x6 = Parameter(name = 'IUTR7x6',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR7x6}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 7, 6 ])

IUTR7x7 = Parameter(name = 'IUTR7x7',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUTR7x7}',
                    lhablock = 'IMMIXTR',
                    lhacode = [ 7, 7 ])

RUBL1x1 = Parameter(name = 'RUBL1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.5814484243241691,
                    texname = '\\text{RUBL1x1}',
                    lhablock = 'MIXBL',
                    lhacode = [ 1, 1 ])

RUBL1x2 = Parameter(name = 'RUBL1x2',
                    nature = 'external',
                    type = 'real',
                    value = -0.8008872786919412,
                    texname = '\\text{RUBL1x2}',
                    lhablock = 'MIXBL',
                    lhacode = [ 1, 2 ])

RUBL1x3 = Parameter(name = 'RUBL1x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.10123560806444973,
                    texname = '\\text{RUBL1x3}',
                    lhablock = 'MIXBL',
                    lhacode = [ 1, 3 ])

RUBL1x4 = Parameter(name = 'RUBL1x4',
                    nature = 'external',
                    type = 'real',
                    value = -0.10123560806444971,
                    texname = '\\text{RUBL1x4}',
                    lhablock = 'MIXBL',
                    lhacode = [ 1, 4 ])

RUBL2x1 = Parameter(name = 'RUBL2x1',
                    nature = 'external',
                    type = 'real',
                    value = -0.022384046054811396,
                    texname = '\\text{RUBL2x1}',
                    lhablock = 'MIXBL',
                    lhacode = [ 2, 1 ])

RUBL2x2 = Parameter(name = 'RUBL2x2',
                    nature = 'external',
                    type = 'real',
                    value = -0.19165418712825022,
                    texname = '\\text{RUBL2x2}',
                    lhablock = 'MIXBL',
                    lhacode = [ 2, 2 ])

RUBL2x3 = Parameter(name = 'RUBL2x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.6938182856621845,
                    texname = '\\text{RUBL2x3}',
                    lhablock = 'MIXBL',
                    lhacode = [ 2, 3 ])

RUBL2x4 = Parameter(name = 'RUBL2x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.6938182856621848,
                    texname = '\\text{RUBL2x4}',
                    lhablock = 'MIXBL',
                    lhacode = [ 2, 4 ])

RUBL3x1 = Parameter(name = 'RUBL3x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{RUBL3x1}',
                    lhablock = 'MIXBL',
                    lhacode = [ 3, 1 ])

RUBL3x2 = Parameter(name = 'RUBL3x2',
                    nature = 'external',
                    type = 'real',
                    value = -1.1592537223779667e-17,
                    texname = '\\text{RUBL3x2}',
                    lhablock = 'MIXBL',
                    lhacode = [ 3, 2 ])

RUBL3x3 = Parameter(name = 'RUBL3x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.7071067811865476,
                    texname = '\\text{RUBL3x3}',
                    lhablock = 'MIXBL',
                    lhacode = [ 3, 3 ])

RUBL3x4 = Parameter(name = 'RUBL3x4',
                    nature = 'external',
                    type = 'real',
                    value = -0.7071067811865475,
                    texname = '\\text{RUBL3x4}',
                    lhablock = 'MIXBL',
                    lhacode = [ 3, 4 ])

RUBL4x1 = Parameter(name = 'RUBL4x1',
                    nature = 'external',
                    type = 'real',
                    value = -0.813275282012897,
                    texname = '\\text{RUBL4x1}',
                    lhablock = 'MIXBL',
                    lhacode = [ 4, 1 ])

RUBL4x2 = Parameter(name = 'RUBL4x2',
                    nature = 'external',
                    type = 'real',
                    value = -0.5673167011340551,
                    texname = '\\text{RUBL4x2}',
                    lhablock = 'MIXBL',
                    lhacode = [ 4, 2 ])

RUBL4x3 = Parameter(name = 'RUBL4x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.09147424851075993,
                    texname = '\\text{RUBL4x3}',
                    lhablock = 'MIXBL',
                    lhacode = [ 4, 3 ])

RUBL4x4 = Parameter(name = 'RUBL4x4',
                    nature = 'external',
                    type = 'real',
                    value = -0.09147424851075993,
                    texname = '\\text{RUBL4x4}',
                    lhablock = 'MIXBL',
                    lhacode = [ 4, 4 ])

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

IUBL1x3 = Parameter(name = 'IUBL1x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBL1x3}',
                    lhablock = 'IMMIXBL',
                    lhacode = [ 1, 3 ])

IUBL1x4 = Parameter(name = 'IUBL1x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBL1x4}',
                    lhablock = 'IMMIXBL',
                    lhacode = [ 1, 4 ])

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

IUBL2x3 = Parameter(name = 'IUBL2x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBL2x3}',
                    lhablock = 'IMMIXBL',
                    lhacode = [ 2, 3 ])

IUBL2x4 = Parameter(name = 'IUBL2x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBL2x4}',
                    lhablock = 'IMMIXBL',
                    lhacode = [ 2, 4 ])

IUBL3x1 = Parameter(name = 'IUBL3x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBL3x1}',
                    lhablock = 'IMMIXBL',
                    lhacode = [ 3, 1 ])

IUBL3x2 = Parameter(name = 'IUBL3x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBL3x2}',
                    lhablock = 'IMMIXBL',
                    lhacode = [ 3, 2 ])

IUBL3x3 = Parameter(name = 'IUBL3x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBL3x3}',
                    lhablock = 'IMMIXBL',
                    lhacode = [ 3, 3 ])

IUBL3x4 = Parameter(name = 'IUBL3x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBL3x4}',
                    lhablock = 'IMMIXBL',
                    lhacode = [ 3, 4 ])

IUBL4x1 = Parameter(name = 'IUBL4x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBL4x1}',
                    lhablock = 'IMMIXBL',
                    lhacode = [ 4, 1 ])

IUBL4x2 = Parameter(name = 'IUBL4x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBL4x2}',
                    lhablock = 'IMMIXBL',
                    lhacode = [ 4, 2 ])

IUBL4x3 = Parameter(name = 'IUBL4x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBL4x3}',
                    lhablock = 'IMMIXBL',
                    lhacode = [ 4, 3 ])

IUBL4x4 = Parameter(name = 'IUBL4x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBL4x4}',
                    lhablock = 'IMMIXBL',
                    lhacode = [ 4, 4 ])

RUBR1x1 = Parameter(name = 'RUBR1x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.9999995905598186,
                    texname = '\\text{RUBR1x1}',
                    lhablock = 'MIXBR',
                    lhacode = [ 1, 1 ])

RUBR1x2 = Parameter(name = 'RUBR1x2',
                    nature = 'external',
                    type = 'real',
                    value = -0.0008927833856880419,
                    texname = '\\text{RUBR1x2}',
                    lhablock = 'MIXBR',
                    lhacode = [ 1, 2 ])

RUBR1x3 = Parameter(name = 'RUBR1x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.00010444620995815245,
                    texname = '\\text{RUBR1x3}',
                    lhablock = 'MIXBR',
                    lhacode = [ 1, 3 ])

RUBR1x4 = Parameter(name = 'RUBR1x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.0001044462099499368,
                    texname = '\\text{RUBR1x4}',
                    lhablock = 'MIXBR',
                    lhacode = [ 1, 4 ])

RUBR2x1 = Parameter(name = 'RUBR2x1',
                    nature = 'external',
                    type = 'real',
                    value = -0.000039829952402622236,
                    texname = '\\text{RUBR2x1}',
                    lhablock = 'MIXBR',
                    lhacode = [ 2, 1 ])

RUBR2x2 = Parameter(name = 'RUBR2x2',
                    nature = 'external',
                    type = 'real',
                    value = -0.20649542952736372,
                    texname = '\\text{RUBR2x2}',
                    lhablock = 'MIXBR',
                    lhacode = [ 2, 2 ])

RUBR2x3 = Parameter(name = 'RUBR2x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.6918669077206553,
                    texname = '\\text{RUBR2x3}',
                    lhablock = 'MIXBR',
                    lhacode = [ 2, 3 ])

RUBR2x4 = Parameter(name = 'RUBR2x4',
                    nature = 'external',
                    type = 'real',
                    value = -0.6918669077206556,
                    texname = '\\text{RUBR2x4}',
                    lhablock = 'MIXBR',
                    lhacode = [ 2, 4 ])

RUBR3x1 = Parameter(name = 'RUBR3x1',
                    nature = 'external',
                    type = 'real',
                    value = 5.725462464658752e-15,
                    texname = '\\text{RUBR3x1}',
                    lhablock = 'MIXBR',
                    lhacode = [ 3, 1 ])

RUBR3x2 = Parameter(name = 'RUBR3x2',
                    nature = 'external',
                    type = 'real',
                    value = -4.8916855614543594e-17,
                    texname = '\\text{RUBR3x2}',
                    lhablock = 'MIXBR',
                    lhacode = [ 3, 2 ])

RUBR3x3 = Parameter(name = 'RUBR3x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.7071067811865477,
                    texname = '\\text{RUBR3x3}',
                    lhablock = 'MIXBR',
                    lhacode = [ 3, 3 ])

RUBR3x4 = Parameter(name = 'RUBR3x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.7071067811865474,
                    texname = '\\text{RUBR3x4}',
                    lhablock = 'MIXBR',
                    lhacode = [ 3, 4 ])

RUBR4x1 = Parameter(name = 'RUBR4x1',
                    nature = 'external',
                    type = 'real',
                    value = -0.0009040430134678115,
                    texname = '\\text{RUBR4x1}',
                    lhablock = 'MIXBR',
                    lhacode = [ 4, 1 ])

RUBR4x2 = Parameter(name = 'RUBR4x2',
                    nature = 'external',
                    type = 'real',
                    value = -0.9784471577566853,
                    texname = '\\text{RUBR4x2}',
                    lhablock = 'MIXBR',
                    lhacode = [ 4, 2 ])

RUBR4x3 = Parameter(name = 'RUBR4x3',
                    nature = 'external',
                    type = 'real',
                    value = -0.14601428386307624,
                    texname = '\\text{RUBR4x3}',
                    lhablock = 'MIXBR',
                    lhacode = [ 4, 3 ])

RUBR4x4 = Parameter(name = 'RUBR4x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.14601428386307624,
                    texname = '\\text{RUBR4x4}',
                    lhablock = 'MIXBR',
                    lhacode = [ 4, 4 ])

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

IUBR1x3 = Parameter(name = 'IUBR1x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBR1x3}',
                    lhablock = 'IMMIXBR',
                    lhacode = [ 1, 3 ])

IUBR1x4 = Parameter(name = 'IUBR1x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBR1x4}',
                    lhablock = 'IMMIXBR',
                    lhacode = [ 1, 4 ])

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

IUBR2x3 = Parameter(name = 'IUBR2x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBR2x3}',
                    lhablock = 'IMMIXBR',
                    lhacode = [ 2, 3 ])

IUBR2x4 = Parameter(name = 'IUBR2x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBR2x4}',
                    lhablock = 'IMMIXBR',
                    lhacode = [ 2, 4 ])

IUBR3x1 = Parameter(name = 'IUBR3x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBR3x1}',
                    lhablock = 'IMMIXBR',
                    lhacode = [ 3, 1 ])

IUBR3x2 = Parameter(name = 'IUBR3x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBR3x2}',
                    lhablock = 'IMMIXBR',
                    lhacode = [ 3, 2 ])

IUBR3x3 = Parameter(name = 'IUBR3x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBR3x3}',
                    lhablock = 'IMMIXBR',
                    lhacode = [ 3, 3 ])

IUBR3x4 = Parameter(name = 'IUBR3x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBR3x4}',
                    lhablock = 'IMMIXBR',
                    lhacode = [ 3, 4 ])

IUBR4x1 = Parameter(name = 'IUBR4x1',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBR4x1}',
                    lhablock = 'IMMIXBR',
                    lhacode = [ 4, 1 ])

IUBR4x2 = Parameter(name = 'IUBR4x2',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBR4x2}',
                    lhablock = 'IMMIXBR',
                    lhacode = [ 4, 2 ])

IUBR4x3 = Parameter(name = 'IUBR4x3',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBR4x3}',
                    lhablock = 'IMMIXBR',
                    lhacode = [ 4, 3 ])

IUBR4x4 = Parameter(name = 'IUBR4x4',
                    nature = 'external',
                    type = 'real',
                    value = 0.,
                    texname = '\\text{IUBR4x4}',
                    lhablock = 'IMMIXBR',
                    lhacode = [ 4, 4 ])

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
                value = 2458.76254120206,
                texname = '\\text{MT4}',
                lhablock = 'MASS',
                lhacode = [ 9000 ])

MX23 = Parameter(name = 'MX23',
                 nature = 'external',
                 type = 'real',
                 value = 2699.0419524388776,
                 texname = '\\text{MX23}',
                 lhablock = 'MASS',
                 lhacode = [ 9001 ])

MT1 = Parameter(name = 'MT1',
                nature = 'external',
                type = 'real',
                value = 2713.5245108574245,
                texname = '\\text{MT1}',
                lhablock = 'MASS',
                lhacode = [ 9002 ])

MU23 = Parameter(name = 'MU23',
                 nature = 'external',
                 type = 'real',
                 value = 2713.93,
                 texname = '\\text{MU23}',
                 lhablock = 'MASS',
                 lhacode = [ 9003 ])

MY23 = Parameter(name = 'MY23',
                 nature = 'external',
                 type = 'real',
                 value = 3611.157774846642,
                 texname = '\\text{MY23}',
                 lhablock = 'MASS',
                 lhacode = [ 9004 ])

MZ23 = Parameter(name = 'MZ23',
                 nature = 'external',
                 type = 'real',
                 value = 4327.865737968602,
                 texname = '\\text{MZ23}',
                 lhablock = 'MASS',
                 lhacode = [ 9005 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MB4 = Parameter(name = 'MB4',
                nature = 'external',
                type = 'real',
                value = 2706.297017061536,
                texname = '\\text{MB4}',
                lhablock = 'MASS',
                lhacode = [ 10000 ])

MY13 = Parameter(name = 'MY13',
                 nature = 'external',
                 type = 'real',
                 value = 2713.93,
                 texname = '\\text{MY13}',
                 lhablock = 'MASS',
                 lhacode = [ 10001 ])

MZ13 = Parameter(name = 'MZ13',
                 nature = 'external',
                 type = 'real',
                 value = 4332.066694791222,
                 texname = '\\text{MZ13}',
                 lhablock = 'MASS',
                 lhacode = [ 10002 ])

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

WU23 = Parameter(name = 'WU23',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WU23}',
                 lhablock = 'DECAY',
                 lhacode = [ 9003 ])

WY23 = Parameter(name = 'WY23',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WY23}',
                 lhablock = 'DECAY',
                 lhacode = [ 9004 ])

WZ23 = Parameter(name = 'WZ23',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WZ23}',
                 lhablock = 'DECAY',
                 lhacode = [ 9005 ])

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

WY13 = Parameter(name = 'WY13',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WY13}',
                 lhablock = 'DECAY',
                 lhacode = [ 10001 ])

WZ13 = Parameter(name = 'WZ13',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WZ13}',
                 lhablock = 'DECAY',
                 lhacode = [ 10002 ])

WX53 = Parameter(name = 'WX53',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WX53}',
                 lhablock = 'DECAY',
                 lhacode = [ 11000 ])

WU53 = Parameter(name = 'WU53',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WU53}',
                 lhablock = 'DECAY',
                 lhacode = [ 11001 ])

WY53 = Parameter(name = 'WY53',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WY53}',
                 lhablock = 'DECAY',
                 lhacode = [ 11002 ])

WU83 = Parameter(name = 'WU83',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WU83}',
                 lhablock = 'DECAY',
                 lhacode = [ 13000 ])

WZ43 = Parameter(name = 'WZ43',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{WZ43}',
                 lhablock = 'DECAY',
                 lhacode = [ 12000 ])

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

MU83 = Parameter(name = 'MU83',
                 nature = 'internal',
                 type = 'real',
                 value = 'M9',
                 texname = '\\text{MU83}')

MU53 = Parameter(name = 'MU53',
                 nature = 'internal',
                 type = 'real',
                 value = 'M9',
                 texname = '\\text{MU53}')

MY53 = Parameter(name = 'MY53',
                 nature = 'internal',
                 type = 'real',
                 value = 'M9',
                 texname = '\\text{MY53}')

MZ43 = Parameter(name = 'MZ43',
                 nature = 'internal',
                 type = 'real',
                 value = 'M9',
                 texname = '\\text{MZ43}')

MT141x1 = Parameter(name = 'MT141x1',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT141x1}')

MT142x2 = Parameter(name = 'MT142x2',
                    nature = 'internal',
                    type = 'real',
                    value = '-M4',
                    texname = '\\text{MT142x2}')

MT142x3 = Parameter(name = 'MT142x3',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT142x3}')

MT142x4 = Parameter(name = 'MT142x4',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT142x4}')

MT142x5 = Parameter(name = 'MT142x5',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT142x5}')

MT142x6 = Parameter(name = 'MT142x6',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT142x6}')

MT142x7 = Parameter(name = 'MT142x7',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT142x7}')

MT143x2 = Parameter(name = 'MT143x2',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT143x2}')

MT143x3 = Parameter(name = 'MT143x3',
                    nature = 'internal',
                    type = 'real',
                    value = '-M4',
                    texname = '\\text{MT143x3}')

MT143x4 = Parameter(name = 'MT143x4',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT143x4}')

MT143x5 = Parameter(name = 'MT143x5',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT143x5}')

MT143x6 = Parameter(name = 'MT143x6',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT143x6}')

MT143x7 = Parameter(name = 'MT143x7',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT143x7}')

MT144x2 = Parameter(name = 'MT144x2',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT144x2}')

MT144x3 = Parameter(name = 'MT144x3',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT144x3}')

MT144x4 = Parameter(name = 'MT144x4',
                    nature = 'internal',
                    type = 'real',
                    value = '-M1',
                    texname = '\\text{MT144x4}')

MT144x5 = Parameter(name = 'MT144x5',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT144x5}')

MT144x6 = Parameter(name = 'MT144x6',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT144x6}')

MT144x7 = Parameter(name = 'MT144x7',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT144x7}')

MT145x2 = Parameter(name = 'MT145x2',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT145x2}')

MT145x3 = Parameter(name = 'MT145x3',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT145x3}')

MT145x4 = Parameter(name = 'MT145x4',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT145x4}')

MT145x5 = Parameter(name = 'MT145x5',
                    nature = 'internal',
                    type = 'real',
                    value = '-M9',
                    texname = '\\text{MT145x5}')

MT145x6 = Parameter(name = 'MT145x6',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT145x6}')

MT145x7 = Parameter(name = 'MT145x7',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT145x7}')

MT146x2 = Parameter(name = 'MT146x2',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT146x2}')

MT146x3 = Parameter(name = 'MT146x3',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT146x3}')

MT146x4 = Parameter(name = 'MT146x4',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT146x4}')

MT146x5 = Parameter(name = 'MT146x5',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT146x5}')

MT146x6 = Parameter(name = 'MT146x6',
                    nature = 'internal',
                    type = 'real',
                    value = '-M9',
                    texname = '\\text{MT146x6}')

MT146x7 = Parameter(name = 'MT146x7',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT146x7}')

MT147x2 = Parameter(name = 'MT147x2',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT147x2}')

MT147x3 = Parameter(name = 'MT147x3',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT147x3}')

MT147x4 = Parameter(name = 'MT147x4',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT147x4}')

MT147x5 = Parameter(name = 'MT147x5',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT147x5}')

MT147x6 = Parameter(name = 'MT147x6',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MT147x6}')

MT147x7 = Parameter(name = 'MT147x7',
                    nature = 'internal',
                    type = 'real',
                    value = '-M9',
                    texname = '\\text{MT147x7}')

MB142x1 = Parameter(name = 'MB142x1',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MB142x1}')

MB142x2 = Parameter(name = 'MB142x2',
                    nature = 'internal',
                    type = 'real',
                    value = '-M4',
                    texname = '\\text{MB142x2}')

MB142x3 = Parameter(name = 'MB142x3',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MB142x3}')

MB142x4 = Parameter(name = 'MB142x4',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MB142x4}')

MB143x1 = Parameter(name = 'MB143x1',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MB143x1}')

MB143x2 = Parameter(name = 'MB143x2',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MB143x2}')

MB143x3 = Parameter(name = 'MB143x3',
                    nature = 'internal',
                    type = 'real',
                    value = '-M9',
                    texname = '\\text{MB143x3}')

MB143x4 = Parameter(name = 'MB143x4',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MB143x4}')

MB144x1 = Parameter(name = 'MB144x1',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MB144x1}')

MB144x2 = Parameter(name = 'MB144x2',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MB144x2}')

MB144x3 = Parameter(name = 'MB144x3',
                    nature = 'internal',
                    type = 'real',
                    value = '0',
                    texname = '\\text{MB144x3}')

MB144x4 = Parameter(name = 'MB144x4',
                    nature = 'internal',
                    type = 'real',
                    value = '-M9',
                    texname = '\\text{MB144x4}')

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

UTL1x5 = Parameter(name = 'UTL1x5',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL1x5 + RUTL1x5',
                   texname = '\\text{UTL1x5}')

UTL1x6 = Parameter(name = 'UTL1x6',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL1x6 + RUTL1x6',
                   texname = '\\text{UTL1x6}')

UTL1x7 = Parameter(name = 'UTL1x7',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL1x7 + RUTL1x7',
                   texname = '\\text{UTL1x7}')

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

UTL2x5 = Parameter(name = 'UTL2x5',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL2x5 + RUTL2x5',
                   texname = '\\text{UTL2x5}')

UTL2x6 = Parameter(name = 'UTL2x6',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL2x6 + RUTL2x6',
                   texname = '\\text{UTL2x6}')

UTL2x7 = Parameter(name = 'UTL2x7',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL2x7 + RUTL2x7',
                   texname = '\\text{UTL2x7}')

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

UTL3x5 = Parameter(name = 'UTL3x5',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL3x5 + RUTL3x5',
                   texname = '\\text{UTL3x5}')

UTL3x6 = Parameter(name = 'UTL3x6',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL3x6 + RUTL3x6',
                   texname = '\\text{UTL3x6}')

UTL3x7 = Parameter(name = 'UTL3x7',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL3x7 + RUTL3x7',
                   texname = '\\text{UTL3x7}')

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

UTL4x5 = Parameter(name = 'UTL4x5',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL4x5 + RUTL4x5',
                   texname = '\\text{UTL4x5}')

UTL4x6 = Parameter(name = 'UTL4x6',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL4x6 + RUTL4x6',
                   texname = '\\text{UTL4x6}')

UTL4x7 = Parameter(name = 'UTL4x7',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL4x7 + RUTL4x7',
                   texname = '\\text{UTL4x7}')

UTL5x1 = Parameter(name = 'UTL5x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL5x1 + RUTL5x1',
                   texname = '\\text{UTL5x1}')

UTL5x2 = Parameter(name = 'UTL5x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL5x2 + RUTL5x2',
                   texname = '\\text{UTL5x2}')

UTL5x3 = Parameter(name = 'UTL5x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL5x3 + RUTL5x3',
                   texname = '\\text{UTL5x3}')

UTL5x4 = Parameter(name = 'UTL5x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL5x4 + RUTL5x4',
                   texname = '\\text{UTL5x4}')

UTL5x5 = Parameter(name = 'UTL5x5',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL5x5 + RUTL5x5',
                   texname = '\\text{UTL5x5}')

UTL5x6 = Parameter(name = 'UTL5x6',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL5x6 + RUTL5x6',
                   texname = '\\text{UTL5x6}')

UTL5x7 = Parameter(name = 'UTL5x7',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL5x7 + RUTL5x7',
                   texname = '\\text{UTL5x7}')

UTL6x1 = Parameter(name = 'UTL6x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL6x1 + RUTL6x1',
                   texname = '\\text{UTL6x1}')

UTL6x2 = Parameter(name = 'UTL6x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL6x2 + RUTL6x2',
                   texname = '\\text{UTL6x2}')

UTL6x3 = Parameter(name = 'UTL6x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL6x3 + RUTL6x3',
                   texname = '\\text{UTL6x3}')

UTL6x4 = Parameter(name = 'UTL6x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL6x4 + RUTL6x4',
                   texname = '\\text{UTL6x4}')

UTL6x5 = Parameter(name = 'UTL6x5',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL6x5 + RUTL6x5',
                   texname = '\\text{UTL6x5}')

UTL6x6 = Parameter(name = 'UTL6x6',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL6x6 + RUTL6x6',
                   texname = '\\text{UTL6x6}')

UTL6x7 = Parameter(name = 'UTL6x7',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL6x7 + RUTL6x7',
                   texname = '\\text{UTL6x7}')

UTL7x1 = Parameter(name = 'UTL7x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL7x1 + RUTL7x1',
                   texname = '\\text{UTL7x1}')

UTL7x2 = Parameter(name = 'UTL7x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL7x2 + RUTL7x2',
                   texname = '\\text{UTL7x2}')

UTL7x3 = Parameter(name = 'UTL7x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL7x3 + RUTL7x3',
                   texname = '\\text{UTL7x3}')

UTL7x4 = Parameter(name = 'UTL7x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL7x4 + RUTL7x4',
                   texname = '\\text{UTL7x4}')

UTL7x5 = Parameter(name = 'UTL7x5',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL7x5 + RUTL7x5',
                   texname = '\\text{UTL7x5}')

UTL7x6 = Parameter(name = 'UTL7x6',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL7x6 + RUTL7x6',
                   texname = '\\text{UTL7x6}')

UTL7x7 = Parameter(name = 'UTL7x7',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTL7x7 + RUTL7x7',
                   texname = '\\text{UTL7x7}')

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

UTR1x5 = Parameter(name = 'UTR1x5',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR1x5 + RUTR1x5',
                   texname = '\\text{UTR1x5}')

UTR1x6 = Parameter(name = 'UTR1x6',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR1x6 + RUTR1x6',
                   texname = '\\text{UTR1x6}')

UTR1x7 = Parameter(name = 'UTR1x7',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR1x7 + RUTR1x7',
                   texname = '\\text{UTR1x7}')

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

UTR2x5 = Parameter(name = 'UTR2x5',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR2x5 + RUTR2x5',
                   texname = '\\text{UTR2x5}')

UTR2x6 = Parameter(name = 'UTR2x6',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR2x6 + RUTR2x6',
                   texname = '\\text{UTR2x6}')

UTR2x7 = Parameter(name = 'UTR2x7',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR2x7 + RUTR2x7',
                   texname = '\\text{UTR2x7}')

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

UTR3x5 = Parameter(name = 'UTR3x5',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR3x5 + RUTR3x5',
                   texname = '\\text{UTR3x5}')

UTR3x6 = Parameter(name = 'UTR3x6',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR3x6 + RUTR3x6',
                   texname = '\\text{UTR3x6}')

UTR3x7 = Parameter(name = 'UTR3x7',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR3x7 + RUTR3x7',
                   texname = '\\text{UTR3x7}')

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

UTR4x5 = Parameter(name = 'UTR4x5',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR4x5 + RUTR4x5',
                   texname = '\\text{UTR4x5}')

UTR4x6 = Parameter(name = 'UTR4x6',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR4x6 + RUTR4x6',
                   texname = '\\text{UTR4x6}')

UTR4x7 = Parameter(name = 'UTR4x7',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR4x7 + RUTR4x7',
                   texname = '\\text{UTR4x7}')

UTR5x1 = Parameter(name = 'UTR5x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR5x1 + RUTR5x1',
                   texname = '\\text{UTR5x1}')

UTR5x2 = Parameter(name = 'UTR5x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR5x2 + RUTR5x2',
                   texname = '\\text{UTR5x2}')

UTR5x3 = Parameter(name = 'UTR5x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR5x3 + RUTR5x3',
                   texname = '\\text{UTR5x3}')

UTR5x4 = Parameter(name = 'UTR5x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR5x4 + RUTR5x4',
                   texname = '\\text{UTR5x4}')

UTR5x5 = Parameter(name = 'UTR5x5',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR5x5 + RUTR5x5',
                   texname = '\\text{UTR5x5}')

UTR5x6 = Parameter(name = 'UTR5x6',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR5x6 + RUTR5x6',
                   texname = '\\text{UTR5x6}')

UTR5x7 = Parameter(name = 'UTR5x7',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR5x7 + RUTR5x7',
                   texname = '\\text{UTR5x7}')

UTR6x1 = Parameter(name = 'UTR6x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR6x1 + RUTR6x1',
                   texname = '\\text{UTR6x1}')

UTR6x2 = Parameter(name = 'UTR6x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR6x2 + RUTR6x2',
                   texname = '\\text{UTR6x2}')

UTR6x3 = Parameter(name = 'UTR6x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR6x3 + RUTR6x3',
                   texname = '\\text{UTR6x3}')

UTR6x4 = Parameter(name = 'UTR6x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR6x4 + RUTR6x4',
                   texname = '\\text{UTR6x4}')

UTR6x5 = Parameter(name = 'UTR6x5',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR6x5 + RUTR6x5',
                   texname = '\\text{UTR6x5}')

UTR6x6 = Parameter(name = 'UTR6x6',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR6x6 + RUTR6x6',
                   texname = '\\text{UTR6x6}')

UTR6x7 = Parameter(name = 'UTR6x7',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR6x7 + RUTR6x7',
                   texname = '\\text{UTR6x7}')

UTR7x1 = Parameter(name = 'UTR7x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR7x1 + RUTR7x1',
                   texname = '\\text{UTR7x1}')

UTR7x2 = Parameter(name = 'UTR7x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR7x2 + RUTR7x2',
                   texname = '\\text{UTR7x2}')

UTR7x3 = Parameter(name = 'UTR7x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR7x3 + RUTR7x3',
                   texname = '\\text{UTR7x3}')

UTR7x4 = Parameter(name = 'UTR7x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR7x4 + RUTR7x4',
                   texname = '\\text{UTR7x4}')

UTR7x5 = Parameter(name = 'UTR7x5',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR7x5 + RUTR7x5',
                   texname = '\\text{UTR7x5}')

UTR7x6 = Parameter(name = 'UTR7x6',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR7x6 + RUTR7x6',
                   texname = '\\text{UTR7x6}')

UTR7x7 = Parameter(name = 'UTR7x7',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUTR7x7 + RUTR7x7',
                   texname = '\\text{UTR7x7}')

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

UBL1x3 = Parameter(name = 'UBL1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBL1x3 + RUBL1x3',
                   texname = '\\text{UBL1x3}')

UBL1x4 = Parameter(name = 'UBL1x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBL1x4 + RUBL1x4',
                   texname = '\\text{UBL1x4}')

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

UBL2x3 = Parameter(name = 'UBL2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBL2x3 + RUBL2x3',
                   texname = '\\text{UBL2x3}')

UBL2x4 = Parameter(name = 'UBL2x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBL2x4 + RUBL2x4',
                   texname = '\\text{UBL2x4}')

UBL3x1 = Parameter(name = 'UBL3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBL3x1 + RUBL3x1',
                   texname = '\\text{UBL3x1}')

UBL3x2 = Parameter(name = 'UBL3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBL3x2 + RUBL3x2',
                   texname = '\\text{UBL3x2}')

UBL3x3 = Parameter(name = 'UBL3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBL3x3 + RUBL3x3',
                   texname = '\\text{UBL3x3}')

UBL3x4 = Parameter(name = 'UBL3x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBL3x4 + RUBL3x4',
                   texname = '\\text{UBL3x4}')

UBL4x1 = Parameter(name = 'UBL4x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBL4x1 + RUBL4x1',
                   texname = '\\text{UBL4x1}')

UBL4x2 = Parameter(name = 'UBL4x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBL4x2 + RUBL4x2',
                   texname = '\\text{UBL4x2}')

UBL4x3 = Parameter(name = 'UBL4x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBL4x3 + RUBL4x3',
                   texname = '\\text{UBL4x3}')

UBL4x4 = Parameter(name = 'UBL4x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBL4x4 + RUBL4x4',
                   texname = '\\text{UBL4x4}')

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

UBR1x3 = Parameter(name = 'UBR1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBR1x3 + RUBR1x3',
                   texname = '\\text{UBR1x3}')

UBR1x4 = Parameter(name = 'UBR1x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBR1x4 + RUBR1x4',
                   texname = '\\text{UBR1x4}')

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

UBR2x3 = Parameter(name = 'UBR2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBR2x3 + RUBR2x3',
                   texname = '\\text{UBR2x3}')

UBR2x4 = Parameter(name = 'UBR2x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBR2x4 + RUBR2x4',
                   texname = '\\text{UBR2x4}')

UBR3x1 = Parameter(name = 'UBR3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBR3x1 + RUBR3x1',
                   texname = '\\text{UBR3x1}')

UBR3x2 = Parameter(name = 'UBR3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBR3x2 + RUBR3x2',
                   texname = '\\text{UBR3x2}')

UBR3x3 = Parameter(name = 'UBR3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBR3x3 + RUBR3x3',
                   texname = '\\text{UBR3x3}')

UBR3x4 = Parameter(name = 'UBR3x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBR3x4 + RUBR3x4',
                   texname = '\\text{UBR3x4}')

UBR4x1 = Parameter(name = 'UBR4x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBR4x1 + RUBR4x1',
                   texname = '\\text{UBR4x1}')

UBR4x2 = Parameter(name = 'UBR4x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBR4x2 + RUBR4x2',
                   texname = '\\text{UBR4x2}')

UBR4x3 = Parameter(name = 'UBR4x3',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBR4x3 + RUBR4x3',
                   texname = '\\text{UBR4x3}')

UBR4x4 = Parameter(name = 'UBR4x4',
                   nature = 'internal',
                   type = 'complex',
                   value = 'complex(0,1)*IUBR4x4 + RUBR4x4',
                   texname = '\\text{UBR4x4}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

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

cb = Parameter(name = 'cb',
               nature = 'internal',
               type = 'real',
               value = 'mbHS*cmath.sqrt(1 + (fs**2*(1 - xi)*yL4**2)/(M4**2 - mbHS**2) + (fs**2*xi*yL9**2)/(M9**2 - mbHS**2))',
               texname = '\\text{cb}')

MB141x2 = Parameter(name = 'MB141x2',
                    nature = 'internal',
                    type = 'real',
                    value = 'fs*yL4*cmath.sqrt(1 - xi)',
                    texname = '\\text{MB141x2}')

MB141x3 = Parameter(name = 'MB141x3',
                    nature = 'internal',
                    type = 'real',
                    value = '(fs*yL9*cmath.sqrt(xi))/cmath.sqrt(2)',
                    texname = '\\text{MB141x3}')

MB141x4 = Parameter(name = 'MB141x4',
                    nature = 'internal',
                    type = 'real',
                    value = '-((fs*yL9*cmath.sqrt(xi))/cmath.sqrt(2))',
                    texname = '\\text{MB141x4}')

MT141x2 = Parameter(name = 'MT141x2',
                    nature = 'internal',
                    type = 'real',
                    value = '(fs*yL4*(1 - 2*xi + cmath.sqrt(1 - xi)))/2.',
                    texname = '\\text{MT141x2}')

MT141x3 = Parameter(name = 'MT141x3',
                    nature = 'internal',
                    type = 'real',
                    value = '-(fs*yL4*(1 - 2*xi - cmath.sqrt(1 - xi)))/2.',
                    texname = '\\text{MT141x3}')

MT141x4 = Parameter(name = 'MT141x4',
                    nature = 'internal',
                    type = 'real',
                    value = '-(fs*yL1*cmath.sqrt(5)*cmath.sqrt(1 - xi)*cmath.sqrt(xi))/2.',
                    texname = '\\text{MT141x4}')

MT141x5 = Parameter(name = 'MT141x5',
                    nature = 'internal',
                    type = 'real',
                    value = '-(fs*yL9*(-1 + cmath.sqrt(1 - xi))*cmath.sqrt(xi))/2.',
                    texname = '\\text{MT141x5}')

MT141x6 = Parameter(name = 'MT141x6',
                    nature = 'internal',
                    type = 'real',
                    value = '(fs*yL9*cmath.sqrt((1 - xi)*xi))/2.',
                    texname = '\\text{MT141x6}')

MT141x7 = Parameter(name = 'MT141x7',
                    nature = 'internal',
                    type = 'real',
                    value = '-(fs*yL9*(1 + cmath.sqrt(1 - xi))*cmath.sqrt(xi))/2.',
                    texname = '\\text{MT141x7}')

MT142x1 = Parameter(name = 'MT142x1',
                    nature = 'internal',
                    type = 'real',
                    value = '(fs*yR4*cmath.sqrt(5)*cmath.sqrt(1 - xi)*cmath.sqrt(xi))/2.',
                    texname = '\\text{MT142x1}')

MT143x1 = Parameter(name = 'MT143x1',
                    nature = 'internal',
                    type = 'real',
                    value = '-(fs*yR4*cmath.sqrt(5)*cmath.sqrt(1 - xi)*cmath.sqrt(xi))/2.',
                    texname = '\\text{MT143x1}')

MT144x1 = Parameter(name = 'MT144x1',
                    nature = 'internal',
                    type = 'real',
                    value = 'fs*(1 - (5*xi)/4.)*yR1',
                    texname = '\\text{MT144x1}')

MT145x1 = Parameter(name = 'MT145x1',
                    nature = 'internal',
                    type = 'real',
                    value = '-(fs*xi*yR9*cmath.sqrt(5))/4.',
                    texname = '\\text{MT145x1}')

MT146x1 = Parameter(name = 'MT146x1',
                    nature = 'internal',
                    type = 'real',
                    value = '(fs*xi*yR9*cmath.sqrt(5))/4.',
                    texname = '\\text{MT146x1}')

MT147x1 = Parameter(name = 'MT147x1',
                    nature = 'internal',
                    type = 'real',
                    value = '-(fs*xi*yR9*cmath.sqrt(5))/4.',
                    texname = '\\text{MT147x1}')

WH = Parameter(name = 'WH',
               nature = 'internal',
               type = 'real',
               value = '0.004088*((0.61131*(1 - 2*xi)**2)/(1 - xi) + 0.30261*(1 - xi) + 0.08187*(((4*(1 - M1/M4)*M9)/M4 - ((9*M1)/M4 - (32*M1*M9)/M4**2 + (23*M9)/M4)*xi + 4*((3*M1)/M4 - (8*M1*M9)/M4**2 + (5*M9)/M4)*xi**2)/(((4*(1 - M1/M4)*M9)/M4 - ((3*M1)/M4 - (8*M1*M9)/M4**2 + (5*M9)/M4)*xi)*cmath.sqrt(1 - xi)) + (fs**2*(1 - M9**2/M4**2)*xi*yL1**2*cmath.sqrt(1 - xi))/(fs**2*(1 - M9**2/M4**2)*xi*yL1**2 + (M9**2*(M4**2 + fs**2*yL1**2))/M4**2))**2)',
               texname = '\\text{WH}')

MB141x1 = Parameter(name = 'MB141x1',
                    nature = 'internal',
                    type = 'real',
                    value = 'cb',
                    texname = '\\text{MB141x1}')

