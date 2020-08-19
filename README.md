# pubmed_abstract_crawl
Crawling PubMed Papers' Abstracts and Chemicals.

## Usage
> import pmcrawl as P
>
>P.crawl_abstract(keyword, outfile=None, max_iter=1000)
>
outfile is the name of output file. Default is \<\[Crawling Results]_<keyword>.csv>. 
You may provide customized filename including file extension. ".csv" is recommended.

max_iter is the number of iterations.

The result is tab-separated csv.

## Requirement
>pip install metapub
