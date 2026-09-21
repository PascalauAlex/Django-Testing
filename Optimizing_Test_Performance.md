# Optimizing Test Performance 


Tests with mock from **_unittest.mock_**

**_setUpTestData_ -** The class-level atomic block described above 
allows the creation of initial data at the class level, once for the whole TestCase.

**TransactionTestCase** only for database interactions. Use SimpleTestCase for simple tests.

**Running tests in parallel** _--paralel_

**Password hashing** - use a faster hashing algorithm for test users 

Preserver test_database - --keepdb

--durations N for identify the slower tests

Use tags for grouping tests and run only the tests that are needed for a particular functionality
