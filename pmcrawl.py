"""
Author : Byunghyun Ban
Last Modification : 2020.08.19.
halfbottle@sangsang.farm
https://github.com/needleworm
"""

from metapub import PubMedFetcher


def crawl_abstract(keyword, outfile=None, max_iter=1000):
    fetch = PubMedFetcher()

    pmids = fetch.pmids_for_query(keyword, retmax=max_iter)
    print("PMID scan Done!")

    if not outfile:
        outfile = "[Crawling Results]" + keyword + ".csv"

    o_file = open(outfile, 'w', encoding="utf8")

    header = "PMID, Authors, Year, Title, Abstract, URL, Citation, Chemicals\n"
    o_file.write(header)

    for pmid in pmids:
        article = fetch.article_by_pmid(pmid)
        if not article: continue
        authors = article.authors_str
        if not authors: continue
        year = article.year
        if not year: continue
        title = article.title
        if not title: continue
        abstract = article.abstract
        if not abstract: continue
        url = article.url
        if not url: continue
        citation = article.citation
        if not citation: continue
        chemical = article.chemicals
        if not chemical:
            chemical = "None"
        else:
            chemical =str(chemical)

        print(article.citation)

        o_file.write(pmid + ", ")
        o_file.write(authors + ", ")
        o_file.write(year + ", ")
        o_file.write(title + ", ")
        o_file.write(abstract + ", ")
        o_file.write(url + ", ")
        o_file.write(citation + ",")
        o_file.write(chemical + "\n")

    o_file.close()
    print("Process Done!")
    print("Result is saved in <" + outfile + ">.")



