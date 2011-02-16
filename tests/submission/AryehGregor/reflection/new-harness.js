// We override only the things we need to -- the rest we'll just inherit from
// original-harness.js.  Polymorphism, kind of.
ReflectionHarness.catchUnexpectedExceptions = false;

ReflectionHarness.testWrapper = function(fn) {
	test(fn, this.getTypeDescription());
}

ReflectionHarness.test = function(expected, actual, description) {
	assert_equals(expected, actual, description);
	return true;
}

ReflectionHarness.testException = function(exceptionName, fn, description) {
	assert_throws(exceptionName, fn, description);
}
