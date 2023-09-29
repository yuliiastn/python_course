import seaborn as sns

penguins = sns.load_dataset("penguins")

# 1. Displot (Distribution Plot):
# Use Case: Visualizing the distribution of a single numerical variable ('flipper_length_mm').
sns.displot(penguins, x="flipper_length_mm", kde=True)

# 2. Histplot (Histogram Plot):
# Use Case: Visualizing the distribution of a single numerical variable ('flipper_length_mm') using histograms.
sns.histplot(penguins, x="flipper_length_mm", bins=10)

# 3. Kdeplot (Kernel Density Plot):
# Use Case: Visualizing the distribution of a single numerical variable ('flipper_length_mm') using a kernel density estimate (KDE).
sns.kdeplot(penguins["flipper_length_mm"])

# 4. Ecdfplot (Empirical Cumulative Distribution Function Plot):
# Use Case: Visualizing the empirical cumulative distribution function (ECDF) of a single numerical variable ('flipper_length_mm').
sns.ecdfplot(data=penguins, x="flipper_length_mm")

# 5. Regplot (Regression Plot):
# Use Case: Visualizing the relationship between two numerical variables ('flipper_length_mm' and 'body_mass_g') and fitting a regression line.
sns.regplot(data=penguins, x="flipper_length_mm", y="body_mass_g")

# 6. Catplot (Categorical Plot):
# Use Case: Visualizing relationships between numerical ('flipper_length_mm') and one or more categorical variables ('species') using a scatterplot.
sns.catplot(data=penguins, x="flipper_length_mm", y="species", kind="strip")

# 7. Boxplot (Box Plot):
# Use Case: Visualizing the distribution of a numerical variable ('bill_length_mm') across different categories ('species').
sns.boxplot(data=penguins, x="species", y="bill_length_mm")

# 8. Violinplot (Violin Plot):
# Use Case: Combining a boxplot and KDE to visualize the distribution of a numerical variable ('bill_length_mm') across categories ('species').
sns.violinplot(data=penguins, x="species", y="bill_length_mm")
