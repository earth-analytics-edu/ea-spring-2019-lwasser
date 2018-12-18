
test = {
  'name': 'test_valid',
  'points': 1,
  'suites': [
    {
      'cases': [{'code': r"""
      >>> >>>  # Tests for plot 3  - does each test need to import the proper packages or how does this work??
      >>> >>>  # Begin tests
      >>> >>> from autograde.timeseries import TimeSeriesTester
      >>> # Get the ax_object & run a set of basic tests
      >>> >>> p1_time2 = TimeSeriesTester(ax2)
      >>> # Test that plot is of the right type and contains date ticks
      >>> # POINTS 5
      >>> >>> #p1_time2.assert_plot_type("line") # this test isn't currently working properly. 
      >>> # POINTS 5
      >>> >>> p1_time2.assert_title_contains("stream discharge")
      >>> # POINTS 5
      >>> >>> p1_time2.assert_xticks_locs()
      >>> # POINTS 5
      >>> >>> p1_time2.assert_xticks_reformatted(tick_size="large", loc_exp='year',
      >>> >>> m="x ticks should be of date format. Each tick should represent a year.")
      >>> # POINTS 5
      >>> >>> p1_time2.assert_axis_label_contains("x", lst="date")
      """},
      ]
    }
  ]
}
