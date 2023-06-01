from mrjob.job import MRJob

# DIA NEGRO: Saque el día en el que la mayor cantidad de acciones tienen el menor valor de acción (DESPLOME), suponga una inflación independiente del tiempo.


class BlackDay(MRJob):

    def mapper(self, _, line):
        company, precio, date = line.split(',')

        yield date, (company, float(precio))

    def reducer(self, date, values):
        min_price_companies = []
        min_price = float('inf')

        # Encuentra el valor de acción más bajo para cada día y guarda las acciones correspondientes
        for company, precio in values:
            if precio < min_price:
                min_price = precio
                min_price_companies = [company]
            elif precio == min_price:
                min_price_companies.append(company)

        yield date, min_price_companies


if __name__ == '__main__':
    BlackDay.run()
