from behave import *
#from pathlib import Path
#import pytest
import sort

#def pytest_configure():
#    gdata = []

#@scenario('first_1.feature','Sort Abs')
#def test_sort_abs1():
#    print('End of test sort_abs1')
#    pass

@given('the list is [3, -4, 5, 0, 1]')
def step_impl(context):
    context.gdata = [3, -4, 5, 0, 1]
    #return gdata
    #pass
#def begin_list():
#    gdata = [3, -4, 5, 0, 1]
#    return gdata

@when('the list is sorted')
def step_impl(context):
    context.gdata = sort.sort_1(context.gdata)
#def sorted_list(begin_list):
#    begin_list = sort.sort_1(begin_list)
    

@then('the new list is [5, -4, 3, 1, 0]')
def step_impl(context):
    assert context.gdata == [5, -4, 3, 1, 0]
#def final_list(begin_list):
#    assert begin_list == [5, -4, 3, 1, 0]


