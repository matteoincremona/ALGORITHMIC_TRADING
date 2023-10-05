# 1° WAY
# Non-interactive visualization

import matplotlib.pyplot as plt
from plotly.offline import iplot

frame.price # data I want to display

plt.figure(figsize = (8,4), dpi = 200)
plt.plot(frame.price, color = 'blue', linewidth = 1.0)
plt.axhline(y = 30, color = 'grey', linestyle = '--', linewidth = 1)
plt.axhline(y = 70, color = 'grey', linestyle = '--', linewidth = 1)
plt.xlabel("xTitle")
plt.ylabel("yTitle")
plt.title("Title")
plt.show();

# 2° WAY
# Interactive visualization

import matplotlib.pyplot as plt
from plotly.offline import iplot
import cufflinks as cf

# Display only ONE variable

frame.price # data I want to display

cf.go_offline() # will make cufflinks offline
cf.set_config_file(offline = False, world_readable = True)
frame.price.iplot(kind = "line", color = "black", theme = "white", title = "Title", xTitle = "xTitle", yTitle = "yTitle")

# Display TWO one variable in the same graph

frame.price # data I want to display
frame.SMA200 # data I want to display

cf.go_offline() # will make cufflinks offline
cf.set_config_file(offline = False, world_readable = True)
graph = frame[["price", "SMA200"]]
graph.iplot(kind = "line", color = ["black", "red"], theme = "white", title = "Title", xTitle = "xTitle", yTitle = "yTitle")

