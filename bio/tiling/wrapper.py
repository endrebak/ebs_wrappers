__author__ = "Endre Bakken Stovner"
__email__ = "endrebak85@gmail.com"
__license__ = "MIT"

import pandas as pd

from regions_to_bins import regions_to_bins

df = pd.read_table(snakemake.input[0])
df = regions_to_bins(df)
df.to_csv(snakemake.output[0], index=False)
