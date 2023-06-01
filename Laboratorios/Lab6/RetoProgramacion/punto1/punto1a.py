from mrjob.job import MRJob

class PromedioSalarioSector(MRJob):

    def mapper(self, _, line):
        idemp, sector,salary,year = line.split(',')
        yield sector,int(salary)


    def reducer(self, sector,salario):
        contador_salario=0
        sumatoria=0
        #ciclo para empezar a sacar el promedio
        for sala in salario:
            sumatoria+=int(sala)
            contador_salario+=1
        promedio=sumatoria/contador_salario

        yield sector,promedio

if __name__ == '__main__':
    PromedioSalarioSector.run()
