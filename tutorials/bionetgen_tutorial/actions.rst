Actions
================================================================================================================================================

The blocks we have discussed above specify the elements of a BNG2 model.
Statements in the BNGL file not enclosed within blocks are interpreted as
commands by the BNG command interpreter.  These should occur after the model
specification blocks.  At present, the command set is fairly limited but
provides access to a number of different options for applying the rules to
generate a network and for simulating a network.  The major commands, 
``generate_network``, ``simulate_ode``, ``simulate_ssa`` and ``writeSBML``
are discussed in this section. 

When the BNGL file is parsed, the model specification is loaded into a data
structure called BNGModel.  The commands operate on this structure, sending
output both to the BNGModel and to various files.

+--------------------+--------------------------------------------+
| Command            | Output                                     |
+====================+============================================+
| generate_network   | NET file (contains generated species,      |
|                    | reactions and observables)                 | 
+--------------------+--------------------------------------------+
| simulate_{ode,ssa} | CDAT file (concentrations of all species)  |
|                    +--------------------------------------------+
|                    | GDAT file (concentrations of observables)  |
+--------------------+--------------------------------------------+
| writeSBML          | XML file (contains parameters, species,    |
|                    | reactions, and observables in SBML         |
|                    | level 2 format)                            |                    
+--------------------+--------------------------------------------+



The basic syntax for all commands is the same

.. code-block:: ${1:type}

	command_name({param1=>value1,param2=>value2,hash1=>{hash_param1_param1=>hash_value1,...},...});

Command parameters are passed using Perl hashes so that parameter values can
be specified in any order.