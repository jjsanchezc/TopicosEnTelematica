from mrjob.job import MRJob


class UsuarioCaliXPeliProm(MRJob):

    def mapper(self, _, line):
        id_usuario,id_pelicula,calificacion,genero,fecha=line.split(',')
        yield id_pelicula, (1, float(calificacion))

    def reducer(self, id_pelicula, values):
        user_count = 0
        calificacion_sum = 0
        
        # Recorre para hacer sumatoria de usuarios y calificaciones
        for value in values:
            user_count += value[0]
            calificacion_sum += value[1]
        
        average_calificacion = calificacion_sum / user_count
        yield id_pelicula, (user_count, average_calificacion)




if __name__ == '__main__':
    UsuarioCaliXPeliProm.run()