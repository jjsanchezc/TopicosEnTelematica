from mrjob.job import MRJob
from mrjob.step import MRStep

class PromedioSalarioEmpleado(MRJob):

    def mapper(self, _, line):
        idemp, sector,salary,year = line.split(',')
        yield idemp,int(salary)


    def reducer(self, idemp,salario):
        contador_salario=0
        sumatoria=0
        #ciclo para empezar a sacar el promedio
        for sala in salario:
            sumatoria+=int(sala)
            contador_salario+=1
        promedio=sumatoria/contador_salario

        yield idemp,promedio

if __name__ == '__main__':
    PromedioSalarioEmpleado.run()
