import password_analyzer

def test_entropy():
    assert password_analyzer.calculate_entropy("A1b2C3d4!") > 50

def test_common():
    assert password_analyzer.is_common("123456", ["123456", "password"])

def test_evaluation():
    assert password_analyzer.evaluate_password("Super$ecret123") == "Strong"
