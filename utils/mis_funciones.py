import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def grafico_univariante(df : pd.DataFrame, columna):
    """ Psamos un Dataframe con su columna, para que nos retorne dos gráficos.
    - El primero será de tipo boxplot con medidas estadísticas : mediana - std.
    - El segundo será un histograma para ver como es la distribución de los datos.
    
    Args:
        df (DataFrame): typo dataframe
        columna (_type_): 
        
    """
    fig, ax = plt.subplots(figsize=(8, 8))

    # Agregar el gráfico de caja (boxplot) arriba
    sns.boxplot(df[columna], ax=ax, showfliers=False, vert=False)

    media = np.mean(df[columna])
    median_val = np.median(df[columna])
    std_val = np.std(df[columna])

    ax.axvline(median_val, color='red', linestyle='dashdot', linewidth=2, label=f'Median: {median_val:.2f}')
    ax.axvline(media + std_val, color='black', linestyle='dashdot', linewidth=2, label=f'std: {std_val:.2f}')
    ax.axvline(media - std_val, color='black', linestyle='dashdot', linewidth=2, label=f'std: {std_val:.2f}')

    leg = ax.legend()
    leg.set_bbox_to_anchor((1, 0.05)) 

    # Eliminar los ticks del eje y del gráfico de caja
    ax.set_yticklabels([])
    ax.set_yticks([])

    # Agregar el gráfico de histograma en el centro
    ax_hist = fig.add_axes([0.1, 0.45, 0.8, 0.4], sharex=ax)
    sns.histplot(df[columna], kde=False, ax=ax_hist)

    # Eliminar los ticks del eje x del gráfico de histograma
    ax_hist.set_xticks([])
    ax_hist.set_xticklabels([])

    # Ajustar la posición del gráfico de caja
    pos = ax.get_position()
    pos.y0 = 1.02
    ax.set_position(pos)

    ax_hist.set_ylabel('Frequency');
    
    
def grafico_bivariante(df : pd.DataFrame, x : str, y: str, type : str, title=None) -> sns.jointplot:
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
    if type in form:
        plot = sns.jointplot(data = df, x = x, y = y, kind=type, marginal_ticks=True)
        plot.fig.suptitle(title, y=1.02)
        plt.show()
        return plot
    else:
        print("Error en el tipo de gráfica")
