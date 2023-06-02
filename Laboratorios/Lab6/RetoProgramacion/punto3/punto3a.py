from mrjob.job import MRJob


class CalificicacionPeli(MRJob):

    def mapper(self, _, line):
        id_usuario,id_pelicula,calificacion,genero,fecha=line.split(',')

        yield id_usuario, (1, float(calificacion))

    def reducer(self, id_usuario, values):
        movie_count = 0
        calificacion_sum = 0
        # Recorre valores 
        for value in values:
            movie_count += value[0]
            calificacion_sum += value[1]
        average_calificacion = calificacion_sum / movie_count

        yield id_usuario, (movie_count, average_calificacion)



if __name__ == '__main__':
    CalificicacionPeli.run()