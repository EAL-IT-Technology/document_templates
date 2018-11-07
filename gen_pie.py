import matplotlib.pyplot as plt

# the only values to change
sizes = [2, 10, 2, 4]
fig_name = "pie.png"

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'K2', 'K3', 'K4', 'K1'
explode = (0.0, 0.0, 0.0, 0.0)
colors = ['#a5a5a5', '#5b9bd5', '#ffc000', '#f28544']


def get_labels(label, value):
    return "{:s}\n{:d} hrs/week".format(label, value)

label_str = [get_labels( labels[i], sizes[i] ) for i in range(len(labels))]
print label_str

fig1, ax1 = plt.subplots()
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

# use this to show, if not saving
#plt.show()

print "image saved {:s}".format( fig_name )
plt.savefig(fig_name, bbox_inches='tight')
