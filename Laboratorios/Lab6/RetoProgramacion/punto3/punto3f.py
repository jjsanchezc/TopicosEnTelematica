from mrjob.job import MRJob


class BestRatingDayMR(MRJob):
    def mapper(self, _, line):
        fields = line.split(',')
        # Extrae la fecha y el calificacion de la línea
        fecha = fields[4]
        calificacion = float(fields[2])
        yield fecha, calificacion
    
    def reducer(self, fecha, calificacions):
        calificacion_sum = 0
        calificacion_count = 0
        # Recorre para hacer sumatoria
        for calificacion in calificacions:
            calificacion_sum += calificacion
            calificacion_count += 1
        average_calificacion = calificacion_sum / calificacion_count
        yield average_calificacion, fecha


if __name__ == '__main__':
    BestRatingDayMR.run()