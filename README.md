### OS X

    $ brew install imagemagick
    $ pip install -r requirements.txt

### Test run

Run on my MacBook Air. Output from `system_profiler`:

      Model Name: MacBook Air
      Model Identifier: MacBookAir4,2
      Processor Name: Intel Core i5
      Processor Speed: 1,7 GHz
      Number of Processors: 1
      Total Number of Cores: 2
      L2 Cache (per Core): 256 KB
      L3 Cache: 3 MB

Time:

    $ time python stroll.py > out.txt

    real0m4.265s
    user0m4.746s
    system_profiler0m1.850s

Metrics:

    $ cat out.txt
    0 undefined: 0.219870921748
    0 absolute_error: 49567.0
    0 mean_absolute_error: 0.0835573423202
    0 mean_error_per_pixel: 825430801.0
    0 mean_squared_error: 0.0214286530978
    0 peak_absolute_error: 1.0
    0 peak_signal_to_noise_ratio: 16.6900512577
    0 root_mean_squared_error: 0.146385289895
    0 normalized_cross_correlation_error: 0.219870921748
    0 fuzz_error: 0.146385289895
    1 undefined: 0.442307779813
    1 absolute_error: 45871.0
    1 mean_absolute_error: 0.0436480229688
    1 mean_error_per_pixel: 431182007.0
    1 mean_squared_error: 0.00696530001777
    1 peak_absolute_error: 0.980392156863
    1 peak_signal_to_noise_ratio: 21.5706017238
    1 root_mean_squared_error: 0.0834583729639
    1 normalized_cross_correlation_error: 0.442307779813
    1 fuzz_error: 0.0834583729639
    2 undefined: 0.608844157163
    2 absolute_error: 46601.0
    2 mean_absolute_error: 0.0393376743286
    2 mean_error_per_pixel: 388601733.0
    2 mean_squared_error: 0.00663790136126
    2 peak_absolute_error: 0.992156862745
    2 peak_signal_to_noise_ratio: 21.7796920546
    2 root_mean_squared_error: 0.0814733168667
    2 normalized_cross_correlation_error: 0.608844157163
    2 fuzz_error: 0.0814733168667
    3 undefined: 0.33898724879
    3 absolute_error: 45708.0
    3 mean_absolute_error: 0.0407222348399
    3 mean_error_per_pixel: 402279273.0
    3 mean_squared_error: 0.00782645541822
    3 peak_absolute_error: 0.996078431373
    3 peak_signal_to_noise_ratio: 21.0643488428
    3 root_mean_squared_error: 0.0884672561925
    3 normalized_cross_correlation_error: 0.33898724879
    3 fuzz_error: 0.0884672561925
    4 undefined: 0.526372264682
    4 absolute_error: 50136.0
    4 mean_absolute_error: 0.0488817501552
    4 mean_error_per_pixel: 482883982.0
    4 mean_squared_error: 0.00597308347888
    4 peak_absolute_error: 1.0
    4 peak_signal_to_noise_ratio: 22.2380141558
    4 root_mean_squared_error: 0.0772857262299
    4 normalized_cross_correlation_error: 0.526372264682
    4 fuzz_error: 0.0772857262299
    5 undefined: 0.265271360271
    5 absolute_error: 50129.0
    5 mean_absolute_error: 0.0490381571037
    5 mean_error_per_pixel: 484429066.0
    5 mean_squared_error: 0.00724763881044
    5 peak_absolute_error: 1.0
    5 peak_signal_to_noise_ratio: 21.3980345807
    5 root_mean_squared_error: 0.085133065318
    5 normalized_cross_correlation_error: 0.265271360271
    5 fuzz_error: 0.085133065318
    6 undefined: 0.227636241144
    6 absolute_error: 47986.0
    6 mean_absolute_error: 0.0260852813309
    6 mean_error_per_pixel: 257686447.0
    6 mean_squared_error: 0.00469825625678
    6 peak_absolute_error: 1.0
    6 peak_signal_to_noise_ratio: 23.2806329921
    6 root_mean_squared_error: 0.0685438272697
    6 normalized_cross_correlation_error: 0.227636241144
    6 fuzz_error: 0.0685438272697
    7 undefined: 0.302941107107
    7 absolute_error: 46963.0
    7 mean_absolute_error: 0.0265901958443
    7 mean_error_per_pixel: 262674303.0
    7 mean_squared_error: 0.00527634942146
    7 peak_absolute_error: 1.0
    7 peak_signal_to_noise_ratio: 22.7766645141
    7 root_mean_squared_error: 0.0726384844381
    7 normalized_cross_correlation_error: 0.302941107107
    7 fuzz_error: 0.0726384844381
    8 undefined: 0.49412754487
    8 absolute_error: 45526.0
    8 mean_absolute_error: 0.0259217460552
    8 mean_error_per_pixel: 256070945.0
    8 mean_squared_error: 0.00526578843776
    8 peak_absolute_error: 1.0
    8 peak_signal_to_noise_ratio: 22.7853659342
    8 root_mean_squared_error: 0.0725657525129
    8 normalized_cross_correlation_error: 0.49412754487
    8 fuzz_error: 0.0725657525129
    9 undefined: 0.488665924094
    9 absolute_error: 46746.0
    9 mean_absolute_error: 0.0299196190039
    9 mean_error_per_pixel: 295564392.0
    9 mean_squared_error: 0.00502946535979
    9 peak_absolute_error: 1.0
    9 peak_signal_to_noise_ratio: 22.9847817869
    9 root_mean_squared_error: 0.0709187236193
    9 normalized_cross_correlation_error: 0.488665924094
    9 fuzz_error: 0.0709187236193
    10 undefined: 0.499157236322
    10 absolute_error: 50245.0
    10 mean_absolute_error: 0.0634089950645
    10 mean_error_per_pixel: 626393039.0
    10 mean_squared_error: 0.0104928365029
    10 peak_absolute_error: 0.996078431373
    10 peak_signal_to_noise_ratio: 19.7910709417
    10 root_mean_squared_error: 0.102434547409
    10 normalized_cross_correlation_error: 0.499157236322
    10 fuzz_error: 0.102434547409
    11 undefined: 0.67627235039
    11 absolute_error: 50235.0
    11 mean_absolute_error: 0.0588304496127
    11 mean_error_per_pixel: 581163352.0
    11 mean_squared_error: 0.0105139100095
    11 peak_absolute_error: 0.980392156863
    11 peak_signal_to_noise_ratio: 19.7823574451
    11 root_mean_squared_error: 0.102537359092
    11 normalized_cross_correlation_error: 0.67627235039
    11 fuzz_error: 0.102537359092
    12 undefined: 0.554534400101
    12 absolute_error: 49658.0
    12 mean_absolute_error: 0.0635356139298
    12 mean_error_per_pixel: 627643858.0
    12 mean_squared_error: 0.0144908647302
    12 peak_absolute_error: 1.0
    12 peak_signal_to_noise_ratio: 18.389056976
    12 root_mean_squared_error: 0.120378007668
    12 normalized_cross_correlation_error: 0.554534400101
    12 fuzz_error: 0.120378007668
    13 undefined: 0.339269332472
    13 absolute_error: 50135.0
    13 mean_absolute_error: 0.0566569341585
    13 mean_error_per_pixel: 559692030.0
    13 mean_squared_error: 0.0128473981062
    13 peak_absolute_error: 0.996078431373
    13 peak_signal_to_noise_ratio: 18.9118481806
    13 root_mean_squared_error: 0.113346363445
    13 normalized_cross_correlation_error: 0.339269332472
    13 fuzz_error: 0.113346363445
    14 undefined: 0.268324440992
    14 absolute_error: 49984.0
    14 mean_absolute_error: 0.0560254788272
    14 mean_error_per_pixel: 553454126.0
    14 mean_squared_error: 0.0128667907885
    14 peak_absolute_error: 1.0
    14 peak_signal_to_noise_ratio: 18.9052976053
    14 root_mean_squared_error: 0.113431877303
    14 normalized_cross_correlation_error: 0.268324440992
    14 fuzz_error: 0.113431877303
    15 undefined: 0.342554151543
    15 absolute_error: 49839.0
    15 mean_absolute_error: 0.0530138645966
    15 mean_error_per_pixel: 523703549.0
    15 mean_squared_error: 0.00989738009179
    15 peak_absolute_error: 1.0
    15 peak_signal_to_noise_ratio: 20.0447975109
    15 root_mean_squared_error: 0.0994855773054
    15 normalized_cross_correlation_error: 0.342554151543
    15 fuzz_error: 0.0994855773054
    16 undefined: 0.360328919872
    16 absolute_error: 50246.0
    16 mean_absolute_error: 0.128736732921
    16 mean_error_per_pixel: 1271740599.0
    16 mean_squared_error: 0.0298622445899
    16 peak_absolute_error: 0.996078431373
    16 peak_signal_to_noise_ratio: 15.2487755172
    16 root_mean_squared_error: 0.172806957585
    16 normalized_cross_correlation_error: 0.360328919872
    16 fuzz_error: 0.172806957585
    17 undefined: 0.632283384321
    17 absolute_error: 50245.0
    17 mean_absolute_error: 0.0988579066808
    17 mean_error_per_pixel: 976579183.0
    17 mean_squared_error: 0.0190837184602
    17 peak_absolute_error: 0.996078431373
    17 peak_signal_to_noise_ratio: 17.1933699916
    17 root_mean_squared_error: 0.138143832509
    17 normalized_cross_correlation_error: 0.632283384321
    17 fuzz_error: 0.138143832509
    18 undefined: 0.111640501009
    18 absolute_error: 50246.0
    18 mean_absolute_error: 0.113250701971
    18 mean_error_per_pixel: 1118760064.0
    18 mean_squared_error: 0.0304730255274
    18 peak_absolute_error: 0.996078431373
    18 peak_signal_to_noise_ratio: 15.1608442452
    18 root_mean_squared_error: 0.174565247193
    18 normalized_cross_correlation_error: 0.111640501009
    18 fuzz_error: 0.174565247193
    19 undefined: 0.160883239071
    19 absolute_error: 50246.0
    19 mean_absolute_error: 0.0905529890976
    19 mean_error_per_pixel: 894538101.0
    19 mean_squared_error: 0.0189788856282
    19 peak_absolute_error: 0.992156862745
    19 peak_signal_to_noise_ratio: 17.2172929137
    19 root_mean_squared_error: 0.137763876354
    19 normalized_cross_correlation_error: 0.160883239071
    19 fuzz_error: 0.137763876354
    20 undefined: 0.115260004735
    20 absolute_error: 50215.0
    20 mean_absolute_error: 0.0982209620172
    20 mean_error_per_pixel: 970287052.0
    20 mean_squared_error: 0.0253242845916
    20 peak_absolute_error: 0.988235294118
    20 peak_signal_to_noise_ratio: 15.9646281457
    20 root_mean_squared_error: 0.159136056856
    20 normalized_cross_correlation_error: 0.115260004735
    20 fuzz_error: 0.159136056856
    21 undefined: 0.508098114583
    21 absolute_error: 50140.0
    21 mean_absolute_error: 0.0579010614183
    21 mean_error_per_pixel: 571982284.0
    21 mean_squared_error: 0.0123612392453
    21 peak_absolute_error: 0.992156862745
    21 peak_signal_to_noise_ratio: 19.0793798795
    21 root_mean_squared_error: 0.11118111011
    21 normalized_cross_correlation_error: 0.508098114583
    21 fuzz_error: 0.11118111011
    22 undefined: 0.412411160502
    22 absolute_error: 50132.0
    22 mean_absolute_error: 0.0687808921284
    22 mean_error_per_pixel: 679459941.0
    22 mean_squared_error: 0.0157369621508
    22 peak_absolute_error: 1.0
    22 peak_signal_to_noise_ratio: 18.0307909971
    22 root_mean_squared_error: 0.125447049191
    22 normalized_cross_correlation_error: 0.412411160502
    22 fuzz_error: 0.125447049191
    23 undefined: 0.148620049492
    23 absolute_error: 50194.0
    23 mean_absolute_error: 0.0974919474616
    23 mean_error_per_pixel: 963085398.0
    23 mean_squared_error: 0.0252079154387
    23 peak_absolute_error: 0.988235294118
    23 peak_signal_to_noise_ratio: 15.984630667
    23 root_mean_squared_error: 0.158770007995
    23 normalized_cross_correlation_error: 0.148620049492
    23 fuzz_error: 0.158770007995
    24 undefined: 0.336892065447
    24 absolute_error: 50230.0
    24 mean_absolute_error: 0.0820035490745
    24 mean_error_per_pixel: 810081476.0
    24 mean_squared_error: 0.0186291224696
    24 peak_absolute_error: 1.0
    24 peak_signal_to_noise_ratio: 17.2980760219
    24 root_mean_squared_error: 0.136488543364
    24 normalized_cross_correlation_error: 0.336892065447
    24 fuzz_error: 0.136488543364
    25 undefined: 0.173034529269
    25 absolute_error: 50198.0
    25 mean_absolute_error: 0.0994330378199
    25 mean_error_per_pixel: 982260682.0
    25 mean_squared_error: 0.0227561413863
    25 peak_absolute_error: 1.0
    25 peak_signal_to_noise_ratio: 16.4290137658
    25 root_mean_squared_error: 0.150851388414
    25 normalized_cross_correlation_error: 0.173034529269
    25 fuzz_error: 0.150851388414
    26 undefined: 0.116920743287
    26 absolute_error: 50217.0
    26 mean_absolute_error: 0.119995400408
    26 mean_error_per_pixel: 1185388342.0
    26 mean_squared_error: 0.0286707246305
    26 peak_absolute_error: 1.0
    26 peak_signal_to_noise_ratio: 15.4256133046
    26 root_mean_squared_error: 0.169324317895
    26 normalized_cross_correlation_error: 0.116920743287
    26 fuzz_error: 0.169324317895
    27 undefined: 0.299173388059
    27 absolute_error: 50236.0
    27 mean_absolute_error: 0.109340216072
    27 mean_error_per_pixel: 1080129880.0
    27 mean_squared_error: 0.0198934930772
    27 peak_absolute_error: 0.921568627451
    27 peak_signal_to_noise_ratio: 17.0128895287
    27 root_mean_squared_error: 0.141044294735
    27 normalized_cross_correlation_error: 0.299173388059
    27 fuzz_error: 0.141044294735
    28 undefined: 0.252318154072
    28 absolute_error: 50236.0
    28 mean_absolute_error: 0.117073878869
    28 mean_error_per_pixel: 1156527756.0
    28 mean_squared_error: 0.0244511645789
    28 peak_absolute_error: 0.972549019608
    28 peak_signal_to_noise_ratio: 16.1170045114
    28 root_mean_squared_error: 0.156368681579
    28 normalized_cross_correlation_error: 0.252318154072
    28 fuzz_error: 0.156368681579
    29 undefined: 0.356506869986
    29 absolute_error: 50246.0
    29 mean_absolute_error: 0.286599004792
    29 mean_error_per_pixel: 2831201179.0
    29 mean_squared_error: 0.103719343072
    29 peak_absolute_error: 0.741176470588
    29 peak_signal_to_noise_ratio: 9.84140242587
    29 root_mean_squared_error: 0.322054875871
    29 normalized_cross_correlation_error: 0.356506869986
    29 fuzz_error: 0.322054875871
    30 undefined: 0.349287065666
    30 absolute_error: 50246.0
    30 mean_absolute_error: 0.1647397289
    30 mean_error_per_pixel: 1627400329.0
    30 mean_squared_error: 0.0425094737148
    30 peak_absolute_error: 0.576470588235
    30 peak_signal_to_noise_ratio: 13.7151427175
    30 root_mean_squared_error: 0.206178257134
    30 normalized_cross_correlation_error: 0.349287065666
    30 fuzz_error: 0.206178257134
    31 undefined: 0.79038190447
    31 absolute_error: 50235.0
    31 mean_absolute_error: 0.0769156664245
    31 mean_error_per_pixel: 759820243.0
    31 mean_squared_error: 0.0130043342464
    31 peak_absolute_error: 0.509803921569
    31 peak_signal_to_noise_ratio: 18.8591187649
    31 root_mean_squared_error: 0.114036547854
    31 normalized_cross_correlation_error: 0.79038190447
    31 fuzz_error: 0.114036547854
    32 undefined: 0.299516726946
    32 absolute_error: 50246.0
    32 mean_absolute_error: 0.194900644385
    32 mean_error_per_pixel: 1925348396.0
    32 mean_squared_error: 0.0543778247827
    32 peak_absolute_error: 0.639215686275
    32 peak_signal_to_noise_ratio: 12.6457816901
    32 root_mean_squared_error: 0.233190533218
    32 normalized_cross_correlation_error: 0.299516726946
    32 fuzz_error: 0.233190533218
    33 undefined: 0.308129410467
    33 absolute_error: 50246.0
    33 mean_absolute_error: 0.160407891214
    33 mean_error_per_pixel: 1584607773.0
    33 mean_squared_error: 0.0427577664042
    33 peak_absolute_error: 0.686274509804
    33 peak_signal_to_noise_ratio: 13.689849897
    33 root_mean_squared_error: 0.206779511568
    33 normalized_cross_correlation_error: 0.308129410467
    33 fuzz_error: 0.206779511568
    34 undefined: 0.196142594718
    34 absolute_error: 50244.0
    34 mean_absolute_error: 0.223029622363
    34 mean_error_per_pixel: 2203223735.0
    34 mean_squared_error: 0.0739595295975
    34 peak_absolute_error: 0.858823529412
    34 peak_signal_to_noise_ratio: 11.3100585973
    34 root_mean_squared_error: 0.271955013922
    34 normalized_cross_correlation_error: 0.196142594718
    34 fuzz_error: 0.271955013922
    35 undefined: 0.433944899633
    35 absolute_error: 50242.0
    35 mean_absolute_error: 0.161492203457
    35 mean_error_per_pixel: 1595319276.0
    35 mean_squared_error: 0.0452070577337
    35 peak_absolute_error: 0.658823529412
    35 peak_signal_to_noise_ratio: 13.4479375777
    35 root_mean_squared_error: 0.212619514
    35 normalized_cross_correlation_error: 0.433944899633
    35 fuzz_error: 0.212619514

Visualization:

    $ python analyze.py 
    undefined
    ▂▄▆▃▅▂▂▂▄▄▅▆▅▃▂▃▃▆▁▁▁▅▄▁▃▁▁▂▂▃▃█▂▃▁▄
    absolute_error
    ▆▁▂▁▇▇▄▃▁▂▇▇▇▇▇▇█▇██▇▇▇▇▇▇▇▇▇██▇██▇▇
    mean_absolute_error
    ▂▁▁▁▁▁▁▁▁▁▂▁▂▁▁▁▃▂▃▂▂▁▂▂▂▂▃▃▃█▄▂▅▄▆▄
    mean_error_per_pixel
    ▃▂▁▁▂▂▁▁▁▁▂▂▂▂▂▂▄▃▃▃▃▂▂▃▂▃▃▃▃█▅▂▅▄▆▄
    mean_squared_error
    ▂▁▁▁▁▁▁▁▁▁▁▁▁▁▁▁▂▂▂▁▂▁▁▂▁▂▂▂▂█▃▁▄▃▅▃
    peak_absolute_error
    █▇▇▇██████▇▇█▇██▇▇▇▇▇▇█▇███▆▇▄▁▁▂▃▅▃
    peak_signal_to_noise_ratio
    ▄▇▇▆▇▇█▇▇▇▆▆▅▅▅▆▃▄▃▄▄▅▅▄▄▄▃▄▄▁▃▅▂▃▁▂
    root_mean_squared_error
    ▃▁▁▁▁▁▁▁▁▁▁▁▂▂▂▁▃▂▃▂▃▂▂▃▂▃▃▃▃█▄▂▅▄▆▄
    normalized_cross_correlation_error
    ▂▄▆▃▅▂▂▂▄▄▅▆▅▃▂▃▃▆▁▁▁▅▄▁▃▁▁▂▂▃▃█▂▃▁▄
    fuzz_error
    ▃▁▁▁▁▁▁▁▁▁▁▁▂▂▂▁▃▂▃▂▃▂▂▃▂▃▃▃▃█▄▂▅▄▆▄
