from abbrev_name import abbrev_name

def test_name_to_initials():
    assert abbrev_name("Sam Harris") == "S.H"

    assert abbrev_name("patrick feeney") == "P.F"

    assert abbrev_name("   John   Doe   ") == "J.D"


