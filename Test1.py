import re
ignore_case=re.I
#########################    Question # 01 ##############################
def check_alpha_numeric_value(text_data):
    pattern = r'[A-Za-z0-9]+'
    match_data = re.findall(pattern,text_data,ignore_case)
    return match_data
text_data = "To check alpha @ numeric values & # &&& 125_483"
match_data = check_alpha_numeric_value(text_data)
print("Only find alphanumeric values  :", match_data)

#########################    Question # 02 ##############################
def check_a_follwed_by_zero_or_more_b(text_data):
    pattern = r'ab*'
    match_data = re.findall(pattern,text_data,ignore_case)
    return match_data
text_data = "aaa abb ACC AB"
match_data = check_a_follwed_by_zero_or_more_b(text_data)
print("Check b/B followed by zero or more time  :", match_data)