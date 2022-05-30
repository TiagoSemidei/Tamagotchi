from random import randrange


class Pet(object):
    ''''Pet virtual'''
    excitacao_max = 10
    excitacao_perigo = 3
    comida_max = 10
    comida_perigo = 3
    vocab = ['"Grrr..."']

    def __init__(self, nome, animal_tipo):
        self.nome = nome
        self.animal_tipo = animal_tipo
        self.comida = randrange(self.comida_max)
        self.excitacao = randrange(self.excitacao_max)
        self.vocab = self.vocab[:]

    def __clock_tick(self):
        self.excitacao -= 1
        self.comida -= 1

    def humor(self):
        if self.comida > self.comida_perigo and self.excitacao > self.excitacao_perigo:
            return "feliz"
        elif self.comida < self.comida_perigo:
            return "faminto"
        else:
            return "entediado"

    def __str__(self):
        return "\nEu " + self.nome + "." + "\nEstou me sentindo  " + self.humor() + "."

    def ensinar(self, palavra):
        self.vocab.append(palavra)
        self.__clock_tick()

    def falar(self):
        print(
            "Eu sou ",
            self.animal_tipo,
            " chamado ",
            self.nome,
            ".",
            "Eu me sinto ",
            self.humor(),
            " agora.\n"
        )

        print(self.vocab[randrange(len(self.vocab))])

        self.__clock_tick()

    def alimentar(self):
        print("**Nhac*** \n Hmmm...tamo junto!")
        meal = randrange(self.comida, self.comida_max)
        self.comida += meal

        if self.comida < 0:
            self.comida = 0
        elif self.comida > self.comida_max:
            self.comida = self.comida_max
            print("Eu estou cheio!")
        self.__clock_tick()

    def brincar(self):
        print("Woohoo")
        divercao = randrange(self.excitacao, self.excitacao_max)
        self.excitacao += divercao
        if self.excitacao < 0:
            self.excitacao = 0
            print("Estou entediado")
        elif self.excitacao > self.excitacao_max:
            self.excitacao = self.excitacao_max
            print("Eu to muito feliz!")
        self.__clock_tick()


def main():
    pet_nome = input("Que nome você gostaria de dar ao seu Pet? ")
    pet_type = input("Que tipo de animal é o seu Pet? ")

    my_pet = Pet(pet_nome, pet_type)
    input(f'Olá! Eu sou {my_pet.nome} e eu sou novo aqui!\nAperte ENTER para continuar.')
    escolha = None

    while escolha != 0:
        print("""
            ***INTERAGIR COM SEU PET***

            1 - Alimentar seu pet
            2 - Falar com seu pet
            3 - Ensinar uma nova palavra a seu pet
            4 - Brincar com seu pet
            0 - Sair
            """
              )
        escolha = input("Escolha : ")

        if escolha == "0":
            print("Até mais!")
            exit()
        elif escolha == "1":
            my_pet.alimentar()
        elif escolha == "2":
            my_pet.falar()
        elif escolha == "3":
            new_palavra = input("\nQue palavra você gostaria de ensinar ao seu Pet? ")
            my_pet.ensinar(new_palavra)
        elif escolha == "4":
            my_pet.brincar()
        else:
            print("Desculpe, esta não é uma opção válida!")


main()