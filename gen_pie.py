import matplotlib.pyplot as plt

sizes = [2, 10, 2, 4]

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'K2', 'K3', 'K4', 'K1'
explode = (0.0, 0.0, 0.0, 0.0)
colors = ['#a5a5a5', '#5b9bd5', '#ffc000', '#f28544']


def get_labels(label, value):
    return "{:s}\n{:d} hrs/week".format(label, value)

label_str = [get_labels( labels[i], sizes[i] ) for i in range(len(labels))]
print label_str

fig1, ax1 = plt.subplots()
#wedges, texts, autotexts = ax1.pie(sizes, autopct=lambda : get_labels(size, labels),
#                                  textprops=dict(color="w"))

#ax1.legend(wedges, ingredients,
#          title="Ingredients",
#          loc="center left",
#          bbox_to_anchor=(1, 0, 0.5, 1))

#plt.setp(autotexts, size=8, weight="bold")


#ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
wedges, texts = ax1.pie(sizes, explode=explode, labels=label_str,
        shadow=False, counterclock=False,
        wedgeprops={"edgecolor":"w",'linewidth': 1, 'linestyle': 'solid', 'antialiased': True},
        startangle=90,
        colors=colors,
        labeldistance=0.7)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
for t in texts:
    t.set_horizontalalignment('center')
    t.set_color( "w" )
plt.show()

