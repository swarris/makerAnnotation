
The assembly snakemake pipeline
===============================

The assembly snakemake pipeline is a pipeline for the creation of an assembly 
from raw sequencing reads of any sequencing platform. 

Execution
---------
The pipeline can be run with the following command:

	snakemake --snakefile {/path/to/your/workflow} 
	
Where the outputFile is required when the rule all is not defined in the workflow.

Rules
-----
The rules package only contains rules and functions required by these rules. 

Workflows
---------
The workflows folder implements the MAKER annotation pipeline
	
Configuration
-------------
The configuration of the workflows is always stored in JSON format. The has to be called config.json,
this file has to be stored in the working directly. In each workflow the config has to be parsed by using
the load method of the json module, and has to be stored in a global variable called CONFIG.

The JSON configuration has to follow the schema described in configSchema.json.

	
