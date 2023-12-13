import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kurtosis, skew


def grafico_univariante(df : pd.DataFrame, columna : str, color_boxplot='#b81414', color_hist='#b81414'):
    """ Pasamos un DataFrame con su columna, para que nos retorne dos gráficos.
    - El primero será de tipo boxplot con medidas estadísticas : mediana - std.
    - El segundo será un histograma para ver cómo es la distribución de los datos.

    Args:
        df (DataFrame): DataFrame
        columna (_type_): Nombre de la columna
        color_boxplot (str): Color para el boxplot (por defecto: lightblue)
        color_hist (str): Color para el histograma (por defecto: lightblue)
    """

    fig, ax = plt.subplots(figsize=(8, 8))

    # Agregar el gráfico de caja (boxplot) arriba
    sns.boxplot(df[columna], ax=ax, showfliers=False, vert=False, color=color_boxplot)

    media = np.mean(df[columna])
    median_val = np.median(df[columna])
    std_val = np.std(df[columna])
    kurtosis_valor = kurtosis(df[columna])
    simetria_valor = skew(df[columna])

    ax.axvline(median_val, color='white', linestyle='dashdot', linewidth=2, label=f'Median: {median_val:.2f}')
    ax.axvline(media + std_val, color='black', linestyle='dashdot', linewidth=2, label=f'std: {std_val:.2f}')
    ax.axvline(media - std_val, color='black', linestyle='dashdot', linewidth=2, label=f'std: {std_val:.2f}')

    leg = ax.legend()
    leg.set_bbox_to_anchor((1, 0.05)) 

    # # Eliminar los ticks del eje y del gráfico de caja
    ax.set_yticklabels([])
    ax.set_yticks([])

    # Agregar el gráfico de histograma en el centro
    ax_hist = fig.add_axes([0.1, 0.45, 0.8, 0.4])
    sns.histplot(df[columna], kde=False, ax=ax_hist, color=color_hist)
    
    # Ajustar la posición del gráfico de caja
    pos = ax.get_position()
    pos.y0 = 1.02
    ax.set_position(pos)

    ax_hist.set_ylabel('Frequency');
    
    print(f"kurtosis: {kurtosis_valor:.2f}")
    print(f"simetria: {simetria_valor:.2f}")

    if kurtosis_valor > 3:
        print("La distribución es leptocúrtica, lo que sugiere colas pesadas y picos agudos.")
    elif kurtosis_valor < 3:
        print("La distribución es platicúrtica, lo que sugiere colas ligeras y un pico achatado.")
    else:
        print("La distribución es mesocúrtica, similar a una distribución normal.")

    if simetria_valor > 0:
        print("La distribución es asimétrica positiva (sesgo hacia la derecha).")
    elif simetria_valor < 0:
        print("La distribución es asimétrica negativa (sesgo hacia la izquierda).")
    else:
        print("La distribución es perfectamente simétrica alrededor de su media.")
    
    
def grafico_bivariante(df : pd.DataFrame, x : str, y: str, forma : str, color_jointplot='#b81414', title=None) -> sns.jointplot:
    """ Grafico bivariante con el fin de retornar un jointplot entre variables para un análisis más práctico
    arg:
    df : DataFrame
    x : columna de df que se quiere analizar en el eje x - tipo STR
    y : columna de df que se quiere analizar en el eje y - tipo STR
    type : tipo de gráfica que se quiere mostrar, puede ser ['scatter' , 'kde' , 'hist' , 'hex' , 'reg' , 'resid'] - tipo STR
    title :  viene por defecto en None - tipo STR
    
    return:
        gráfica de seaborn jointplot
    """
    import seaborn as sns
    
    form = ['scatter' , 'kde' , 'hist' , 'hex' , 'reg' , 'resid']
    if forma in form:
        plot = sns.jointplot(data = df, x = x, y = y, kind=forma, marginal_ticks=True, color=color_jointplot)
        plot.fig.suptitle(title, y=1.05)

        return plot
    else:
        print("Error en el tipo de gráfica")
