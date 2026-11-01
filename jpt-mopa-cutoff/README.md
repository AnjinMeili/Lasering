# JPT MOPA fiber laser cut-off frequency tables

Per-model pulse width, cut-off frequency and maximum frequency for JPT M7, E-M7, E2-M7, M8 and LP sources, as one machine-readable CSV plus the tables below.

- **Cut-off (kHz):** at or above this repetition rate the source delivers full rated average power. Below it, average power falls roughly in proportion to frequency so peak power holds.
- **Max (kHz):** the highest repetition rate allowed at that pulse width.
- Each profile is specific to one model code. Do not scale values between wattages or series.

## Identifying your source without the manual

Many machine builders ship a JPT source without its manual, and some rebrand the machine entirely. The tables here are meant to fill that gap.

1. **Read the label on the source itself.** Somewhere on the source housing there is a sticker with the full model code (for example `YDFLP-E-100-M7-M-R`) and a serial number. It is often inside the machine's cabinet or under a cover, not on the outside of the machine. Power off and unplug before you open anything.
2. **Match the whole code, not just the wattage.** `M7`, `E-M7`, `E2-M7`, `M7-L1`, `M8` and `M8-S-W-V2` are different sources with different tables, even at the same wattage.
3. **Can't reach the label?** Ask the builder for the source's full model code and serial; the sales invoice or spec sheet sometimes lists it. As a rough hint, check which pulse widths your control software offers. The list should match the `pulse_ns` set for your model in the CSV, and a mismatch means you are probably looking at the wrong profile.
4. **Still unsure?** Treat the values as a starting point, not a guarantee, and test at the low end of the range on scrap.

If you have the manual and it disagrees with a table here, please open an issue or PR with the model code, manual revision and table number.

Data: [`jpt-mopa-cutoff.csv`](jpt-mopa-cutoff.csv), with columns `series, model_code, rated_w, mode, pulse_ns, cutoff_khz, max_khz, manual_ref, note`.

## YDFLP-60-M7-M-R

M7 · 60 W · S-PI-0035 v1.0 Table 5

| Pulse (ns) | Cut-off (kHz) | Max (kHz) |
| ---: | ---: | ---: |
| 2 | 1950 | 4000 |
| 4 | 1350 | 4000 |
| 6 | 975 | 4000 |
| 9 | 600 | 4000 |
| 13 | 412 | 3000 |
| 20 | 225 | 3000 |
| 30 | 187 | 3000 |
| 45 | 150 | 2000 |
| 60 | 135 | 2000 |
| 80 | 112 | 2000 |
| 100 | 105 | 1000 |
| 150 | 57 | 1000 |
| 200 | 45 | 1000 |
| 250 | 42 | 900 |
| 350 | 40 | 600 |
| 500 | 30 | 500 |

## YDFLP-80-M7-M-R

M7 · 80 W · S-PI-0035 v1.0 Table 5

| Pulse (ns) | Cut-off (kHz) | Max (kHz) |
| ---: | ---: | ---: |
| 2 | 2600 | 4000 |
| 4 | 1800 | 4000 |
| 6 | 1300 | 4000 |
| 9 | 800 | 4000 |
| 13 | 550 | 3000 |
| 20 | 300 | 3000 |
| 30 | 250 | 3000 |
| 45 | 200 | 2000 |
| 60 | 180 | 2000 |
| 80 | 150 | 2000 |
| 100 | 140 | 1000 |
| 150 | 76 | 1000 |
| 200 | 60 | 1000 |
| 250 | 56 | 900 |
| 350 | 53 | 600 |
| 500 | 40 | 500 |

## YDFLP-100-M7-M-R

M7 · 100 W · S-PI-0035 v1.0 Table 5

| Pulse (ns) | Cut-off (kHz) | Max (kHz) |
| ---: | ---: | ---: |
| 2 | 2960 | 4000 |
| 4 | 2160 | 4000 |
| 6 | 1400 | 4000 |
| 9 | 960 | 4000 |
| 13 | 680 | 3000 |
| 20 | 420 | 3000 |
| 30 | 300 | 3000 |
| 45 | 250 | 2000 |
| 60 | 200 | 2000 |
| 80 | 180 | 2000 |
| 100 | 160 | 1000 |
| 150 | 95 | 1000 |
| 200 | 75 | 1000 |
| 250 | 70 | 900 |
| 350 | 67 | 600 |
| 500 | 67 | 500 |

## YDFLP-120-M7-M-R

M7 · 120 W · S-PI-0035 v1.0 Table 5

| Pulse (ns) | Cut-off (kHz) | Max (kHz) |
| ---: | ---: | ---: |
| 2 | 3900 | 4000 |
| 4 | 2700 | 4000 |
| 6 | 1950 | 4000 |
| 9 | 1200 | 4000 |
| 13 | 825 | 3000 |
| 20 | 500 | 3000 |
| 30 | 300 | 3000 |
| 45 | 240 | 2000 |
| 60 | 216 | 2000 |
| 80 | 210 | 2000 |
| 100 | 190 | 1000 |
| 150 | 115 | 1000 |
| 200 | 90 | 1000 |
| 250 | 85 | 900 |
| 350 | 80 | 600 |
| 500 | 80 | 500 |

## YDFLP-200-M7-M-R

M7 · 200 W · v1.1 2021 Table 5

Note: 2/4/6 ns: manual guarantees only >45/>75/>100 W at 4000 kHz

| Pulse (ns) | Cut-off (kHz) | Max (kHz) |
| ---: | ---: | ---: |
| 2 | 4000 | 4000 |
| 4 | 4000 | 4000 |
| 6 | 4000 | 4000 |
| 9 | 4000 | 4000 |
| 13 | 2600 | 3000 |
| 20 | 1700 | 3000 |
| 30 | 1100 | 3000 |
| 45 | 950 | 2000 |
| 55 | 750 | 2000 |
| 60 | 650 | 2000 |
| 80 | 550 | 2000 |
| 100 | 480 | 1000 |
| 150 | 300 | 1000 |
| 200 | 240 | 1000 |
| 250 | 210 | 900 |
| 350 | 150 | 600 |
| 500 | 130 | 500 |

## YDFLP-E-20-M7-S-R

E-M7 · 20 W · J-SI-0036 v1.4 Table 4

| Pulse (ns) | Cut-off (kHz) | Max (kHz) |
| ---: | ---: | ---: |
| 2 | 850 | 4000 |
| 4 | 500 | 4000 |
| 6 | 320 | 4000 |
| 9 | 250 | 4000 |
| 13 | 170 | 3000 |
| 20 | 115 | 3000 |
| 30 | 90 | 3000 |
| 45 | 75 | 2000 |
| 60 | 65 | 2000 |
| 80 | 60 | 400 |
| 100 | 55 | 400 |
| 150 | 30 | 400 |
| 200 | 25 | 400 |
| 250 | 25 | 400 |
| 350 | 25 | 400 |
| 500 | 25 | 400 |

## YDFLP-E-30-M7-S-R

E-M7 · 30 W · J-SI-0036 v1.4 Table 4

| Pulse (ns) | Cut-off (kHz) | Max (kHz) |
| ---: | ---: | ---: |
| 2 | 1300 | 4000 |
| 4 | 750 | 4000 |
| 6 | 480 | 4000 |
| 9 | 375 | 4000 |
| 13 | 250 | 3000 |
| 20 | 170 | 3000 |
| 30 | 135 | 3000 |
| 45 | 110 | 2000 |
| 60 | 100 | 2000 |
| 80 | 90 | 400 |
| 100 | 80 | 400 |
| 150 | 45 | 400 |
| 200 | 37 | 400 |
| 250 | 37 | 400 |
| 350 | 37 | 400 |
| 500 | 37 | 400 |

## YDFLP-E-60-M7-M-R

E-M7 · 60 W · v1.0 2021 Table 5

| Pulse (ns) | Cut-off (kHz) | Max (kHz) |
| ---: | ---: | ---: |
| 2 | 1950 | 4000 |
| 4 | 1350 | 4000 |
| 6 | 975 | 4000 |
| 9 | 600 | 4000 |
| 13 | 412 | 3000 |
| 20 | 225 | 3000 |
| 30 | 187 | 3000 |
| 45 | 150 | 2000 |
| 60 | 135 | 2000 |
| 80 | 112 | 2000 |
| 100 | 105 | 1000 |
| 150 | 57 | 1000 |
| 200 | 45 | 1000 |
| 250 | 42 | 900 |
| 350 | 40 | 600 |
| 500 | 30 | 500 |

## YDFLP-E-80-M7-M-R

E-M7 · 80 W · JG-MCYF-SM-0039 / V00 2022 Table 5

| Pulse (ns) | Cut-off (kHz) | Max (kHz) |
| ---: | ---: | ---: |
| 2 | 2600 | 4000 |
| 4 | 1800 | 4000 |
| 6 | 1300 | 4000 |
| 9 | 800 | 4000 |
| 13 | 550 | 3000 |
| 20 | 330 | 3000 |
| 30 | 250 | 3000 |
| 45 | 200 | 2000 |
| 60 | 180 | 2000 |
| 80 | 150 | 2000 |
| 100 | 140 | 1000 |
| 150 | 76 | 1000 |
| 200 | 60 | 1000 |
| 250 | 56 | 900 |
| 350 | 53 | 600 |
| 500 | 53 | 500 |

## YDFLP-E-100-M7-M-R

E-M7 · 100 W · JG-MCYF-SM-0039 / V00 2022 Table 5

| Pulse (ns) | Cut-off (kHz) | Max (kHz) |
| ---: | ---: | ---: |
| 2 | 2960 | 4000 |
| 4 | 2160 | 4000 |
| 6 | 1400 | 4000 |
| 9 | 960 | 4000 |
| 13 | 680 | 3000 |
| 20 | 420 | 3000 |
| 30 | 300 | 3000 |
| 45 | 250 | 2000 |
| 60 | 200 | 2000 |
| 80 | 180 | 2000 |
| 100 | 160 | 1000 |
| 150 | 95 | 1000 |
| 200 | 75 | 1000 |
| 250 | 70 | 900 |
| 350 | 67 | 600 |
| 500 | 67 | 500 |

## YDFLP-E-200-M7-M-R

E-M7 · 200 W · JG-MCYF-SM-0039 v1.0 Table 5

Note: 2/4/6 ns: manual lists only >45/>70/>100 W at 4000 kHz

| Pulse (ns) | Cut-off (kHz) | Max (kHz) |
| ---: | ---: | ---: |
| 2 | 4000 | 4000 |
| 4 | 4000 | 4000 |
| 6 | 4000 | 4000 |
| 9 | 4000 | 4000 |
| 13 | 2600 | 3000 |
| 20 | 1700 | 3000 |
| 30 | 1100 | 3000 |
| 45 | 950 | 2000 |
| 60 | 650 | 2000 |
| 80 | 550 | 2000 |
| 100 | 480 | 1000 |
| 150 | 300 | 1000 |
| 200 | 240 | 1000 |
| 250 | 210 | 900 |
| 350 | 150 | 600 |
| 500 | 130 | 500 |

## YDFLP-E-200-M7-M-R (Performance mode)

E-M7 · 200 W · JG-MCYF-SM-0039 v1.0 Table 5

Note: 2/4/6 ns: manual lists only >50/>80/>120 W at 4000 kHz

| Pulse (ns) | Cut-off (kHz) | Max (kHz) |
| ---: | ---: | ---: |
| 2 | 4000 | 4000 |
| 4 | 4000 | 4000 |
| 6 | 4000 | 4000 |
| 9 | 4000 | 4000 |
| 13 | 2900 | 3000 |
| 20 | 1900 | 3000 |
| 30 | 1200 | 3000 |
| 45 | 1100 | 2000 |
| 60 | 720 | 2000 |
| 80 | 610 | 2000 |
| 100 | 530 | 1000 |
| 150 | 330 | 1000 |
| 200 | 270 | 1000 |
| 250 | 230 | 900 |
| 350 | 170 | 600 |
| 500 | 150 | 500 |

## YDFLP-E2-60-M7-M-R

E2-M7 · 60 W · E2-60 Table 4

| Pulse (ns) | Cut-off (kHz) | Max (kHz) |
| ---: | ---: | ---: |
| 2 | 1950 | 4000 |
| 4 | 1350 | 4000 |
| 6 | 975 | 4000 |
| 9 | 600 | 4000 |
| 13 | 412 | 3000 |
| 20 | 252 | 3000 |
| 30 | 187 | 3000 |
| 45 | 150 | 2000 |
| 60 | 135 | 2000 |
| 80 | 112 | 2000 |
| 100 | 105 | 1000 |
| 150 | 57 | 1000 |
| 200 | 48 | 1000 |
| 250 | 46 | 900 |
| 350 | 40 | 600 |
| 500 | 30 | 500 |

## YDFLP-E2-100-M7-M-R

E2-M7 · 100 W · E2-100 Table 5 (Normal mode)

| Pulse (ns) | Cut-off (kHz) | Max (kHz) |
| ---: | ---: | ---: |
| 2 | 2960 | 4000 |
| 4 | 2160 | 4000 |
| 6 | 1400 | 4000 |
| 9 | 960 | 4000 |
| 13 | 680 | 3000 |
| 20 | 420 | 3000 |
| 30 | 300 | 3000 |
| 45 | 250 | 2000 |
| 60 | 200 | 2000 |
| 80 | 180 | 2000 |
| 100 | 160 | 1000 |
| 150 | 95 | 1000 |
| 200 | 75 | 1000 |
| 250 | 70 | 900 |
| 350 | 67 | 600 |
| 500 | 67 | 500 |

## YDFLP-E2-200-M7-M-R

E2-M7 · 200 W · v2.2 Table 5

Note: 2/4/6 ns: manual lists only >35/>55/>90 W at 4000 kHz

| Pulse (ns) | Cut-off (kHz) | Max (kHz) |
| ---: | ---: | ---: |
| 2 | 4000 | 4000 |
| 4 | 4000 | 4000 |
| 6 | 4000 | 4000 |
| 9 | 3000 | 4000 |
| 13 | 2100 | 3000 |
| 20 | 1600 | 3000 |
| 30 | 1100 | 3000 |
| 45 | 700 | 2000 |
| 60 | 550 | 2000 |
| 80 | 450 | 2000 |
| 100 | 350 | 1000 |
| 150 | 300 | 1000 |
| 200 | 240 | 1000 |
| 250 | 210 | 900 |
| 350 | 150 | 600 |
| 500 | 130 | 500 |

## YDFLP-200-M7-L1-X

M7-L1 · 200 W · Version B 2018-09 Table 5

| Pulse (ns) | Cut-off (kHz) | Max (kHz) |
| ---: | ---: | ---: |
| 8 | 3000 | 4000 |
| 12 | 2000 | 4000 |
| 20 | 1200 | 3000 |
| 30 | 900 | 3000 |
| 40 | 700 | 3000 |
| 50 | 600 | 2000 |
| 60 | 550 | 2000 |
| 80 | 450 | 2000 |
| 100 | 350 | 2000 |
| 150 | 200 | 1000 |
| 200 | 150 | 1000 |
| 250 | 130 | 900 |
| 350 | 130 | 600 |
| 500 | 130 | 500 |

## YDFLP-20-M8-S-R

M8 · 20 W · V01 2021 Table 4

Note: setting 1 = CW

| Pulse (ns) | Cut-off (kHz) | Max (kHz) |
| ---: | ---: | ---: |
| 2 | 240 | 4000 |
| 4 | 160 | 4000 |
| 6 | 120 | 4000 |
| 9 | 85 | 4000 |
| 13 | 65 | 3000 |
| 20 | 50 | 3000 |
| 30 | 46 | 3000 |
| 45 | 42 | 2000 |
| 60 | 38 | 2000 |
| 80 | 36 | 2000 |
| 100 | 34 | 1000 |
| 150 | 24 | 1000 |
| 200 | 20 | 1000 |
| 250 | 18 | 900 |
| 350 | 18 | 600 |
| 500 | 18 | 500 |

## YDFLP-50-M8-M-R

M8 · 50 W · V01 Table 5 (machine-translated)

Note: setting 500 = CW; 250/350 ns need 10-35 C ambient

| Pulse (ns) | Cut-off (kHz) | Max (kHz) |
| ---: | ---: | ---: |
| 1 | 1500 | 4000 |
| 2 | 900 | 4000 |
| 4 | 560 | 4000 |
| 6 | 400 | 4000 |
| 9 | 300 | 4000 |
| 13 | 210 | 3000 |
| 20 | 150 | 3000 |
| 30 | 110 | 3000 |
| 45 | 90 | 2000 |
| 60 | 80 | 2000 |
| 80 | 70 | 2000 |
| 100 | 65 | 1000 |
| 150 | 24 | 1000 |
| 200 | 20 | 1000 |
| 250 | 17 | 900 |
| 350 | 12 | 600 |

## YDFLP-100-M8-M-R

M8 · 100 W · V01 2021-06-23 Table 4

| Pulse (ns) | Cut-off (kHz) | Max (kHz) |
| ---: | ---: | ---: |
| 6 | 280 | 4000 |
| 8 | 220 | 4000 |
| 12 | 170 | 3000 |
| 20 | 130 | 3000 |
| 30 | 110 | 3000 |
| 40 | 105 | 2000 |
| 50 | 100 | 2000 |
| 60 | 95 | 2000 |
| 80 | 90 | 2000 |
| 100 | 85 | 1000 |

## YDFLP-120-M8-S-W-V2

M8-V2 · 120 W · S-W-V2 Version 01 Table 5

| Pulse (ns) | Cut-off (kHz) | Max (kHz) |
| ---: | ---: | ---: |
| 6 | 210 | 4000 |
| 9 | 160 | 4000 |
| 12 | 125 | 3000 |
| 14 | 120 | 3000 |
| 16 | 115 | 3000 |
| 20 | 110 | 3000 |
| 30 | 90 | 3000 |
| 45 | 80 | 2000 |
| 60 | 150 | 2000 |
| 80 | 150 | 2000 |
| 100 | 150 | 1000 |
| 150 | 150 | 1000 |
| 200 | 150 | 1000 |

## YDFLP-200-M8-S-W-V2

M8-V2 · 200 W · S-W-V2 Version 01 Table 5

| Pulse (ns) | Cut-off (kHz) | Max (kHz) |
| ---: | ---: | ---: |
| 6 | 360 | 4000 |
| 9 | 280 | 4000 |
| 12 | 210 | 3000 |
| 14 | 200 | 3000 |
| 16 | 195 | 3000 |
| 20 | 180 | 3000 |
| 30 | 170 | 3000 |
| 45 | 165 | 2000 |
| 60 | 250 | 2000 |
| 80 | 250 | 2000 |
| 100 | 250 | 1000 |
| 150 | 250 | 1000 |
| 200 | 250 | 1000 |

## YDFLP-300-M8-S-W-V2

M8-V2 · 300 W · S-W-V2 Version 01 Table 5

| Pulse (ns) | Cut-off (kHz) | Max (kHz) |
| ---: | ---: | ---: |
| 6 | 540 | 4000 |
| 9 | 420 | 4000 |
| 12 | 345 | 3000 |
| 14 | 315 | 3000 |
| 16 | 295 | 3000 |
| 20 | 270 | 3000 |
| 30 | 255 | 3000 |
| 45 | 250 | 2000 |
| 60 | 375 | 2000 |
| 80 | 375 | 2000 |
| 100 | 375 | 1000 |
| 150 | 375 | 1000 |
| 200 | 375 | 1000 |

## YDFLP-E-20-LP-S

LP · 20 W · Version 02 Tables 4-5

Note: fixed 200 ns pulse

| Pulse (ns) | Cut-off (kHz) | Max (kHz) |
| ---: | ---: | ---: |
| 200 | 25 | 600 |

## YDFLP-E-30-LP-S

LP · 30 W · Version 02 Tables 4-5

Note: fixed 200 ns pulse

| Pulse (ns) | Cut-off (kHz) | Max (kHz) |
| ---: | ---: | ---: |
| 200 | 37 | 600 |

## YDFLP-E-50-LP-L

LP · 50 W · Version 02 Tables 4-5

Note: fixed 200 ns pulse

| Pulse (ns) | Cut-off (kHz) | Max (kHz) |
| ---: | ---: | ---: |
| 200 | 40 | 600 |

## Sources

Transcribed on 2026-11-01 from the data tables in the [LaserTips JPT M7 / M8 / LP Cut-off Calculator](https://lasertips.org/cutoff/) (reviewed by its author against JPT manuals on 2026-10-21). The values have not been re-checked against each manual page by page. PRs with corrections are welcome; please include the model code, manual revision and table number.

Manuals cited by LaserTips:

- [YDFLP M7 60/80/100/120 W, S-PI-0035 v1.0](https://www.scribd.com/document/658848434/YDFLP-6-V1)
- [YDFLP-E-80/100/200-M7-M-R v1.0](https://www.scribd.com/document/646069855/YDFLP-E-80-100-200-M7-M-R-User-manual-V1-0)
- [YDFLP-E-20/30-M7-S-R v1.4](https://chpukomplekt.ru/f/jpt_ydflp-e-2030-m7-s-r_user_manual_v14.pdf)
- [YDFLP-E-60-M7-M-R](https://device.report/manual/8463234)
- [YDFLP-E2-60-M7-M-R](https://www.h-part.com/api/product-assets/resources/jpt_ydflp_e2_60_m7_m_r/ydflp_e2_60_m7_m_r_user_manual)
- [YDFLP-E2-100-M7-M-R](https://www.scribd.com/document/845812360/Aurora-8-or-8-Pro-Ydflp-e2-100-m7-M-r-Laser-Source-User-Manual)
- [YDFLP-E2-200-M7-M-R v2.2](https://www.scribd.com/document/752890953/YDFLP-E2-200-M7-M-R-User-manual)
- [YDFLP-200-M7-L1-X Version B](https://cdck-file-uploads-us1.s3.dualstack.us-west-2.amazonaws.com/flex020/uploads/cloudray/original/1X/548b455036b6ddf267cf29572e83c53cebf6e909.pdf)
- [YDFLP-100-M8-M-R V01](https://haotianlasers.com/wp-content/uploads/2026/10/jpt-m8-100w-mopa-fiber-laser-source-manual-ydflp-100-m8-m-r.pdf)
- [YDFLP-M8-S-W-V2 120/200/300 W](https://haotianlasers.com/wp-content/uploads/2026/10/jpt-m8-120w-200w-300w-mopa-fiber-laser-source-manual-ydflp-m8-s-w-v2.pdf)
- [YDFLP-E-100-M7-M-R (Laser Everything archive)](https://db.lasereverything.net/api/files/download?path=%2Fmanuals_hardware%2Fsources_fiber%2Fjpt%2Fm7_e_series%2FYDFLP-E-100-M7-M-R.pdf)

Values come from manufacturer documentation and are given for reference only. Your controller, firmware and source revision can behave differently.
