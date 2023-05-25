# Sample code for profiling :)
import cProfile
import pandas as pd

with cProfile.Profile() as pr:
    # run something
    x = list(i for i in range(1, 1000000))
df = pd.DataFrame(
    pr.getstats(),
    columns=['func', 'ncalls', 'ccalls', 'tottime', 'cumtime', 'callers']
)
print(df)