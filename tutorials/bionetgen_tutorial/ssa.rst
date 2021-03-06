Simulating SSAs
======================================================================================================

The ``simulate_ssa`` command is used to compute a timecourse of the network using
the Gillespie direct algorithm for simulation of the stochastic master
equations.  When using this method to simulate a network, the species
concentrations must be provided in number of molecules (per cell or per
fraction of a cell) and the rate constants must be scaled accordingly.  BNG2
does not currently provide any functions for performing unit conversions.  The
simulate_ssa interface is still incomplete and additional functionality will
be added as needed. Currently, only one simulation run can be performed per
command invocation.

The main difference between the simulate_ssa command and standard Gillespie
implementations, is that species and reactions can be generated by application
of the reation rules on-the-fly.  No special parameters are required to access
this functionality.  This is done by keeeping track of whether the reaction
rules have been applied to each species.  When a species to which the rules
have not been applied becomes populated for the first time, the rules are
applied to that species to generate new reactions and species and to update
observables.  This adaptive generation of the network is particularly useful
for infinite networks.  A simulation can be carried out adaptively by setting
a small value for max_iter in the generate_network command prior to the
simulate_ssa command, or, alternatively, but not invoking generate_network at
all.  The stochastic simulation will then map out the network over the course
of the simulation. 

Parameters for the simulate_ssa command:	

+--------------------+---------------------------------------------------------+---------------+
| Name               | Function                                                | Default Value |
+====================+=========================================================+===============+
| n_steps            | Number of intervals at which to report concentrations   | 1             |
+--------------------+---------------------------------------------------------+---------------+
| prefix             | Base name of CDAT and GDAT files                        | Base name of  |
|                    |                                                         | BNGL file     |
+--------------------+---------------------------------------------------------+---------------+
| sample_times       | Times at which concentrations are reported              | None          |
|                    | (supercedes requirment for t_end)                       |               |
+--------------------+---------------------------------------------------------+---------------+
| t_start            | Starting time for integration                           | 0             |
+--------------------+---------------------------------------------------------+---------------+
| t_end              | End time for integration                                | None          |
+--------------------+---------------------------------------------------------+---------------+
| verbose            | Additional output for debugging                         | 0 (Off)       |
+--------------------+---------------------------------------------------------+---------------+
