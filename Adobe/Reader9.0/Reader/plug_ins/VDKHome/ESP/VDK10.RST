$control: 1
descriptor:
{
  data-table:	rsf
    /offset      = 0
    /num-records = 145
    /priority    = MEDIUM
  {
    constant:	LOCALE	text "english"
    varwidth:	M2 rsv
      /offset = 0
      /max-file-size = 0xFFF0
    fixwidth:	M2_SZ 2 signed-integer
    fixwidth:	M2_OF 2 unsigned-integer
  }
  data-table:	rsf
    /offset      = 580
    /num-records = 59
    /priority    = MEDIUM
  {
    varwidth:	M1 rsv
      /offset = 4374
      /max-file-size = 0xFFF0
    fixwidth:	M1_SZ 2 signed-integer
    fixwidth:	M1_OF 2 unsigned-integer
  }
  data-table:	rsf
    /offset      = 816
    /num-records = 245
    /priority    = MEDIUM
  {
    varwidth:	M0 rsv
      /offset = 4636
      /max-file-size = 0xFFF0
    fixwidth:	M0_SZ 2 signed-integer
    fixwidth:	M0_OF 2 unsigned-integer
  }
  data-table:	rsf
    /offset      = 1796
    /num-records = 213
    /priority    = MEDIUM
  {
    varwidth:	E3 rsv
      /offset = 8970
      /max-file-size = 0xFFF0
    fixwidth:	E3_SZ 2 signed-integer
    fixwidth:	E3_OF 2 unsigned-integer
  }
  data-table:	rsf
    /offset      = 2648
    /num-records = 207
    /priority    = MEDIUM
  {
    varwidth:	E2 rsv
      /offset = 18417
      /max-file-size = 0xFFF0
    fixwidth:	E2_SZ 2 signed-integer
    fixwidth:	E2_OF 2 unsigned-integer
  }
  data-table:	rsf
    /offset      = 3476
    /num-records = 166
    /priority    = MEDIUM
  {
    varwidth:	E1 rsv
      /offset = 28051
      /max-file-size = 0xFFF0
    fixwidth:	E1_SZ 2 signed-integer
    fixwidth:	E1_OF 2 unsigned-integer
  }
  data-table:	rsf
    /offset      = 4140
    /num-records = 431
    /priority    = MEDIUM
  {
    varwidth:	E0 rsv
      /offset = 33965
      /max-file-size = 0xFFF0
    fixwidth:	E0_SZ 2 signed-integer
    fixwidth:	E0_OF 2 unsigned-integer
  }
}
$$
