from mrjob.job import MRJob


class BWRating(MRJob):
    def mapper(self, _, line):
        id_usuario,id_pelicula,calificacion,genero,fecha=line.split(',')
        yield genero, (float(calificacion), id_pelicula)

    def reducer(self, genero, values):
        mejor_pelicula = None
        mejor_calificacion = float('-inf')
        peor_pelicula = None
        peor_calificacion = float('inf')
        
        # Recorre los valores y encuentra la mejor y peor película por género
        for value in values:
            calificacion, pelicula = value
            if calificacion > mejor_calificacion:
                mejor_calificacion = calificacion
                mejor_pelicula = pelicula
            if calificacion < peor_calificacion:
                peor_calificacion = calificacion
                peor_pelicula = pelicula
        
        yield genero, (mejor_pelicula, peor_pelicula)

if __name__ == '__main__':
    BWRating.run()