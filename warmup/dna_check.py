def hamming(father, child):
    distance = 0
    for c in zip(child, father):
        cn, fn = c
        if cn != fn:
            distance += 1

    return distance



if __name__ == "__main__":
    first_dna = input("1st candidate DNA: ")
    second_dna = input("2nd candidate DNA: ")
    child_dna = input("child DNA: ")

    first_distance = hamming(first_dna, child_dna)
    second_distance = hamming(second_dna, child_dna)
    if first_distance > second_distance:
        print("Second candidate is a father")
    elif first_distance == second_distance:
        print("Error - someone cheating")
    else:
        print("First candidate is a father")