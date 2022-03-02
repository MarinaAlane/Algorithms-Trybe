def find_duplicate(nums):
    ordered_nums = bubble_sort(nums)
    if len(ordered_nums) < 2 or ordered_nums[0] < 1:
        return False

    for index in range(len(ordered_nums) - 1):
        if ordered_nums[index] == ordered_nums[index + 1]:
            return True
    return False


def bubble_sort(array):
    # variável utilizado na iteração
    # para marcar se houve ou não trocas naquela iteração
    # Quando falsa, indica que o array está ordenado
    has_swapped = True

    # armazena o número de iterações para evitar
    # a iteração sobre índices já ordenados
    num_of_iterations = 0

    try:
        # Enquanto ainda não está ordenado (ocorreram trocas na iteração)
        while has_swapped:
            has_swapped = False
            # percorra o array até o ultimo índice não ordenado
            for i in range(len(array) - num_of_iterations - 1):
                # caso a posição corrente seja maior que a posterior
                if array[i] > array[i + 1]:
                    # realiza a troca entre as posições
                    array[i], array[i + 1] = array[i + 1], array[i]
                    # marca que tivemos trocas nesta iteração
                    has_swapped = True
            num_of_iterations += 1
            return array

    except TypeError:
        return []
