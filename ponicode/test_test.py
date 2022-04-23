import test
import pytest

class Test_Employee_Show_alry_detail:
    
    @pytest.fixture()
    def employee(self):
        return test.Employee()
    

    def test_show_alry_detail_1(self, employee):
        result = employee.show_alry_detail()

