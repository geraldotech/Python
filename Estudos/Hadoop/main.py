""" 
, uma biblioteca Python desenvolvida pela Yelp que facilita a escrita e execução de jobs MapReduce, tanto localmente quanto em plataformas como Hadoop, Amazon EMR e Google Cloud Dataproc

pip install mrjob

 """
from mrjob.job import MRJob
import re


# Expressão regular para extrair palavras
palavra_regex = re.compile(r"[\w']+")


class QuantidadePalavras(MRJob):
    def mapper(self, _, linha):
        for p in palavra_regex.findall(linha):
            yield (p.lower(), 1)

    def reducer(self, p, qtd):
        yield (p, sum(qtd))


if __name__ == '__main__':
    QuantidadePalavras.run()
 