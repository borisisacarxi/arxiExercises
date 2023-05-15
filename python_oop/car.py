'''
6. Crie uma classe chamada "Car" que possua os seguintes atributos: marca, modelo, ano e velocidade atual. Também inclua um
método chamado "acelerar" que aumente a velocidade atual em 5 km/h e outro método chamado "frear" que diminua a velocidade atual em 5 km/h.

7.Crie uma instância da classe "Car" e atribua valores aos atributos. Em seguida, chame o método "acelerar" e "frear" e imprima a velocidade
atual do carro antes e depois de cada chamada.

'''

def printDict(dicionary):
    for key, value in dicionary.items():
        print('{:>10}: {:>10}'.format(key, value))

class Car:
    def __init__(self, brand, model, release, spead = 5):
        self.brand = brand
        self.model = model
        self.release = release
        self.spead = spead

    def aceleration(self):
        self.spead = 15 #safty first
    def stop(self):
        self.spead = 0


brand = input('Brand: ')
model = input('Model: ')
year = input('Year: ')

car1 = Car(brand,model, year)

print('car {} {} {}, has been creatad with such parametrs:'.format(brand, model, year).upper())
printDict(car1.__dict__)

print('Car {} {} {}, stoped:'.format(brand, model, year).upper())
car1.stop()
printDict(car1.__dict__)

print('Car {} {} {}, acelareted again'.format(brand, model, year).upper())
car1.aceleration()
printDict(car1.__dict__)