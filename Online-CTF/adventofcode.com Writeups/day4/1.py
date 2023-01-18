import re

data = """
hcl:#6b5442 ecl:brn iyr:2019
pid:637485594 hgt:171cm
eyr:2021 byr:1986

eyr:2025 iyr:1938 byr:2014 hcl:#341e13
hgt:66cm
pid:70195175

hcl:#efcc98
iyr:2011 ecl:hzl
eyr:2020 hgt:174cm pid:589700330

hcl:#bba027 eyr:2027 cid:54
ecl:brn pid:153cm
iyr:2028 hgt:173cm
byr:2004

hcl:b45cec
iyr:2011 ecl:oth hgt:185cm eyr:2029 pid:178cm

hgt:185cm iyr:2016 eyr:2029 hcl:#888785 pid:026540921

eyr:2025
hcl:6962f7 byr:2015 ecl:oth iyr:1974
hgt:191cm
pid:2616015

pid:268398556 iyr:2019 ecl:grn
eyr:2027 byr:1951 hcl:#18171d hgt:67cm

eyr:2029 hgt:153cm ecl:brn pid:183179186 byr:2013 hcl:#623a2f
iyr:1957

cid:121 iyr:1922 hcl:752fbc pid:79577560 byr:2025
hgt:61cm eyr:1971

iyr:2016
eyr:2024 hcl:#18171d hgt:184cm
ecl:hzl byr:1992 pid:751161201

eyr:2021 ecl:blu byr:1938 iyr:2016 hcl:#b6652a pid:313406514 hgt:191cm

hcl:#623a2f eyr:2021
ecl:brn
pid:145249653 hgt:167cm iyr:2019 byr:1991

iyr:2022 pid:175cm
byr:2021 eyr:2027 ecl:#f615b1
hgt:172in hcl:#ceb3a1

hgt:173in
ecl:#0cba5e pid:1885981567 iyr:1968
byr:1952
eyr:1942

ecl:oth eyr:2023 hgt:65cm pid:521737908 byr:1971 hcl:z iyr:2017

byr:1936
hcl:#cfa07d
ecl:brn iyr:2011 pid:589047874
eyr:2025

hcl:#fffffd
pid:912552538
cid:159 hgt:160cm iyr:2012
eyr:2023 ecl:hzl
byr:1946

iyr:2015
ecl:amb hgt:72in
cid:59 pid:782818257 hcl:#18171d eyr:2026
byr:1952

hgt:173cm iyr:2018 cid:96 ecl:amb byr:1986 pid:783160698 eyr:2026
hcl:#602927

hcl:#a97842 cid:199 pid:912273414 eyr:2030
hgt:171cm ecl:hzl iyr:2011 byr:1960

ecl:amb hgt:156cm
iyr:2013
hcl:#ceb3a1
cid:116 pid:567057004 byr:1942
eyr:2029

ecl:#cddc40
pid:045090966 cid:254
hgt:75in hcl:#733820 eyr:2026 byr:1956
iyr:2015

pid:156cm
eyr:2040
hgt:176cm ecl:#02e67d hcl:b7c0e6
iyr:1959 cid:129 byr:2022

hgt:160cm byr:1933
ecl:blu eyr:2029 iyr:2012 hcl:#888785 pid:028571975

iyr:2017
hcl:#390f37 hgt:171cm ecl:brn byr:1931 pid:015365720 eyr:2030

iyr:2014 pid:697057757
eyr:2026 hgt:188cm
ecl:gry byr:1926

pid:484310015 hcl:#fffffd hgt:150cm iyr:2018
cid:53 ecl:gry eyr:2021 byr:1957

hgt:156cm
eyr:2026 byr:1963
pid:063272603 ecl:brn iyr:2011
hcl:#888785

byr:1955 pid:310518398 hgt:191cm iyr:2018
ecl:oth eyr:2023 cid:132 hcl:#888785

byr:1938 hcl:#623a2f eyr:2023
iyr:2010
hgt:165cm
pid:170304863
cid:290 ecl:amb

eyr:2026
pid:021468065 hgt:164cm
byr:1996 iyr:2016 hcl:#18171d
ecl:brn

byr:2027 ecl:oth pid:8258823391 hgt:153in hcl:#733820 eyr:1948

byr:2026 ecl:#cd275a iyr:2012 eyr:2036 pid:5917499975

byr:2004
cid:151
hcl:99ecb1
eyr:2033 pid:871137711 iyr:1997
hgt:184cm ecl:oth

byr:2011
hcl:z ecl:#eee1d2 hgt:59cm eyr:1925 iyr:2030 pid:#02ee78

pid:742658992
hcl:#888785
byr:1995
eyr:2024 hgt:162cm iyr:2013 cid:169 ecl:gry

hgt:152cm byr:1946
eyr:2027 iyr:2018
pid:352799678
hcl:#238da0
ecl:amb
cid:71

hcl:#623a2f pid:723616064 eyr:2021
hgt:172cm
byr:1926 iyr:2013
ecl:grn

iyr:2019 hgt:94 byr:2028 eyr:1986
pid:#ee7f00

ecl:amb
eyr:2027 pid:188153423 byr:1957 hcl:#d67ae1
iyr:2011 hgt:183cm

byr:1950 ecl:#e2495d iyr:2010 hgt:166cm eyr:2034 pid:151457075

eyr:1981
byr:2016 iyr:2029 pid:153cm ecl:#55c2a4 hcl:z
hgt:76cm

hgt:184cm ecl:amb eyr:2021
hcl:#623a2f
pid:414607669 iyr:1960 byr:2002

eyr:2027 iyr:2020 hgt:179cm byr:1991
pid:969568248
ecl:blu

hgt:175cm pid:536803427 hcl:#a97842 iyr:2012
ecl:grn byr:1950 eyr:2027

eyr:2028 hgt:60in hcl:#733820 iyr:2018 ecl:oth pid:871909483
byr:1930

hgt:155cm iyr:2020 byr:1960 eyr:2021
pid:515710074 ecl:amb hcl:#341e13

byr:1922 hcl:z iyr:1977 ecl:brn
eyr:2023 hgt:119 pid:865700639

ecl:gry hcl:959fcd pid:#633ac1
byr:2011 hgt:68in
eyr:2020

iyr:1972 hcl:z cid:149 byr:2020
hgt:166in pid:4548657 eyr:1960
ecl:#cc987c

eyr:2023 hcl:#b6652a iyr:2015
hgt:187in pid:547953710 byr:1979 ecl:grn

iyr:2018
pid:508691429 ecl:oth eyr:2025 hgt:187cm cid:270
hcl:#888785 byr:1977

hgt:168cm eyr:2032 byr:2020
ecl:gry iyr:1982
hcl:z pid:648015564

hcl:#fffffd pid:911858643 iyr:2016 ecl:gry eyr:2030 byr:1992 hgt:156cm

pid:241562994 eyr:2026 ecl:grn hgt:164cm
hcl:#c0946f byr:1945 iyr:2015 cid:296

byr:1976 pid:269322775 ecl:hzl
hgt:162cm hcl:#b6652a
eyr:2022 cid:335 iyr:2012

eyr:2028
hgt:106
pid:268626219 hcl:#a97842
iyr:2011
ecl:grn byr:1967

iyr:2016 hcl:#888785 hgt:193cm ecl:oth
pid:034099334 eyr:2027
byr:1945
cid:181

pid:248319556 byr:1987 iyr:2010 cid:122 ecl:utc
hcl:z hgt:190cm eyr:2030

iyr:2019 hcl:#ceb3a1
ecl:hzl
cid:281 hgt:73in byr:1992
eyr:2023

hcl:#fffffd
ecl:blu cid:340 hgt:176cm byr:1980 pid:809878309 iyr:2018

hgt:167cm hcl:#866857 byr:1973 cid:143 eyr:2030 iyr:2012
ecl:hzl pid:168618514

hcl:c97d76 iyr:2016 pid:8439355994 byr:2013 eyr:2036 hgt:71cm
cid:116 ecl:#055b62

hcl:#341e13 pid:961548527 eyr:2027 hgt:192cm byr:1940 iyr:2011 ecl:oth

byr:1935 hgt:189cm ecl:brn iyr:2012
eyr:2028 hcl:#602927

byr:2024
eyr:1939 iyr:2020 hgt:140 pid:889951037
hcl:#b6652a ecl:blu

ecl:amb byr:1942
iyr:2012 pid:161703003 hgt:181cm
eyr:2027 hcl:#602927

hcl:#18171d
iyr:2015 byr:1935
cid:204
ecl:gry
hgt:180cm eyr:2025 pid:988699528

eyr:2025 byr:1985
cid:192
hcl:#866857 hgt:150cm pid:315179208 iyr:2010 ecl:blu

hcl:#341e13 iyr:2013 eyr:2021 cid:62
byr:1928
hgt:168cm pid:862861470 ecl:hzl

pid:099158408
ecl:grn
eyr:2026 iyr:2018 hcl:#b6652a cid:81
hgt:185cm byr:1964

byr:1990 hgt:155cm
ecl:brn
eyr:2023
hcl:#ceb3a1 iyr:2012

ecl:brn
eyr:2026 cid:242 pid:658930205
hgt:176cm byr:1990 iyr:2016 hcl:#d55f68

hcl:#602927 pid:924899781
eyr:2024 byr:1964
iyr:2019
cid:163
hgt:181cm ecl:gry

eyr:2026 ecl:blu pid:8812414708 iyr:2017 hcl:#a97842 hgt:190cm
byr:1970

hgt:152cm
pid:403682313 iyr:2019
hcl:#ceb3a1 ecl:oth
eyr:2021 byr:1957

pid:23799214
byr:2030 hgt:66cm
iyr:2022
hcl:z ecl:#c806fe eyr:2035

eyr:2022 hgt:177cm byr:1967 cid:194
pid:060293594
ecl:brn
iyr:2016
hcl:#cfa07d

hgt:184cm hcl:#6b5442 eyr:2029
ecl:oth iyr:2013 pid:26983291 byr:1965
cid:147

pid:255519852 byr:1975 hgt:192cm
ecl:lzr
iyr:2015 eyr:2030
hcl:#623a2f

iyr:2010
ecl:blu
hcl:#881267 hgt:162cm pid:121130250 byr:1935 cid:57 eyr:2025

hgt:189cm
hcl:#a97842
iyr:2014 eyr:2024
ecl:brn
pid:972960330

hcl:#623a2f eyr:2026 hgt:193cm cid:87 byr:1982 iyr:2020 pid:158154062 ecl:amb

eyr:2025 hgt:191cm
ecl:amb
hcl:#341e13
pid:137048981 iyr:2016 byr:1950

byr:1930 eyr:2029 ecl:hzl hgt:75in
pid:464272185 cid:341
iyr:2012 hcl:#c0946f

ecl:brn
pid:952709301 byr:1926 hcl:#c0946f
eyr:2028
hgt:170cm

pid:578940518 byr:2025 hgt:190in
iyr:2030 cid:52 ecl:amb eyr:2027

ecl:amb hgt:185cm cid:237 iyr:2016 pid:490377510 byr:1950 hcl:#18171d
eyr:2025

iyr:2014 hgt:156in pid:65952131
ecl:blu byr:1938 hcl:#7d3b0c
eyr:2023

ecl:gry iyr:2016 pid:818347623 hcl:#888785 eyr:2030 hgt:174cm

ecl:hzl
hcl:#866857
eyr:2027
pid:213124752 hgt:179cm
byr:1989

pid:024846371 byr:1990 iyr:2018
eyr:2026 hgt:161cm ecl:oth

hcl:z hgt:129 iyr:2016
eyr:2034
pid:#b85e75 byr:2026 ecl:oth

hgt:192cm hcl:#602927 ecl:blu iyr:2011
pid:863613568 byr:1996 eyr:2027

hgt:160cm cid:229 byr:1952
iyr:2019
ecl:#0ae2d6 eyr:2027 pid:719697407 hcl:z

pid:040987502 cid:155 iyr:2012 hgt:173cm
byr:2002
hcl:#fffffd eyr:2023 ecl:hzl

ecl:oth byr:1993 iyr:2019 pid:319157251 hcl:#733820 hgt:70in eyr:2027

hcl:#9d85d4
hgt:192cm pid:570514935
cid:238 eyr:2022 ecl:gry byr:1989
iyr:2016

hgt:162cm
cid:201 iyr:2015 eyr:2023 pid:553794028 byr:1922 ecl:amb hcl:#623a2f

cid:56
eyr:2024 ecl:amb hgt:179cm hcl:#efcc98
pid:665225721
iyr:2012 byr:1963

byr:2026
hcl:#888785
iyr:1972 eyr:1980 cid:323 pid:153cm
hgt:170cm ecl:blu

pid:704204892 ecl:gry
eyr:2023
byr:1920 hgt:168cm iyr:2010 hcl:#3311ec

pid:#7f3caf eyr:2023
hcl:z hgt:146 byr:1990 ecl:amb
iyr:2014 cid:270

hgt:171cm ecl:blu pid:383695713
cid:200 iyr:2010
hcl:#602927 byr:1950 eyr:2024

hgt:178cm byr:1935 hcl:#2da7db
pid:597509269
eyr:2020 iyr:2014
ecl:blu

eyr:2034
ecl:#d4719a
hcl:z hgt:67cm iyr:2023 pid:#268d93 byr:2006

eyr:1939 pid:9942171839
hgt:104
iyr:1945
byr:2011 ecl:#f9bafb hcl:#ceb3a1

byr:1937
iyr:2010 pid:979528684
eyr:2028 hcl:#ceb3a1 ecl:gry hgt:164cm

iyr:2019 eyr:2022 pid:044485658 hcl:#18171d byr:1996 hgt:169cm
ecl:gry

pid:031482456
eyr:2024
iyr:2015
hgt:157cm hcl:#7d3b0c byr:1921
ecl:oth

pid:399398768
ecl:lzr
hcl:z
eyr:1983 hgt:68cm
byr:2024 iyr:2027 cid:127

hgt:186cm eyr:2026 pid:140032921 ecl:amb cid:278
byr:1937 iyr:2015

hgt:172cm
ecl:amb pid:718725983 hcl:#6b5442 eyr:2024
iyr:2013 byr:1974

ecl:amb iyr:2014 cid:216 hcl:#cfa07d
eyr:2022 pid:442275714 hgt:68in byr:1999

hgt:152cm cid:193
iyr:2015 pid:806672342 hcl:#b6652a byr:1927 ecl:oth

hcl:#7d3b0c byr:1925 iyr:2015 hgt:174cm pid:888044223 cid:168 ecl:oth eyr:2029

ecl:gry byr:2009 hgt:156cm
hcl:#888785 pid:263500722 iyr:2015 eyr:2021

cid:103
hcl:#ba8b89 ecl:hzl hgt:169cm
byr:1929 pid:626102979 iyr:2016 eyr:2028

iyr:2016 hgt:188cm cid:133
byr:1926 ecl:hzl eyr:2023 hcl:#602927 pid:678092780

ecl:utc byr:2025 pid:#584dc1 eyr:2037
hgt:151cm iyr:1950 hcl:#cfa07d

ecl:oth hgt:140 eyr:1977 hcl:#6b5442 iyr:1955
byr:1999
pid:868434068

eyr:2029 hcl:#18171d cid:158 iyr:2016 hgt:166cm ecl:hzl
pid:100226690 byr:1942

ecl:#806ce8
cid:153 iyr:2024 byr:1985 hcl:da8a68
pid:#d9e5b0 eyr:2017

eyr:2020 hgt:164cm cid:222 ecl:hzl byr:1945 hcl:#cfa07d
iyr:2011

iyr:2018 hgt:165cm
pid:868536448 eyr:2026 byr:1930
ecl:hzl hcl:#623a2f cid:128

ecl:grn iyr:2012
cid:326 byr:1950 hcl:#efcc98 eyr:2029 hgt:177cm pid:685629972

byr:2004 hgt:168cm
ecl:dne iyr:2020 hcl:z

byr:1964 pid:132604237 ecl:oth hcl:#602927 hgt:188cm
cid:78
iyr:2012 eyr:2025

byr:1945
iyr:2023 ecl:#1a590c hgt:70in
pid:186cm eyr:2031 hcl:z

cid:178
ecl:amb eyr:2024 hgt:162cm
hcl:#18171d iyr:2016
byr:1945 pid:737813370

hcl:#18171d
byr:1949
pid:064917719
hgt:176cm ecl:amb
eyr:2034
iyr:1998

hgt:72in
pid:711343766 hcl:#623a2f
iyr:2010 byr:1977 ecl:amb cid:177 eyr:2023

byr:1933 hgt:66 pid:22149379 eyr:2040
ecl:#92d7a7 hcl:#cfa07d

iyr:2020 byr:1946 eyr:2020 ecl:hzl pid:153cm
hgt:159cm cid:261 hcl:#888785

iyr:2013 byr:1931
ecl:#2ced2e hcl:3c49c1 eyr:1950
hgt:182cm cid:133 pid:#19fc55

hcl:#a9abe6
iyr:2016
eyr:2029 ecl:hzl cid:343 pid:691253232 byr:1952 hgt:187cm

hcl:z
eyr:1964
ecl:#5995e6
byr:2021 hgt:72in pid:2103603035 iyr:1951

iyr:2024 hgt:151in byr:1988 ecl:blu
eyr:1961 cid:117
hcl:z pid:5371118784

hgt:71cm iyr:2021
eyr:2033 ecl:amb
hcl:z cid:202
pid:207141921 byr:1987

ecl:gry byr:1927 eyr:2024
hgt:60in iyr:2014
pid:847799723 cid:285
hcl:#733820

eyr:2022 hcl:#18171d
pid:847063261
byr:1926 ecl:grn
iyr:2011

pid:647225630 iyr:2016 hcl:#a97842 ecl:oth eyr:2025
cid:144 hgt:182cm byr:1983

hgt:150 byr:1924
eyr:2024 hcl:1600da
ecl:brn
cid:168 pid:656253964

hgt:153in pid:644514788 byr:1956 hcl:#866857
iyr:2029
ecl:utc

cid:57 pid:755541617 byr:1961
iyr:2019
ecl:grn
hgt:169cm hcl:#efcc98 eyr:2029

iyr:2005
eyr:2040 hcl:8080a4 byr:2013 pid:145803668

iyr:2029
hcl:z ecl:brn
byr:1948
hgt:76cm pid:186cm eyr:2031

hcl:#888785 ecl:grn byr:1983 cid:268 pid:402246959 iyr:2018
eyr:2020

hgt:175cm eyr:2026 pid:594997236
byr:1991 hcl:#ceb3a1 iyr:2015 ecl:blu

byr:1989
eyr:2027
iyr:2020 hgt:192cm ecl:blu hcl:#cfa07d cid:61 pid:657979353

pid:#a043a3 iyr:2016 byr:1947
eyr:2031 hgt:191cm ecl:xry

eyr:2023 ecl:blu byr:1948 cid:128 hgt:74in
pid:966094274
iyr:2015

iyr:2020 ecl:zzz
eyr:1999 hcl:3cf716 byr:2017 cid:343 pid:60198759
hgt:70cm

hgt:182 pid:80897411 byr:2014 eyr:2033 iyr:1941 ecl:#9c54e8 cid:107
hcl:z

iyr:2015 hcl:#866857 byr:1990 cid:167 pid:588340506 eyr:2030 hgt:168cm ecl:oth

hcl:676aad hgt:151 cid:192 eyr:1930 ecl:oth byr:2012
pid:513365039
iyr:1943

cid:119
ecl:#921980 hgt:70cm
eyr:2024 hcl:4909ee pid:#13fe6c iyr:2022 byr:2014

eyr:2036 hcl:02fdbc hgt:155cm
iyr:1946
pid:508011940 ecl:utc byr:2025

pid:#f74bbe eyr:2028 hcl:#c0946f hgt:171cm ecl:#9077c0
byr:1951 iyr:2010

iyr:2017 hgt:125 hcl:#cfa07d pid:731062033 ecl:brn eyr:2028 cid:255 byr:2020

ecl:xry eyr:2033 byr:1978
iyr:2012 hgt:70cm hcl:z
pid:272848084

ecl:blu hgt:174cm
eyr:2030 byr:1999 hcl:#ceb3a1 iyr:2015
pid:322583115 cid:301

eyr:2007 byr:2007
ecl:dne cid:322 pid:182cm iyr:2013 hgt:156in
hcl:680e8c

hgt:189cm hcl:#18171d
byr:1996 ecl:amb
eyr:2022 iyr:2020 pid:470853813

pid:785152983 iyr:2014 eyr:2028 hcl:#d50ced ecl:hzl byr:1998

ecl:hzl byr:1945 hcl:#7d3b0c cid:164 hgt:187cm pid:414181589 iyr:2018

byr:1936
hgt:183cm ecl:gry pid:376279728 hcl:#7d3b0c
eyr:2023 iyr:2012

byr:2000 hgt:157cm
ecl:hzl
iyr:2020
pid:203994583
eyr:2023 hcl:#866857

eyr:1992 byr:2009
iyr:2029
hcl:dc80b3 hgt:70cm ecl:grn pid:#65c31d

hcl:#7d3b0c
byr:1945
hgt:177cm
iyr:2013 eyr:2028 pid:038116668 cid:74 ecl:blu

pid:700997508 eyr:1970 ecl:zzz hcl:#888785 iyr:2013 byr:1986 cid:219 hgt:76cm

eyr:2025 hgt:161cm
iyr:2015 cid:188
hcl:#fffffd
pid:840085402 ecl:gry byr:1988

pid:96550914 hcl:#481a3b byr:1997 ecl:#a57167
cid:274 hgt:174cm

hcl:#b6652a
ecl:brn eyr:2029
hgt:157cm iyr:2011 pid:910022061
byr:1947 cid:273

pid:010289131 eyr:2026
byr:1930
hcl:#b6652a ecl:grn
cid:220 hgt:187cm iyr:2013

hcl:#6b5442 ecl:grt hgt:120
pid:454504291 eyr:1933 byr:2025 iyr:1930

iyr:2016
hgt:180cm ecl:amb eyr:2028 cid:237
pid:334803890 byr:1953 hcl:#18171d

eyr:2020 byr:2002 hcl:#c54f21
iyr:2019 ecl:blu hgt:180cm cid:138

byr:1933
iyr:2020
ecl:brn hgt:185cm
hcl:#c0946f
eyr:2020 pid:050791974

byr:1933 ecl:brn hgt:186cm
pid:643899463 eyr:2030 iyr:2019
hcl:#866857

iyr:2018 byr:1935 ecl:oth
eyr:2029
pid:732801213 hcl:#6b5442 hgt:169cm

eyr:2020
hcl:z byr:1996
ecl:#4102ee
pid:890541531 hgt:193cm iyr:2014

pid:618379341 ecl:gry hcl:#18171d byr:1991 eyr:2025 hgt:154cm iyr:2019

iyr:2013
pid:912066964 ecl:grn eyr:2040 hgt:192cm byr:1974
hcl:#18171d

eyr:2025 cid:167 hgt:192cm
pid:678328147 ecl:gry
hcl:#18171d iyr:2017

iyr:2011 byr:2021 hgt:189cm ecl:gmt hcl:z eyr:2035 pid:278839955

eyr:2030 hcl:#efcc98
ecl:blu iyr:2011
pid:536958012 hgt:192cm byr:2002

pid:#1306f2 byr:1976
hcl:#790688 hgt:158cm ecl:grn eyr:2024 iyr:2019

eyr:2030 hcl:#866857
cid:50 ecl:oth pid:421235317
iyr:2014 hgt:60in

iyr:2020 byr:1971 cid:124
pid:319896110 ecl:oth hcl:#fffffd

cid:143
eyr:2021 hgt:190cm pid:366021385 hcl:#18171d ecl:amb byr:1934
iyr:2016

hgt:169cm hcl:#602927 pid:177cm
eyr:2022 byr:2020 ecl:#dd96f4 iyr:2014

eyr:2020 hgt:173cm pid:591592395 ecl:oth byr:1966
hcl:#c0946f iyr:2020

pid:282088832 ecl:gmt
hgt:167in byr:2016 hcl:z
iyr:2018

iyr:2016
hgt:62in hcl:#c0946f
pid:306204399 eyr:2020 ecl:brn
byr:1999

eyr:1947 byr:1984 pid:595671246 hcl:3d50e7 ecl:xry iyr:1947

hgt:187cm
eyr:2024 pid:477011496
byr:1971
hcl:#733820
iyr:2010
ecl:brn cid:165

byr:2023
pid:173cm
hgt:193in eyr:2019 cid:102 ecl:grt hcl:#c0946f

pid:195062251
iyr:2027
cid:138 byr:2021 ecl:brn eyr:2025 hgt:60in

hgt:71cm hcl:z
ecl:utc
eyr:2021 iyr:1925 pid:5469028726 byr:2017

hcl:#b6652a hgt:168cm
byr:1960 ecl:grn
pid:653140418
iyr:2014 eyr:2023

pid:#afa892 cid:190 hcl:z
hgt:189cm
eyr:2020 ecl:gry
byr:2003
iyr:1956

hcl:e4cddf cid:185 pid:189cm hgt:175cm
byr:2016 iyr:2010 ecl:#fa945d eyr:1947

cid:176
hcl:7752f8 eyr:2039 byr:2019 ecl:hzl iyr:2029 hgt:185cm pid:636534364

cid:170 ecl:gmt hcl:ef5177 byr:2021
eyr:1993
hgt:71cm pid:2136295 iyr:2013

byr:2028 pid:156cm hcl:d74b86 cid:238
hgt:89
iyr:1957 eyr:1937

eyr:2030 byr:1932 hcl:#c0946f cid:349
hgt:177cm
ecl:grn iyr:2016

hcl:z byr:2003
ecl:#9b98b2 hgt:81 pid:13338103 eyr:2040

iyr:2018 pid:801432704 hgt:73in byr:1964 cid:298 hcl:#fffffd ecl:amb eyr:2030

cid:272
iyr:2019 pid:369160624 byr:1929 hgt:184cm eyr:2025 hcl:#ceb3a1 ecl:blu

hcl:#7d3b0c pid:525287934
byr:1998 eyr:2027
iyr:2017 hgt:168cm ecl:gry

byr:1975 eyr:2027
ecl:brn cid:125 hcl:4e319d
hgt:172cm pid:308046532 iyr:2017

hcl:b889c0 pid:6699675552 byr:2019 iyr:1968
ecl:gmt
eyr:2003
hgt:180in

byr:2025
ecl:zzz hgt:162in hcl:z iyr:2002 pid:#87dca4 eyr:1951

eyr:2022
pid:549517742 ecl:hzl
iyr:2026
byr:2029 hgt:153cm hcl:2993de

eyr:2024
pid:755674604 iyr:2018 hcl:#c0946f
ecl:gry byr:1966
hgt:188cm

pid:665375893 iyr:2017
byr:1997
eyr:2029 hgt:173cm ecl:gry

hcl:#6b5442 hgt:74cm ecl:#0dc7f6
pid:451038742 eyr:1982 byr:1939
iyr:1932

hcl:#18171d
byr:1980 ecl:gry
iyr:2019 hgt:167cm
pid:326267989 eyr:2028

cid:226 hgt:177cm ecl:hzl hcl:#a97842 eyr:2025
iyr:2013
byr:1949 pid:292166795

ecl:oth pid:962521763
iyr:2013 cid:71 eyr:2022 hgt:193cm hcl:#18171d byr:1969

ecl:grn iyr:2028 eyr:2024
hgt:189cm hcl:z byr:1940 pid:032392876

iyr:2012 hgt:191cm cid:339 ecl:oth eyr:2028 pid:392810631 hcl:#b6652a byr:1959

iyr:2011 byr:1975
eyr:2027
hcl:#18171d
hgt:176cm
ecl:gry pid:290432747

cid:180 ecl:brn pid:210871734 eyr:2027
byr:1946 hcl:z hgt:185cm iyr:2011

byr:1924 ecl:grt
eyr:2028 hgt:187cm pid:#608f4f

eyr:2022 ecl:#a05063 byr:1926 hcl:#7d3b0c pid:3292990618 hgt:183in iyr:2021

ecl:#a8b66c
iyr:1942 eyr:1960 hgt:60cm byr:2027 pid:#3b6f3f hcl:9fae56

hgt:183cm
ecl:oth hcl:#c0946f pid:816986054 eyr:2020 iyr:2014 byr:1935

hgt:174 byr:2008
iyr:2029 hcl:9259e7 pid:85036214 ecl:gmt

cid:85
pid:032040868
byr:2001 eyr:2027 hcl:#c0946f ecl:grn iyr:2020
hgt:173cm

hcl:#6b5442
cid:308
ecl:grt iyr:1939 byr:2009
pid:9365125584 eyr:2031 hgt:67cm

hgt:154cm
byr:1936
eyr:2030 hcl:491c70 pid:391887956 iyr:2029 ecl:blu

hcl:#866857
hgt:161cm cid:76 pid:921202500 eyr:2021 ecl:brn byr:1968

iyr:2024 ecl:dne hcl:z pid:8054447805 hgt:154 eyr:2035 byr:2024

hcl:#0a524b pid:667928918
eyr:2025
cid:245 ecl:brn byr:1973 hgt:179cm

ecl:gry hgt:68in pid:322837855 eyr:2023
cid:323 byr:1944
iyr:2012

byr:1940
hgt:178cm ecl:hzl hcl:#c0946f iyr:2030
eyr:2020 pid:788531859

cid:253 iyr:2012 hgt:163cm
pid:554364568 eyr:2025 byr:1976 ecl:grn hcl:#888785

hcl:#efcc98 iyr:2015 ecl:gry eyr:2029 pid:273847553 cid:274
hgt:68in byr:1933

hgt:165cm
pid:209462386 eyr:2024
byr:1969 hcl:#733820 ecl:grn
iyr:2020

byr:1975 hgt:187cm eyr:2027 iyr:2018 hcl:#c0946f ecl:hzl pid:141969110

hcl:z pid:534439483 iyr:2022 ecl:grt eyr:2036 hgt:164in cid:324
byr:2025

hcl:#74ca66
iyr:2011
pid:253012158
hgt:188cm
cid:246 ecl:oth eyr:2023

byr:2020 pid:56939101 hcl:9f5f65
eyr:1949
iyr:2021 hgt:155in

iyr:2020 hgt:174cm cid:304
byr:1944
eyr:2028 hcl:#733820

hcl:#866857 ecl:gry eyr:2030 iyr:2014 hgt:63in byr:1997
pid:371522079

ecl:amb
byr:1955 iyr:2013
hcl:#888785 cid:265 eyr:2026 hgt:190cm pid:311393763

eyr:2026 iyr:2019
pid:721355771 byr:1947
hcl:#733820
hgt:71in ecl:gry

cid:94 eyr:2024 byr:1938 pid:336868233 ecl:hzl
iyr:2012
hgt:177cm hcl:#7d3b0c

ecl:brn iyr:2010
eyr:2027
pid:379769214
cid:111 byr:1960 hcl:#cfa07d hgt:169cm

hgt:179cm
hcl:3f59a6 eyr:2036 byr:2025 ecl:oth pid:217404607
iyr:2018

ecl:amb pid:820370865 hgt:170cm iyr:2012 byr:1967 hcl:#efcc98 cid:309 eyr:2025

byr:1940
pid:008495978 ecl:gry hgt:159cm hcl:#602927 eyr:2024

hgt:186cm
byr:1971 pid:556900517 cid:334 hcl:#efcc98 ecl:brn
iyr:2014

iyr:2020 byr:1928
cid:200 hgt:193cm
ecl:grn hcl:#7d3b0c

cid:233
hcl:a3046e pid:626863952 ecl:lzr iyr:2029 eyr:2024 byr:2000 hgt:193cm

cid:244
hcl:#866857 ecl:amb byr:1931
eyr:1928 pid:557376401 hgt:182cm iyr:2013

"""


# Solving day1
key_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

data = data.strip('\n').split("\n\n")
total = 0
for item in data:
	if all(i in item for i in key_list):
		total += 1

print('day1', total)


# Solving day2
import re 


def min_max_int_validator(value, min_value, max_value, digits=4):
	try:
		if len(value) != digits:
			return False
		value = int(value)
		return min_value <= value <= max_value
	except:
		return False


def height_validator(value, metric='cm'):
	try:
		metric = 'in' if 'in' in value else 'cm'
		value = value.replace('cm', '').replace('in', '')
		value = int(value)
		if metric == 'cm':
			return 150 <= value <= 193
		else:
			return 59 <= value <= 76
	except Exception as e:
		print(e)
		return False

def hair_color_validator(value):
	try:
		value = str(value).lower()
		regex = "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
		x = re.search(regex, value)
		return True if x else False
	except:
		return False


def eye_color_validator(value):
	return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def pid_validator(value):
	try:
		return len(value) == 9 and int(value)
	except:
		return False

total = 0
for item in data:
	if all(i in item for i in key_list):
		# This is a valid passport based on day1. now try to validate each field value
		item = item.replace("\n", " ").split(' ')
		d = {}
		for i in item:
			d[i.split(':')[0]] = i.split(':')[1]

		if 'byr' in d.keys() and not min_max_int_validator(d['byr'], 1920, 2002):
			continue
		
		if 'iyr' in d.keys() and not min_max_int_validator(d['iyr'], 2010, 2020):
			continue
		
		if 'eyr' in d.keys() and not min_max_int_validator(d['eyr'], 2020, 2030):
			continue

		if 'hgt' in d.keys() and not height_validator(d['hgt']):
			continue

		if 'hcl' in d.keys() and not hair_color_validator(d['hcl']):
			continue

		if 'ecl' in d.keys() and not eye_color_validator(d['ecl']):
			continue

		if 'pid' in d.keys() and not pid_validator(d['pid']):
			continue

		total += 1

print('day2', total)
