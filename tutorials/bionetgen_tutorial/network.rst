Generating Network
=====================================================================================================

The ``generate_network`` command generates a complete or partial network of
species, reactions, and observables thorugh iterative application of the rules
to the initially defined species.  For each iteration, the entire set of rules
is applied to all of the current species, potentially generating new reactions
and species.  New species generated at the current iteration are not added to
the species list until all of the rules have been applied.  The order in which
the rules are specified in the input file therefore does not affect the
species and reactions generated at each iteration, although it will affect the
order in which they appear in the species and reaction lists.  The parameters
that affect the behavior of the generate_network command are given in the
Table below.


+--------------------+---------------------------------------------------------+---------------+
| Name               | Function                                                | Default Value |
+====================+=========================================================+===============+
| check_iso          | Perform isomorphism check for species that generate     |               | 
|                    | identical strings (keep this on unless you know         | 1(On)         |
|                    | what you're doing!)                                     |               |
+--------------------+---------------------------------------------------------+---------------+
| max_agg            | Max. number of molecules in one species                 | 1e99          |
+--------------------+---------------------------------------------------------+---------------+
| max_iter           | Max. number of rule applications                        | 100           |
+--------------------+---------------------------------------------------------+---------------+
| max_stoich         | Sets limit for number of molecules of each              | unset         |
|                    | specified type in one species (hash- see syntax above)  |               |
+--------------------+---------------------------------------------------------+---------------+
| print_iter         | Print NET file after each iteration                     | 0 (Off)       |
+--------------------+---------------------------------------------------------+---------------+
| prefix             | Base name of NET file                                   | Base name of  |
|                    |                                                         | BNGL file     |
+--------------------+---------------------------------------------------------+---------------+
| overwrite          | Overwrite existing NET file                             | 0 (Off)       |
+--------------------+---------------------------------------------------------+---------------+
| verbose            | Additional output for debugging                         | 0 (Off)       |
+--------------------+---------------------------------------------------------+---------------+

Calling ``generate_network`` with the default parameters (no parameters specified)
will cause network generation to proceed until the set of species and
reactions no longer increases with further application of the rules.  Some
rules sets generate an infinite number of species and reactions, so in
practice the maximum number of iterations is set to a finite value.

The file example1.bngl, provided in the Tutorial directory of the BNG2
distribution, contains a simple model based on the discussion above and
illustrates the use of several commands with alternate parameters settings.