from mrjob.job import MRJob


class SecXEmp(MRJob):

    def mapper(self, _, line):
        fields = line.split(',')   
        idemp, sector,salary,year = line.split(',')
        yield idemp, sector

    def reducer(self, id_emp, sectors):
        # Calcula el número de sectores económicos únicos para cada empleado
        sectores = set(sectors)
        numero_sectores = len(sectores)
        
        # Emite el ID del empleado y el número de sectores económicos como resultado final
        yield id_emp, numero_sectores

if __name__ == '__main__':
    SecXEmp.run()