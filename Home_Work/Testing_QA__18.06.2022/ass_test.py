import Converter_temp as ct


def testconverter():
    assert ct.converter('37C') == (99, 'F', '99F')
    assert ct.converter('21C') == (70, 'F', '70F')
    assert ct.converter('50C') == (122, 'F', '122F')
    assert ct.converter('99F') == (37, 'C', '37C')
    assert ct.converter('70F') == (21, 'C', '21C')
    assert ct.converter('122F') == (50, 'C', '50C')


testconverter()
