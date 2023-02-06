import matplotlib.pyplot as plt

def generar_bar(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()


if __name__ == "__main__":
    labels =["a", "b", "c"]
    values = [100, 150, 200]
    generar_bar(labels, values)
    