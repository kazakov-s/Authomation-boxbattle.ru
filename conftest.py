import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from pathlib import Path


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    now = datetime.now()
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            report_dir = Path('Reports', now.strftime("%S%H%d%m%Y"))
            file_name = report.nodeid.replace("::", "_") + ".png"
            # file_name = "screenshot" + now.strftime("%S%H%d%m%Y") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="../Reports/Screenshots/%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    now = datetime.now()
    report_dir = Path('Reports')
    report_dir.mkdir(parents=True, exist_ok=True)
    pytest_html = report_dir / f"report_{now.strftime('%d%m%Y') + '_' + now.strftime('%H%M%S')}.html"
    config.option.htmlpath = pytest_html
    config.option.self_contained_html = True


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    global driver
    driver = webdriver.Chrome()
    yield driver
    print("\nquit browser..")
    driver.quit()

def _capture_screenshot(name):
    screenshot_dir = Path('Reports/Screenshots')
    screenshot_dir.mkdir(parents=True, exist_ok=True)
    driver.get_screenshot_as_file(str(screenshot_dir) + '/' + str(name))


def pytest_html_report_title(report):
    report.title = "Автоматизация тестов формы авторизации сайта boxbattle.ru. Выполнил Казаков С.А."
