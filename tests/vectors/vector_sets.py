import re

from pkg_resources import resource_listdir, resource_string


VECTOR_FILE_EXTENSION = '.vector'


class VectorSets(object):
    name = __name__

    @classmethod
    def parse_vector_sets(cls):
        vector_sets = dict()
        for vector_file, vector_lines in cls.read_vector_sets().items():
            vector_sets[vector_file] = cls.parse_vectors(vector_lines)
        return vector_sets

    @classmethod
    def read_vector_sets(cls):
        vector_sets = dict()
        for file_name in resource_listdir(cls.name, '.'):
            result = re.search(r'(.+)\.vector$', file_name)
            try:
                key = result.group(1)
            except AttributeError:
                # it is not a vector file
                continue
            else:
                vector_sets[key] = map(
                    lambda line: line.strip(),
                    resource_string(cls.name, file_name).splitlines())
        return vector_sets

    @classmethod
    def parse_vectors(cls, vector_lines):
        raise Exception('Vector parsing not implemented')
