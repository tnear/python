# statistics - Mathematical statistics functions
# Python 3.4+

import statistics

# quantiles is python 3.8+
def quantiles():
    # data does not need to be sorted for quantiles()
    data = [3.2, 1.1, 2.7, 1.9, 4.8]

    # n = number of quantiles. Choose 100 to compute percentile.
    # Use 'inclusive' if the data set already contains the highest
    # and lowest possible values.
    # Use 'exclusive' (default) if other data samples can have more
    # extreme values.
    quantiles = statistics.quantiles(data, n=100, method='exclusive')
    p50 = quantiles[49]
    assert p50 == 2.7

    # p90 and p99 are greater than the max value (4.8) because
    # interpolation is required when lists have 100 data points
    # for 'exclusive'
    p90 = quantiles[89]
    assert p90 == 5.44
    p99 = quantiles[98]
    assert p99 > 6.303 and p99 < 6.304

def main():
    quantiles()

if __name__ == '__main__':
    main()
    print(f'Tests passed for {__file__}!')
