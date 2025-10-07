def main() -> None:
    pass

def plot_bigrams(B_mtx, chars, ax):
    ax.imshow(B_mtx, cmap="inferno")
    ax.set_title('Character bigrams')
    ax.set_yticks(range(len(chars)), labels=chars)
    ax.set_xticks(range(len(chars)), labels=chars)

    # Text annotations
    for i in range(len(chars)):
        for j in range(len(chars)):
            if B_mtx[i, j] > 150:
                c = "k"
            else:
                c = "w"
            ax.text(j, i, f"({chars[i]} {chars[j]})\n{int(B_mtx[i, j].item())}", ha="center", va="center", color=c)
    return ax

def letter_sorted(raw_dict):
    tr_alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"

    new_dict = {}
    for let in tr_alphabet:
        if let in raw_dict.keys():
            new_dict[let] = raw_dict[let]
    return new_dict

def tr_lower(text):
    text = text.replace('İ', 'i').replace('I', 'ı')
    return text.lower()

if __name__ == 'main':
    main()