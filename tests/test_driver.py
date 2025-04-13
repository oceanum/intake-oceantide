"""Test for intake plugins."""
import os
import pytest
import intake


HERE = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope="module")
def catalog():
    """Open intake catalog."""
    cat = intake.open_catalog(os.path.join(HERE, "catalog.yml"))
    return cat


def test_open_total_currents(catalog):
    dset = catalog.total_currents_testing.to_dask()
    assert all([v in dset.data_vars for v in ("etot", "utot", "vtot")])


def test_open_oceantide_accessor(catalog):
    dset = catalog.oceantide_accessor_testing.to_dask()
    assert hasattr(dset, "tide")
