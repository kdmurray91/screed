"""
Test the pygr API.
"""

from screed_pygr_api import ScreedSequenceDB, ScreedSequenceDB_ByIndex

import tests

def test_name_iterator_methods():
    db = ScreedSequenceDB(tests.testfa)

    # test the various iterator methods for equal results from db
    a = sorted([ (x, db[x]) for x in db ])
    b = sorted([ i for i in db.iteritems() ])
    c = sorted([ (v.name, v) for v in db.itervalues() ])

    assert a == b
    assert a == c

def test_index_iterator_methods():
    db = ScreedSequenceDB_ByIndex(tests.testfa)

    # test the various iterator methods for equal results from db
    m = sorted([ (x, db[x]) for x in db ])
    n = sorted([ i for i in db.iteritems() ])
    o = sorted([ (v.record.index, v) for v in db.itervalues() ])

    assert m == n
    assert m == o, (m, o)

def test_name_index_equality():
    db1 = ScreedSequenceDB(tests.testfa)
    db2 = ScreedSequenceDB_ByIndex(tests.testfa)

    # must use something other than the obj itself for comparison...
    v1 = sorted([ (v.name, v.seq) for v in db1.itervalues() ])
    v2 = sorted([ (v.name, v.seq) for v in db2.itervalues() ])
    assert v1 == v2, (v1, v2)

def test_seqinfodict_by_name():
    db1 = ScreedSequenceDB(tests.testfa)
    sd = db1.seqInfoDict

    m = sorted([ y.id for (x, y) in sd.iteritems() ])
    n = sorted([ x.id for x in sd.itervalues() ])

    assert m == n, (m, n)
    
def test_seqinfodict_by_index():
    db1 = ScreedSequenceDB_ByIndex(tests.testfa)
    sd = db1.seqInfoDict

    m = sorted([ x for (x, y) in sd.iteritems() ])
    n = sorted([ x for x in sd.iterkeys() ])

    assert m == n, (m, n)
    
