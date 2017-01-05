import pandas as pd

def regions_to_bins(bed_df, bin_size=200):

    """Tile genomic regions."""

    rowdicts = []
    for _, (chromosome, start, end) in bed_df.iterrows():
        start = start - (start % bin_size)
        end = end - (end % bin_size) + bin_size - 1

        for tile in range(start, end, bin_size):
            rowdicts.append({"Start": tile, "End": tile + bin_size - 1, "Chromosome": chromosome})

    df = pd.DataFrame.from_dict(rowdicts)

    return df[["Chromosome", "Start", "End"]]
