from mrjob.job import MRJob


class ValorAccionXDia(MRJob):

    def mapper(self, _, line):
        # compalia,precio,fecha
        company, precio, date = line.split(',')
        yield company, (float(precio), date)

    def reducer(self, company, valores):
        min_valor = None
        max_valor = None
        min_date = None
        max_date = None
        # Ciclo para encontrar los dias con menor y mayor valor en las acciones de cada empresa
        for precio, date in valores:
            if max_valor is None or precio > max_valor:
                max_valor = precio
                max_date = date
            if min_valor is None or precio < min_valor:
                min_valor = precio
                min_date = date

        # Retorna los dias que acabamos de encontrar
        yield company, (min_date, min_valor, max_date, max_valor)


if __name__ == '__main__':
    ValorAccionXDia.run()
