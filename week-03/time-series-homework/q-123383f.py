
test = {
  'name': 'test_valid',
  'points': 1,
  'suites': [
    {
      'cases': [{'code': r"""
      >>> # If these will end up in the little .py scripts that is probably ideal.
      >>> from autograde.timeseries import TimeSeriesTester
      >>> # Get the ax_object & run a set of basic tests
      >>> # The question here becomes
      >>> p1_time = TimeSeriesTester(ax1)
      >>> # Test that plot is of the right type and contains date ticks
      >>> p1_time.assert_plot_type("scatter")
      >>> p1_time.assert_title_contains("precipitation")
      >>> p1_time.assert_xticks_locs
      >>> p1_time.assert_xticks_reformatted(
      >>>         tick_size="large",
      >>>         loc_exp='year',
      >>>         m="x ticks should be of date format. Each tick shoud represent a year.")
      """},
      ]
    }
  ]
}
