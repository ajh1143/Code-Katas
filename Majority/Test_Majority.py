#TESTS


test.describe("Find the majority")
test.it("Base fixed tests")

test.assert_equals(majority(["A", "B", "A"]), "A")
test.assert_equals(majority(["A", "BB", "A"]), "A")
test.assert_equals(majority(["A", "B", "C"]), None)
test.assert_equals(majority(["A", "B", "B", "A"]), None)
test.assert_equals(majority(['A','A','A','A']), "A")
test.assert_equals(majority(['A',]), "A")
test.assert_equals(majority(['A','A','A','BBBBBBBB']), "A")
test.assert_equals(majority(["A", "B", "C", "C"]), "C")
test.assert_equals(majority([]), None)
