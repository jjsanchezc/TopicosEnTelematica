from mrjob.job import MRJob


class MostWatchedDayMR(MRJob):

    def mapper(self, _, line):
        fields = line.split(',')
        
        # Extrae la fecha de la línea
        date = fields[4]
        
        # fecha como clave 
        yield date, 1

    def reducer(self, date, values):
        # Calcula la cantidad total de películas vistas para cada fecha
        total_movies = sum(values)
        
        # Emite la cantidad total de películas vistas junto con la fecha
        yield total_movies, date



if __name__ == '__main__':
    MostWatchedDayMR.run()