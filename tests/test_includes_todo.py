from lib.includes_todo import includes_todo

def test_string_does_not_include_todo():
    result = includes_todo("drink tea")
    assert result == False 

def test_string_includes_todo():
    result = includes_todo("#TODO buy milk")
    assert result == True 

def test_string_is_not_case_sensitive():
    result = includes_todo("#Todo buy milk")
    assert result == True 

def test_string_is_empty():
    result = includes_todo("")
    assert result == False 

def test_string_contains_space():
    result = includes_todo(" ")
    assert result == False 