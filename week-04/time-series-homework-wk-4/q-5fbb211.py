
test = {
  'name': 'test_valid',
  'points': 1,
  'suites': [
    {
      'cases': [{'code': r"""
      >>> >>> # Begin tests 
      >>> >>> from autograde.timeseries import TimeSeriesTester
      >>> # Get the ax_object & run a set of basic tests
      >>> >>> p1_time = TimeSeriesTester(ax1)
      >>> # Test that plot is of the right type and contains date ticks
      >>> # POINTS 5 
      >>> >>> p1_time.assert_plot_type("scatter")
      >>> # POINTS 5
      >>> >>> p1_time.assert_title_contains("precipitation")
      >>> # POINTS 5
      >>> >>> p1_time.assert_xticks_locs
      >>> # POINTS 5
      >>> >>> p1_time.assert_xticks_reformatted(tick_size="large", loc_exp='year', 
      >>> >>> m="x ticks should be of date format. Each tick shoud represent a year.")
      """},
      ]
    }
  ]
}
