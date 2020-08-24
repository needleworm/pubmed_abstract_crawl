# pubmed_abstract_crawl
Crawling PubMed Papers' Abstracts and Chemicals.

## Usage
> import pmcrawl as P
>
>P.crawl_abstract(keyword, outfile=None, max_iter=1000, has_chem_only=False)
>
outfile is the name of output file. Default is \<\[Crawling Results]_<keyword>.csv>. 
You may provide customized filename including file extension. ".tsv" is recommended.

max_iter is the number of iterations.

When has_chem_only value is True, it skips articles without PubChem info.

The result is tab-separated values (.tsv).

## Requirement
>pip install metapub
