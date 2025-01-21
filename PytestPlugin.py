import pytest
from typing import Any

class MetricsCollector:
    # store metrics for a single test run
    def __init__(self):
        self.metrics: dict[str, Any] = {}

    def add_metric(self, name: str, value: Any):
        self.metrics[name] = value

class MetricsPlugin:
    # plugin to collect metrics across all tests
    def __init__(self):
        self.test_metrics: dict[str, dict[str, Any]] = {}

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(self, item):
        outcome = yield
        report = outcome.get_result()

        # only collect after test finishes
        if report.when == 'call':
            # get metrics from test's collector
            if 'metrics' in item.funcargs:
                collector = item.funcargs['metrics']
                test_name = item.name
                self.test_metrics[test_name] = collector.metrics.copy()

    def get_all_metrics(self) -> dict[str, dict[str, Any]]:
        return self.test_metrics

@pytest.fixture
def metrics():
    # fixture to provide metrics collector to tests
    collector = MetricsCollector()
    yield collector

# Example usage in test file:
def test_with_metrics(metrics):
    # Perform some test operation
    result = 101
    timing = 0.123

    # Record metrics
    metrics.add_metric('result_value', result)
    metrics.add_metric('operation_time', timing)

    assert result == 101

def test_another_metric(metrics):
    # Another test with different metrics
    items_processed = 100
    error_rate = 0.05

    metrics.add_metric('items_processed', items_processed)
    metrics.add_metric('error_rate', error_rate)

    assert error_rate < 0.1

def run_tests_with_metrics():
    # create plugin instance
    metrics_plugin = MetricsPlugin()

    # run tests using pytest.main() and return collected metrics
    pytest.main([__file__], plugins=[metrics_plugin])
    return metrics_plugin.get_all_metrics()

def main():
    all_metrics = run_tests_with_metrics()

    # print collected metrics
    print('\nCollected test metrics:')
    for test_name2, metrics2 in all_metrics.items():
        print(f'\n{test_name2}:')
        for metric_name, value in metrics2.items():
            print(f'  {metric_name}: {value}')

if __name__ == '__main__':
    main()
    print(f'Tests passed for {__file__}!')
