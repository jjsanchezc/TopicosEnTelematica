from mrjob.job import MRJob

#Listado de acciones que siempre han subido o se mantienen estables.
class EstableAltoStock(MRJob):

    def mapper(self, _, line):
        company, precio, date = line.split(',')
        yield company, float(precio)

    def reducer(self, company, precios):
        price_list = list(precios)
        # Verifica si los precios siempre han subido o se han mantenido estables
        if all(price_list[i] <= price_list[i+1] for i in range(len(price_list)-1)):

            yield company, None

if __name__ == '__main__':
    EstableAltoStock.run()