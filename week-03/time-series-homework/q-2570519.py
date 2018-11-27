
test = {
  'name': 'test_valid',
  'points': 1,
  'suites': [
    {
      'cases': [{'code': r"""
      >>> from autograde.base import PlotTester
      >>> t=PlotTester(ax1)
      >>> # Run a set of basic tests
      >>> # The question here becomes
      >>> t.assert_plot_type("scatter")
      >>> t.assert_title_contains("x")
      """},
      ]
    }
  ]
}
