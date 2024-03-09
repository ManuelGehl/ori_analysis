import matplotlib.pyplot as plt
import seaborn as sns 

def calculate_gc_skew(sequence: str) -> list:
    # Initialize skew skew_array with 0
    skew_array = [0]
    # Iterate over sequence and add scores if Cytosine or Guanine appear
    for pos, nucleotide in enumerate(sequence):
        if nucleotide == "C":
            current_sum = skew_array[pos] - 1
            skew_array.append(current_sum)
        elif nucleotide == "G":
            current_sum = skew_array[pos] + 1
            skew_array.append(current_sum)
        else:
            current_sum = skew_array[pos] + 0
            skew_array.append(current_sum)

    return skew_array

def plot_skew(skew_array: list) -> None:
    # Plot GC skew as function of positions in genome
    sns.set_style()
    plt.xlabel("Position")
    plt.ylabel("GC Skew Score")
    plt.plot(skew_array)
    plt.show()

    
    
    

#minimum = min(skew_array)
#minimum_indices = [index for index in range(len(skew_array)) if skew_array[index] == minimum]
#print(minimum_indices)