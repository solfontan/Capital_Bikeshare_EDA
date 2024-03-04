import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kurtosis, skew

def cardinalidad(df: pd.DataFrame):
    cardi = pd.DataFrame(columns=['cardinalidad', 'porcentaje_cardinalidad', 'tipo_de_dato', 'valores_unicos', 'tipo_de_variable'],
                         index=df.columns)

    cardi['cardinalidad'] = [df[col].nunique() for col in df.columns]
    cardi['porcentaje_cardinalidad'] = cardi['cardinalidad'] / len(df) * 100
    cardi['tipo_de_dato'] = df.dtypes
    cardi['valores_unicos'] = [valor if valor <= 15 else 'valores unicos no representativos' for valor in
                               [df[columna].nunique() for columna in df.columns]]

    valores_tipo_variable = [input(f'Para la columna {columna} ingrese el valor "Tipo_de_variable": ') for columna in df.columns]
    cardi['tipo_de_variable'] = valores_tipo_variable

    return cardi

def extended_describe(column, df):
    describe_df = df[column].describe()
    # Crear un nuevo DataFrame con las estadísticas extendidas
    extended_describe_df = pd.DataFrame({
        'count': describe_df['count'],
        'mean': describe_df['mean'],
        'median':df[column].median(),
        'mode' : df[column].mode()[0],
        'std' : round(describe_df['std'],2),
        'min': describe_df['min'],
        '25%': describe_df['25%'],
        '50%': describe_df['50%'],
        '75%': describe_df['75%'],
        'max': describe_df['max'],
        'kurtosis': round(kurtosis(df[column]), 2),
        'skewness': round(skew(df[column]),2)
    }, index=[column])
    
    if kurtosis(df[column]) > 0 :
        print(f"La distribución es leptocúrtica con una curtosis de {round(kurtosis(df[column]), 2)}. Los datos se encuentran concentrados alrededor de la media.")
    elif kurtosis(df[column]) < 0 :
        print(f"La distribución es platicúrtica con una curtosis de {round(kurtosis(df[column]), 2)}. Los datos se encuentran dispersos.")
    elif kurtosis(df[column]) == 0 :
        print(f"La distribución es mesocúrtica con una curtosis de {round(kurtosis(df[column]), 2)}. Los datos se comportan de manera normal")
        
    if skew(df[column]) > 0 :
        print(f"La distribución se encuentra sesgada hacia la izquierda {round(skew(df[column]),2)}.")
    else:
        print(f"La distribución se encuentra sesgada hacia la derecha {round(skew(df[column]),2)}.")
        
    return extended_describe_df

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

    ax_hist.set_ylabel('Frecuencia')
    extended_description_df = extended_describe(columna, df)  # Llamada a la función extended_describe
    
    return extended_description_df
    
    
def grafico_bivariante(df : pd.DataFrame, x : str, xname: str,  y: str, yname :str,  forma : str, color_jointplot='#b81414', title=None) -> sns.jointplot:
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

        plt.xlabel(xname)
        plt.ylabel(yname)
        
        return plot
    else:
        print("Error en el tipo de gráfica")
