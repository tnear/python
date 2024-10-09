# CProfile: C extension profiler
# https://docs.python.org/3/library/profile.html

# Basic usage:
'''
# Profile Num.py:
# -m = module (use the cProfile module)
# -s = sort by column (ex: ncalls, tottime, percall, cumtime, percall)
$ python -m cProfile -s tottime NumPy.py

        99726 function calls (97361 primitive calls) in 0.185 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      112    0.030    0.000    0.030    0.000 {built-in method io.open_code}
      556    0.025    0.000    0.025    0.000 {built-in method nt.stat}
       17    0.014    0.001    0.016    0.001 {built-in method _imp.create_dynamic}
      112    0.010    0.000    0.010    0.000 {built-in method marshal.loads}
     1254    0.007    0.000    0.011    0.000 <frozen importlib._bootstrap_external>:96(_path_join)
'''

# Profiling unit tests:
# https://stackoverflow.com/questions/11645285/why-cprofile-module-doesnt-work-with-unittest
'''
Replace:
unittest.main()

With:
unittest.main(module='myTest')  # if in 'myTest.py'

Then run the unit tests:
python -m cProfile -s tottime -m unittest discover
'''
