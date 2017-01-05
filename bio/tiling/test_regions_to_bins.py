

import pytest

from io import StringIO

import pandas as pd

from regions_to_bins import regions_to_bins

@pytest.fixture
def bed_df():

    contents = """chrA	14169	14919
chrA	31420	32170"""

    return pd.read_table(StringIO(contents), sep="\t", header=None)


@pytest.fixture
def expected_result():

    contents = """Chromosome Start End
chrA	14000	14199
chrA	14200	14399
chrA	14400	14599
chrA	14600	14799
chrA	14800	14999
chrA	31400	31599
chrA	31600	31799
chrA	31800	31999
chrA	32000	32199"""

    return pd.read_table(StringIO(contents), sep="\s+", header=0, index_col=None)


def test_regions_to_bins(bed_df, expected_result):

    result = regions_to_bins(bed_df)

    print("Actual", result)
    print("Expected", expected_result)

    print("Actual", result.columns)
    print("Expected", expected_result.columns)

    print("Actual", result.dtypes)
    print("Expected", expected_result.dtypes)

    assert expected_result.equals(result)
