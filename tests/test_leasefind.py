#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `leasefind` package."""

import pytest

from click.testing import CliRunner

from leasefind import leasefind
from leasefind import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    import requests
    return requests.get(leasefind.LeaseBuster.URL)


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    assert 'LeaseBuster' in soup.select(".home-header > tr > td > div")[0].string


def test_AutoListing():
    with pytest.raises(TypeError, match=r".*Can't instantiate abstract class AutoListing with abstract methods get_listing.*"):
        leasefind.AutoListing()



def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'leasefind.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
