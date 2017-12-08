Structure of the BNGL file
===============================================================================

BNGL files are currently divided into two parts, the model specification and a
set of commands that operate on the model.  The commands that generate a model
based on the model specification are discussed in the following sections.
Here, we describe the components of the model specification.

The model specification consists of four blocks, each beginning with a line
containing a begin <blockname> command and ending with a line containing an
end <blockname> command.  The four block names are parameters, species,
reaction rules and observables.  They may appear in any order, although,
because of the dependencies the above order is the most logical.

