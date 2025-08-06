from bokeh.plotting import figure, show, output_file
from bokeh.layouts import column

class Plotter:
    def plot_training_vs_ideal(self, train_df, matches, ideal_df):
        plots = []
        for col in train_df.columns[1:]:
            p = figure(title=f"{col} vs {matches[col]}", x_axis_label='x', y_axis_label='y', width=600)
            p.line(train_df["x"], train_df[col], legend_label=col, line_width=2)
            p.line(ideal_df["x"], ideal_df[matches[col]], legend_label=matches[col], line_color="green", line_dash="dashed")
            plots.append(p)

        output_file("train_vs_ideal.html")
        show(column(*plots))

    def plot_test_vs_ideal(self, matched_df):
        p = figure(title="Test Matches", x_axis_label="x", y_axis_label="y", width=800)
        p.scatter(matched_df["x"], matched_df["y"], legend_label="Test Points", size=5, color="blue", alpha=0.6)
        output_file("test_vs_ideal.html")
        show(p)
