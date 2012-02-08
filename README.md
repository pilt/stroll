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
