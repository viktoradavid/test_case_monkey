from django.apps import AppConfig


class TestCaseManagementConfig(AppConfig):
    name = 'test_case_monkey.tcm'
    verbose_name = "Test Case Management"

    def ready(self):
        """Override this to put in:
            ...
        """
        pass
