from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field


# 定义输出数据模型
class TestCase(BaseModel):
    id: str = Field(..., description="Serial number for the test case")
    test_description: str = Field(..., description="Description of the test case")
    test_name: str = Field(..., description="Name of the test case")
    reason: str = Field(..., description="Reason to add this test case")
    importance: str = Field(..., description="Importance level of the test case, e.g., critical")


class TestCaseList(BaseModel):
    test_cases: list[TestCase] = Field(..., description="List of test cases")


def _get_test_cases_parser():
    return JsonOutputParser(pydantic_object=TestCaseList)

