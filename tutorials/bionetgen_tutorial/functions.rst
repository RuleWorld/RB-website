Functions
===============================================================================

In BioNetGen 2.2.0, the functions block was introduced to allow for the definition of arbitrary mathematical formulas for rate laws. The syntax of a line in the functions block is

    [label:] functionName([argument1,argument2,...]) [=] functionDef

where functionName is a valid BioNetGen object name (see Note 6), each optional argument is a reference (tag) to a molecule or complex (see BNGManual:Tags), and functionDef is a mathematical expression involving numbers, built-in operators and functions, parameters, observables and, if applicable, the function arguments. If a function is defined with arguments, these must be passed as arguments to observables in the function expression, where they act as the scope over which the observable is calculated. Functions with arguments are thus referred to as local functions because they are calculated over a restricted subset of the molecules in the system. Conversely, functions without arguments are referred to as global functions since they are evaluated over the entire simulation domain.

An example illustrating the use of both global and local functions is given in BNGManual:Model 4. This simple model of gene expression is comprised of a single DNA molecule, mRNA transcripts, and proteins. The system is self-amplifying in that the rate of promoter activation increases with increasing amount of protein in the system. In the molecule types block, the DNA molecule is modeled as having a single promoter component, which can be in an inactive ('0') or active ('1') state, and three identical protein-binding sites,

    DNA(prot,prot,prot,promoter~0~1) .

mRNA transcripts are modeled as unstructured species,

    mRNA() ,

and proteins are modeled as having a single promoter-binding site,

    Protein(dna) .

In the reaction rules block, rules are defined for DNA-protein binding/unbinding, promoter activation/deactivation, mRNA transcription, protein translation, and mRNA and protein degradation. Protein binding and unbinding at each prot site on the DNA molecule is assumed to occur independently with equal rate,

    DNA(prot) + Protein(dna) <-> DNA(prot!0).Protein(dna!0) kp, km .

However, the rate (probability) of promoter activation is assumed to depend strongly on the number of bound proteins, which is quantified in the observables block as

    Molecules DNA_Prot DNA(prot!0).Protein(dna!0)  .

The rate of promoter activation is then defined in the functions block as

    DNA_activation(x) = 0.01 + k_act*DNA_Prot(x)^2 .

We see that the basal rate of promoter activation (no bound proteins) is 0.01, and that the rate increases with the square of the number of bound proteins. Here, 'x' is a reference to the molecule or complex over which the observable DNA_Prot is to be calculated. Thus, DNA_activation is a local function. In the reaction rules block we then define the rule for promoter activation/deactivation as

    %c:DNA(promoter~0) <-> %c:DNA(promoter~1) DNA_activation(c), k_deact .

Here, we use the "prefix" tagging notation, i.e., the "%" character followed by a string label ("c" in this case) and then a colon. This indicates that the tag 'c' references the complex to which the proceeding pattern is matched (as opposed to the DNA molecule; for a general discussion of tags in BNGL see BNGManual:Tags). Note that the rate for reactions generated from this rule will equal DNA_activation multiplied by the population (concentration) of the reactant species (since there is only a single DNA molecule in this case, that value will be either 0 or 1 for stochastic simulations and between 0 and 1 for ODE simulations). In other words, the function DNA_activation acts as an effective single-site rate constant (see Note 21).

An example of a global function can be found in the definition of the mRNA transcription rule,

    0 -> mRNA() mRNA_synth() ,

where "0" is the null symbol (see Note 49), mRNA_synth() is defined in the functions block as

    mRNA_synth() = v0*DNA_Active ,

and DNA_Active is defined in the observables block as

    Molecules DNA_Active DNA(promoter~1) .

This rule states that the rate of mRNA transcription is proportional to the number of active promoters, quantified through the observable DNA_Active. Note that the rule could have been written in a more verbose, but equivalent, fashion without using functions as DNA(promoter~1) -> DNA(promoter~1) + mRNA() v0 .

It is important to recognize the distinction between mRNA_synth as a global function and DNA_activation as a local function. mRNA transcription is a global process in that it depends simply on the number of activated promoters. If we were to add an additional gene, say on a plasmid, then the rate of transcription would double if both were active. However, the rate of activation of a promoter depends on the number of proteins bound to the specific gene. Adding a second gene does not directly affect the rate of activation of the promoter on the first gene, i.e., promoter activation is a local process.

Finally, the model also illustrates an "inline" function definition in the reaction rules block,

    0 -> Protein(dna) v1*mRNA_Total   # Prot_synth() ,

where the observable mRNA_Total is defined in the observables block as

    Molecules mRNA_Total mRNA() .

Note the commented out call to the global function Prot_synth() defined as v1*mRNA_Total in the functions block. This is to illustrate that users are free to define functions (global and local) in either, or both, of the functions and reaction rules blocks based on convenience.

NOTE: Inline local functions are not currently supported in NFsim (v1.11). 