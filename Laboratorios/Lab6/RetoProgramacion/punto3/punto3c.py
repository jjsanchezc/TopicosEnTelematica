from mrjob.job import MRJob


class MenorCantidadPeli(MRJob):

    def mapper(self, _, line):
        id_usuario,id_pelicula,calificacion,genero,fecha=line.split(',')
        yield fecha, 1

    def reducer(self, fecha, values):
        # Calcula la cantidad total de películas vistas para cada fecha
        total_peliculas = sum(values)
        
        yield total_peliculas, fecha



if __name__ == '__main__':
    MenorCantidadPeli.run()
