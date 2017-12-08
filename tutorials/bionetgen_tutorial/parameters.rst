Parameters
============================================================================================

Parameters are used to provide numerical values for variables that may appear
in the species and reaction rules blocks.  Parameters are generally used to
specify initial concentrations of species and rate constants for reaction
rules. A simple parameter block looks like

.. code-block:: ${1:type}

	begin parameters
  		R0   1
  	 	kp1  0.5
   		km1  0.1
   		kp2  1e-3
   		km2  0.1
   		p1  10
   		d1   5
   		kpA  1-e4
   		kmA  0.02
	end parameters
	
The number in the first column is an index, which is provided solely for the convenience of
the user.  Parameters are referred to both in input and output by name and the
index is ignored by the program.  Specification of an index is optional,
e.g. the first parameter line could read

.. code-block:: ${1:type}

	R0 1

The second column provides the parameter name.  Names must start with an
alphabetical character and may contain only alphanumeric characters and
underscores (_).


