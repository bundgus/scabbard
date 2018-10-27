import pytest
import os
import datetime
import schedule
import time


def run_tests():
    today = datetime.datetime.now()
    results_file_parameter = '--junitxml=test_results/' + today.strftime("%Y-%m-%dT%H:%M:%S") + '_junitxml.xml'

    testpath = os.path.join('tests', 'rest')

    pytest.main(['-q', results_file_parameter, '-p', 'no:warnings', testpath])


run_tests()
schedule.every(60).minutes.do(run_tests)
# schedule.every().hour.do(run_tests)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(10)
