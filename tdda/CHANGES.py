# -*- coding: utf-8 -*-
"""2.0.01
Allow iterations=1 in wizard

2.0.0
Release gentest

1.0.02
Improved documentation to use shorter import forms.

Also bumped version number.

Also planning to tag this with a version to see whether that encourages
readthedocs to add the version properly.

29.05.2018 1.0.03
Add pushv (for maintainer use only) and this CHANGES.py file.

29.05.2018 1.0.04
Correctly cast strings to native strings in check_shell_output.

29.05.2018 1.0.05
Tests for feather are now ignored if pmmif/feather are not installed.

29.05.2018 1.0.06
Windows fixes.

31.05.2018 1.0.07
Fix for UTF-8 encoding in subprocesses on Windows.

Also added documentation on setting up fonts on Windows to display
ticks and crosses correctly.

6.06.2018 1.0.08
Improved metadata in TDDA files.

11.06.2018 1.0.09
Add support for postloadhook and postdicthook.

25.07.2018 1.0.10
Minor bug fixes.

 - Fuzzy verification of 'min' constraint was printing out the type of the col.
 - Typo in documentation of the properties available in a Verification result.
 - Verification of 'rex' constraint was not checking that the field exists.

26.07.2018 1.0.11
Fixed bug in pandas detect; it wasn't detecting min/max length constraints.

Also fixed issue with pandas CSV file reader; it has problems reading files
that have stuttered quotes and which also have escaped content. It now
notices if that has gone wrong, and has another try.

26.07.2018 1.0.12
minor refactoring and comments

1.08.2018 1.0.13
Now accepts 'false' as a valid specification value for no-duplicates.

Also improved the error message you get if you provide invalid specifications.
Also suppressed pandas warning about nanoseconds on conversion.

1.08.2018 1.0.14
Ignore epsilon for date min/max (rather than crashing).

This probably isn't ideal, but to make it better we'd need to decide
on what epsilon should mean for dates, which is not obvious.

13.08.2018 1.0.15
Change use of re.U (UNICODE) to re.UNICODE | re.DOTALL.

This means that dot actually matches any character.
The Python documentation claims that without this any character except
newline is matched, but it appears that some other characters are
also not matched without re.DOTALL, including a non-breaking space (0x80).

18.09.2018 1.0.16
referencetest class now exports TaggedTestLoader for convenience.

18.09.2018 1.0.17
TestLoader now takes an optional 'printer' parameter to control how -0 works.

18.09.2018 1.0.18
Renamed tdda.referencetest method assertFileCorrect -> assertTextFileCorrect.

The original name is still available for backwards compatibility, but
is deprecated.

19.09.2018 1.0.19
Added tdda.referencetest method assertBinaryFileCorrect.
Also fixed some issues with tdda.referencetest ignore_patterns method.

19.09.2018 1.0.20
Added test files so that all the new tests will pass.

28.02.2019 1.0.21
Changed 'test' command to from 'this' Python rather than a new Python.

Previously, the 'test' command (run with 'tdda test') ran in a subshell
using an os.system call. In order to do this, we used sys.executable()
to find (ostensibly) the path to the running version of Python.

It transpires, however, that sys.executable() does not always return
the path to the running Python...and indeed sometimes returns a path
that does not exist. We now, therefore, simply run the tests in the
current Python, by calling the (new) function 'testall', now used
by main() in tdda.testtdda.py.

13.03.2019 1.0.22
Fix for fuzzy min/max comparison on date columns, previously crashing.

Also fixed issue with problems, on some platforms, with the 'tdda examples'
command, for non-ascii example files. It had already had support for doing
this, but it wasn't always working. Now it's much more bullet-proof.

Also, it no longer generates warnings for unrecognised keys in the input
.tdda file (on verify and detect), for keys with names that begin with '#'.
This gives a mechanism for 'commented out' items in the file (which you
could always do, but you'd get annoying warnings, which now you no longer
get).

Also added some examples of 'detect' in the constraints examples and README.

Also added some examples for the 'accounts' banking datasets for constraints,
and included this new dataset as part of the standard examples you get if
you run 'tdda examples'.

Also fixed typo in link to 1-pager pdf in the documentation.

Added tests for accounts-based constraints examples.
Also, copying examples now unzips the file.

18.03.2019 1.0.23
Fixed tests to pass under Python 3.7.2.

The standard re.escape method changed after python version 3.7.1 so that it
only escapes characters that would otherwise be treated as having special
meaning within a regular expression. So the tests now need to allow BOTH
outputs to be considered correct. It's less easy than you'd imagine to work
out exactly what subversion the behaviour changed in.

Small fix to one test to ensure it still works in Pythons 2.7 & 3.6.

Fixed reftest example to use ignore_substrings rather than ignore_patterns
(as a result of the change to semantics of ignore_patterns in 1.0.19).

Added API examples for reference tests using accounts data.
>>>>>>> dev

------------------------- dev branch -------------------------
Refactored reporting of differences for files and strings, to take
better account of 'ignore' and 'remove' parameters. It now builds a 'diff'
that will only appear 'different' for lines that are REALLY different, after
any removals and ignores have been collapsed. That diff can also include an
embedded 'raw' diff, which will show ALL the differences, but the main focus
is on showing 'what is different that should not be'.

Also improved reporting of differences when there are different numbers
of lines. It now says what line at which the (effective) differences start
(taking into account removals and ignores).

Also improved reporting of differences when there is no 'actual' file to
compare (just a string in memory, with assertStringCorrect). It now produces
a temporary file containing the 'actual' contents, if there are errors to
report, so that a 'diff' command can be generated in the same way as it does
when there is a file already available.

The ignore_patterns parameter is now treated slightly more strictly than
before, and has had its documentation improved. If you provide an unanchored
regular expression pattern, it now requires that both sides match that
pattern, but it ALSO now requires that the remaining parts, to the left and
right of where the pattern matched, be 'equivalent' if the line is to be
ignored. The two 'left parts' must be equivalent, and the two 'right parts'
must also be equivalent. This 'equivalence' is checked by (recursively)
applying the same logic to these sub-parts.

The ignore_substrings parameter is now treated slightly more strictly than
before. Previously, a line was ignored if it contained any of the ignorable
substrings, in either the actual or the expected. That meant that lines in
the actual data might be being unexpectedly ignored if they start to include
such strings, which probably was not the intent of the test at all. Now,
ignorable substrings only refer to the *expected* data (which is fixed for
the test, and you know exactly what is in it and what is not).

Add comment=None to all constraint constructors.

This allows comments to be added to individual constraints by using
a dictionary for constraint values with keys "value" (for the constraint
value) and "comment" as an ignored string.

Added better support for unittest single-letter command-line option flags,
allowing things like -W, -1 and -0 to be grouped (with themselves, and with
standard unittest options). This means that passing grouped flags such as -1v
or -1W now works as expected with referencetest tests under unittest.

Relaxed limitation that ignore_patterns regex expressions in referencetest tests
couldn't include grouped expressions. Now they can (which is very useful for when
you want to use alternations in expressions, like (a|b)).

Better reporting of exclusions when checkfiles reports test failures.

Updated reference test tests.

Reporting differences when there are different numbers of lines now improved.

Fixed problem with set_defaults, where print_fn setting wasn't working.

Add -q/--quote flag to rexpy CLI to quote output strings.

Fixed problems with exceptions being raised for constraints that couldn't
apply because of type mis-match. (e.g. if a field is supposed to be a string,
and has min/max length constraints, or a rex constraint, then these should
fail when verified in an environment when it turns out not to be a string
any more; but it was raising an exception instead). Similar for things like
sign constraints, where it's expecting a numeric field, but it should cope
(and fail the constraint rather than blowing up) if the field is not numeric.

Added some 'convenience' imports at the root of the tdda module. So now
you can just import 'tdda', and then refer to things within tdda.constraints
or tdda.referencetest or tdda.rexpy. Previously you had to individually
import each submodule.

Updated MongoDB constraint support, which had rusted.

Updated constraint support for Pandas dataframes to include datetime.date
columns. Previously it only supported datetime.datetime (and raised an
exception if given a date-only).

Extended Pandas verify_df and detect_df so that they can accept an in-memory
dictionary to represent the constraints to verify/detect, as well as accepting
a path for a .tdda file. This means that, when using the tdda.constraints API,
you can now use the library to verify/detect against constraints that are
stored in other places, not just in the filesystem. (E.g. S3, version control,
etc).

------------------------- end of dev branch -------------------------

2.04.2019 1.0.24
Merged dev branch into master.

All changes listed above are now included in master.

10.04.2019 1.0.25
Fix in rexpy code for computing incremental coverage, to deal with some
edge cases that were hanging. It wasn't taking account of the possibility
that a *subset* of the expressions found could give 100% coverage, and
therefore some of the other expressions aren't contributing anything.

Fix for output regeneration in referencetests having rusted.
It was missing the new method _normalize_whitespace.

Merged dev branch into master again.

Fixed various documentation and release notes issues, including expanding
and updating the list of drivers supported and required for various
databases and other data sources.

Minor changes to tests to make them report more accurately and completely
what's going on when there are skipped tests.

Added boilerplate tests for MongoDB, but these are currently disabled
since they cannot yet work entirely correctly.

30.05.2019 1.0.26
Better JSON generation and protect against unfathomable user.

Tweaked the JSON produced for TDDA files:
  1. ensure no trailing whitespace, even in Python2
  2. don't force ASCII, so that accented characters, greek characters etc.,
     come out in UTF-8, rather than as character codes.

Also protect the lookup of the current user in a try ... except
and set to the empty string if it fails. This addresses issue #18,
whereby (poorly configured?) Docker containers with no non-root users
can cause getpass.getuser() to fail with an error. Whether or not
the software should need to deal with this, there seems little harm
in setting an empty user when the alternative is crashing, so that's
what now happens.

3.06.2019 1.0.27
Less excessive escaping (Python3-like even in Python2)

4.06.2019 1.0.28
Fixed (nasty) bug in escaping (above). Updated/improved tests.

Now that we do regular expression escapinge in (almost) the same way in
Python2 and Python3, we can remove a lot of nasty tests that have
two versions of the results.

5.06.2019 1.0.29
Updated bracket generatation ("character classes: [...]").

We now use almost no escaping for characters in character classes,
instead using special rules to force
  - close square bracket ("]") to the start
  - dash (hyphen "-") to the end
  - carat ("^") away from the start
Only backslash is now normally escaped in character classes.

There is also embryonic provision for new dialects "javascript" and "ruby"
to force escaping of "]" in character classes, since they don't appear to
obey the normal rules, but the embryonic provision isn't really used by
anything (or available outside the API) at this point.

Many tests have been updated as a result. Many tests also now check,
to a greater extent than was previously the case, that the regular expressions
generated actually actually match the strings used to generate them and
(equally relevantly) don't match certain strings you might worry they would
match if you weren't fully "au fait" with the details of regex rules!

13.06.2019 1.0.30
Fixed problem with the 'tdda test' command. It was failing with:
    AttributeError: module 'tdda.testtdda' has no attribute 'test'

Also simplified the list of characters to NOT be specially escaped for rexpy,
so it's now just the same across all python versions.

25.10.2019 1.0.31
Constraint verify/detect of regular expressions now handles '.' better.

It wasn't set to allow newlines to match '.', meaning that regular expressions
matching text with newlines in it wasn't always matching as you might expect.

Reftest Exercises added.

20.05.2020 1.0.32
Replaced deprecated uses of pandas.np (pd.np) with np.

19.10.2021 1.0.33
Updates for recent numpy and pandas deprecations and warnings.

Removed used of np.int (now int), np.float (now float) and np.bool (now bool).

Removed used of RangeIndex._start (now RangeIndex.start).

Added regex=False to Series.str.replace, which will be the new default
and which the code (implicitly) assumed was the default previously.

19.10.2021 1.0.34
Bump requirements on numpy/pandas; pandas update.

Pandas update now (starts to) add recognition of Integer Series type.

-------------------------- rexless branch ---------------------------
Use sampling and fewer regexes to speed up rexpy.

Also support specification of a seed (temporarily reseeds PRNG).

Also now use the max_patterns and min_strings_per_pattern parameters,
as well as the use_sampling parameter.

Two discover tests changed to use fixed seeds in light of above.

Fixed two new tests to work properly both Python2 and Python3.

Also now ensure that 'i' of appropriate type is used as type
specifier for an array in Python2. On Python 2.7.5 on Linux,
it complains if this is unicode rather thans ("bytes") str,
whereas on MacOS under Python 2.7.16 it doesn't, so it's not
entirely clear whether this is a feature of old Python 2.7
versions or Python 2.7 on Linux, but either way, forcing the
'i' to be of (bytes) str type under Python2 appears to be safe.

Also changed the default for add_dot_star to False, since adding
it is profoundly unhelpful when discovering constraints.

Slightly modified verbose printing in rexpy.

Fixed problem with sampling in rexpy.
----------------------- end of rexless branch -----------------------

---------------------------- dev branch -----------------------------
Add dialect support for rexpy: Can now generate output in any of

    - perl (the old default, using, e.g. \d)
    - portable (the new default, using, e.g. [0-9], aka grep)
    - java (using, e.g. \p{Digit})
    - posix (using, e.g. [[:digit:]])

Test results have been updated to reflect this new behaviour.

Also, reinstated relib to determine whether to use re or regex.
regex is preferred, where available.
Two variables are set by relib: relib is either 're' or 'regex',
and reIsRegex is set to True if the regex library is being used.

Referencetest no longer strips whitespace when its regenerating outputs,
which it was incorrectly doing due to a recent misplaced 'fix'.

Simplified the list of characters to NOT be specially escaped, so it's
now just the same across all python versions.

Added re.UNICODE and re.DOTALL to flags used for regular expresions.

Discover of regular expressions in database now sorts the values
before running rexpy on them. The order they come in makes a difference.

Updated the rexpy coverage code to handle the possibility that
not enough regular expressions have been generated to cover all
strings. (Probably fixed some edge-case bugs in the coverage code
at the same time.)
------------------------- end of dev branch -------------------------

--------------------------- branch gentest -------------------------------
Add initial code for automatically generating reference tests.

Change location of reference files from $(pwd)/ref to $(pwd)/ref/NAME
where NAME is the base name of the test script (without 'test_' and '.py').
This is to allow multiple tests to co-exist in the same directory
without conflict, and also means that the reference files can be
named STDOUT and STDERR rather than more convoluted names.

Also changed the command-line syntax to use STDOUT and STDERR (in any case)
for those streams, and to default not to use them. This means that any
behaviour specifiable from the wizard can now also be specified on the
command line, and reduces the complexity of the logic.

Check exit status, and require to be zero by default.

Allow NONZEROEXIT to specify that a non-zero exit status is OK on command line,
and add question to wizard for this.

Warn if any of the files specified are not available for copying, but
still generated the test script.

Remove existing reference files and script before generating, if they exist.

Handle multiple reference files with the same name.

Disambiguate reference files that differ only in case so that things
are more likely to work on case-insensitive filesystems.

Clearer reporting after generating test script.

Also test script now includes (equivalent) command used to generate it.

Added shell script that generates the first test for gentest.
(The shell script uses tdda gentest to generate itself.)

Add default values to gentest wizard.

Allow directories as files to check and default to checking new files
created under $(pwd).

Allow glob patterns in reference file specifications.

Add timing information to output from gentest.

Add some tests generated by gentest! Quite circular.
(Will only work for njr at the moment, because of paths in the test
output, but we should be able to fix this soon.)

Add flag handling and use new -r option in tests.

This means tests should work for other people.

Get rid of TDDA_CWD and use os.dirname(__file__).

Added support for multiple runs (default 2). This will be used to look
for variation in output between runs, to generate exclusions etc.

Started to generate exclusions automatically based on the difference
between two runs. Removed some of the boilerplate as a result and instead
use a function to generate all the variable tests.

Started adding code for over-specific lines (paths, timestamps etc.)

The two hand-generated specific gentest tests are now producing
what seem to be the correct results, starting to give some confidence
that we're generating the intended exclusion patterns.

More fixes for exclusion generation.

Fix various issues with gentest.

It now does uses substrings and patterns for exclusion patterns,
as appropriate, and (at least more often) gets the paths and
exclusions right for files with the same name.

It also now generates exclusion patterns for files, as well as for
STDOUT and STDERR. (It was generating them before, but failing to write
them out because of a failed lookup.)

There is also now support for a number of iterations to be passed in
and the wizard also offers this.

More kinds of dates are now recognized.

Now sets TMPDIR and checks that as output place, by default.

Further improvements to utility and handling of TMPDIR.

setUpClass now removes and files expected to be generated before running,
if they are already there.

When multiple runs are used, we now remove outputs from later runs
(which are no longer needed) once the tests have been written.

Fixed TMPDIR handling so it works if you generate multiple test files
and run them together using either pytest or testall.py.

Added test_discover25k.py.

Fixed problem with self.cwd being generated in test file where it should
not have been (should have been cwd).

Fixed problem with empty (None) name being joined onto path wrongly.

----------------------- end of branch gentest ---------------------------

10.02.2023 2.0.03
Add missing gentest examples in setup.py

10.02.2023 2.0.04
Add pyproject.toml

10.02.2023 2.0.05
Add __init__.py to gentest

10.02.2023 2.0.06
Add .readthedocs.yaml

10.02.2023 2.0.07
Fixes to .readthedocs.yaml

10.02.2023 2.0.08
Fix doc/source/conf.py; gentest on IPv6

On some systems (including, probably, ones using IPv6),
the IP address lookup in gentest was failing.
Now catch this and just don't check IP address.

conf.py had a bad path manipulation to get the version;
should be fixed now.

10.02.2023 2.0.09
*Actually* fix the IPv6 etc. issue

26.01.2024 2.0.10
Remove leading zeros in gentest test
"""
