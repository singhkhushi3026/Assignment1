import pandas as pd
import matplotlib.pyplot as plt

def analyze_csv(file_path):

    data = pd.read_csv(file_path)

    mean = data.mean()
    median = data.median()
    mode = data.mode()
    std = data.std()

    correlations = data.corr()

    data.hist()
    plt.savefig('histogram.png')
    plt.close()

    data.plot.scatter(x='column1', y='column2')
    plt.savefig('scatter_plot.png')
    plt.close()

    data.plot()
    plt.savefig('line_plot.png')
    plt.close()

    results = {
        'mean': mean,
        'median': median,
        'mode': mode,
        'std': std,
        'correlations': correlations,
        'histogram_path': 'histogram.png',
        'scatter_plot_path': 'scatter_plot.png',
        'line_plot_path': 'line_plot.png'
    }

    return results

def main():
    file_path = input("Enter the path to the CSV file: ")

    results = analyze_csv(file_path)

    print("Mean:", results['mean'])
    print("Median:", results['median'])
    print("Mode:", results['mode'])
    print("Standard deviation:", results['std'])
    print("Correlations:")
    print(results['correlations'])

    import webbrowser
    webbrowser.open_new_tab('histogram.png')
    webbrowser.open_new_tab('scatter_plot.png')
    webbrowser.open_new_tab('line_plot.png')

if __name__ == '__main__':
    main()
