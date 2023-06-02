from mrjob.job import MRJob


class DiaPeorPromCali(MRJob):
    def mapper(self, _, line):
        id_usuario,id_pelicula,calificacion,genero,fecha=line.split(',')
        yield fecha, float(calificacion) # Emite la fecha como clave y el calificacion como valor

    def reducer(self, fecha, calificaciones):
        calificacion_sum = 0
        calificacion_count = 0
        
        for calificacion in calificaciones:
            calificacion_sum += calificacion
            calificacion_count += 1
        
        average_calificacion = calificacion_sum / calificacion_count # Calcula el calificacion promedio
        
        yield average_calificacion, fecha # Emite el calificacion promedio junto con la fecha



if __name__ == '__main__':
    DiaPeorPromCali.run()
