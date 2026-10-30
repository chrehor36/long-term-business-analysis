from fetch import get
C="1559720"
for out, acc, doc in [
 ("ex991_2026Q2.htm","0001193125-26-337928","d70413dex991.htm"),
 ("ex991_2025Q4.htm","0001193125-26-048670","d58192dex991.htm"),
 ("ex991_2024Q4.htm","0001193125-25-026054","d915198dex991.htm"),
 ("ex991_2023Q4.htm","0001193125-24-033706","d646462dex991.htm"),
 ("eightk_20260316_ex41.htm","0001193125-26-108514","d106317dex41.htm"),
 ("eightk_20260316_ex11.htm","0001193125-26-108514","d106317dex11.htm"),
]:
    r=get(f"https://www.sec.gov/Archives/edgar/data/{C}/{acc.replace('-','')}/{doc}", out); print(out, len(r))
