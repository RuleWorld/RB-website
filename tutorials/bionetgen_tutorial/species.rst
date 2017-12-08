Species
=================================================================================================

The species block is used to define the molecules that are present at the
start of network generation.  It might more accurately be called the "seed
species" block, but we have kept the name species for historical reasons.
Molecules are structured objects comprised of components that can have states
and can bind to each other, both within a molecule and between molecules.
When a molecule is declared in the species block, all of its components must
be declared and those components that can be in different states must have a
defined state.  As an example, consider a receptor (``R``) with three components:
a ligand binding site (``l``), a dimerization domain (``d``), and a site of tyrosine
phosphorylation (``Y``).  Here's how we would define such a molecule in the
species block:

.. code-block:: ${1:type}

	R(l,d,Y~U) R0

The parentheses surround the list of components, which appear as a
comma-separated list.  The ~ character indicates the start of a component
state label.  Here, the component ``Y`` is in the state ``U``, which stands for
unphosphorylated.  It is important to remember that spaces may not appear
anywhere inside the molecule string. Thus, the declaration

.. code-block:: ${1:type}

	R(l, d,Y~U) R0

would produce an error that would cause to program to stop.  Spaces may also
not appear in any species or pattern (see next subsection for a definition.
``R0`` in the second column of the species declaration indicates that initial
concentration of the declared species is determined by the parameter ``R0``.
Referring to an undefined parameter here will cause an error.  The initial
concentration can also be set by using a numerical value in the second column.

Let's expand the species declaration to include a ligand (``L``) and a cytosolic
adaptor protein (``A``). The species block is 

.. code-block:: ${1:type}

	begin species
    		L(r)       L0
    		R(l,d,Y~U) R0
    		A(SH2)     A0
	end species

As with all other blocks in the BNGL file, the index here is optional and
disregarded when the file is processed.  However, BNG2 does assign an index to
each species (based on the order of appearance or generation), and this index
is written to the species block in the output NET file created using the
generate_network command (see below).  These indices are used to refer to
species in the reactions and groups blocks of the NET file.  

For any molecule that we want to be able to bind another molecule we must
define at least one binding component.  A component that appears in a species
declaration without a state label may be used only for binding and may not
take on a state label in subsequent occurences of the same molecule.  Note
that the namespaces for compoents of different molecules are separated, so it
is permissable in this example to have a molecule ``B(SH2)``, or even ``B(SH2~U)``.
It is also allowed to have molecules with no components, which can be used as
dummy species or counters. For example, a species could be declared as

.. code-block:: ${1:type}

	E1 1

After the first occurence of a molecule in the species list, all appearances of
molecules with the same name must have the same components, although their
state labels may differ.  For example the species 

.. code-block:: ${1:type}

  R(l,d,Y~P)

could appear in the species list defined above, but the species

.. code-block:: ${1:type}

  R(l,d1,d2,Y~P)

could not.

Species may also be comprised of complexes of two or more molecules, connected
by bonds between molecular components.  Bonds may join components within the
same molecule or between different molecules.  Bonds are declared as links
between components indicated by an '!' character followed by a name, usually
an integer.  Each bond name must occur exactly two times within a species to
specify the pair of components that are connected by the bond.  The '.'
character is used to concatenate molecules within a complex.  For example, a
ligand-receptor complex would be written as

.. code-block:: ${1:type}

  L(r!1).R(l!1,d,Y~U)

with the link labeled 1 indicating a bond between component ``r`` of molecule ``L``
and component ``l`` of molecule ``R``.  A larger complex containing a dimer of
ligand-bound receptors would be declared as

.. code-block:: ${1:type}

  L(r!1).R(l!1,d!3,Y~U).L(r!2).R(l!2,d!3,Y~U)

Bond 1 joins the first L molecule to the first ``R`` molecule, Bond 2 joins the
second ``L`` to the second ``R``, and Bond 3 joins the two ``R``'s.  Note that the bond
labels are used only to indicate the connectivity and are interchangeable.
Thus the ligand-receptor complex 

.. code-block:: ${1:type}

  L(r!2).R(l!2,d,Y~U)

is identical to the first complex declared above. Edge labels can be
concatenated with state labels to allow bonds involving components that have
state labels.  They may also be concatenated with other edge labels to allow
multiple bonds to the same components, although this usage is deprecated
because it can often lead to confusion in constructing the reaction rules.  An
example of a component with both state and edge lables is the receptor-adaptor
complex

.. code-block:: ${1:type}

  R(l,d,Y~P!1).A(SH2!1)

Generally speaking, it is not necessary to define complexes that appear
transiently prior to network generation, because they will be generated
automatically by application of the rules.  On the other hand, it may be
desirable to use complexes to represent multi-subunit proteins that are
constitutively associated.  For example, a protein consisting of an alpha and
a beta subunit could be represented as alpha(Y1076~U,b!1).beta(Y1055~U,a!1).
If no reaction rule is specified to dissociate this complex, this complex will
be indivisable.
