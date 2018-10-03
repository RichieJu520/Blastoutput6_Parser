# Blastoutput6_Parser

This project contains python scripts for processing blast output (format 6).

Hits_Extractor_Batch.py
A python script for filtering blast output so that only the best N (input parameter) hits are reported. All the hits will be reported for a query sequecne with less than N hits in the blast output. For extracting the best hit, set N as 1.

Hits_Filter_Batch.py
A python script for filtering blast output results by identity (e.g., 80), alignment length (e.g., 75), evalue (e.g., 1e-3) and bitscore (e.g., 50)

The above scripts were originally written in 2012 and has been recently modified and applied for the identification of mRNA internal standard reads from spiked metatranscritpomes (to realize absolute transcript quantification). Please refer to the Bioinformatics-Metatranscriptome section in the Supporting Information of the following paper for details on the paramter setups:

Ju F, Beck K, Yin X, McArdell Christa, Singer H, Johnson D, Zhang T, Buergmann H *. 2018. Wastewater treatment plant resistomes are shaped by bacterial composition, genetic exchange and up-regulated expression in the effluent. The ISME Journal Published: 24 September 2018
Link to paper: https://www.nature.com/articles/s41396-018-0277-8#MOESM1
