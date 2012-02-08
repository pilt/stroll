## OS X Setup

    $ brew install imagemagick
    $ pip install -r requirements.txt

## Input images

The images in `data/` were taken during an outside walk
of approximately 2 km. The last few images in the series
were taken indoors (the end of the walk, before I got home).

## Output images

See the `compared/` dir. Red areas are the difference between
two consecutive images. Also see 
[the ImageMagick tool compare](http://www.imagemagick.org/Usage/compare/).

## Performance

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

## Visualization

Each bar is the distortion metric between two images. The first
bar is the first image of the stroll compared with the second image,
the last bar the last two images.

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
