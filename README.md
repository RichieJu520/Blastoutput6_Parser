# Blastoutput6_Parser

This project contains python scripts for processing blast output (format 6).

Hits_Extractor_Batch.py
A python script for filtering blast output so that only the best N (input parameter) hits are reported. All the hits will be reported for a query sequecne with less than N hits in the blast output. For extracting the best hit, set N as 1.

Hits_Filter_Batch.py
A python script for filtering blast output results by identity (e.g., 80), alignment length (e.g., 75), evalue (e.g., 1e-3) and bitscore (e.g., 50)
