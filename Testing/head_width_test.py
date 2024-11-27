HEAD_WIDTH_VALUE = 0

# Suppressing warnings resulting from downgrading pandas to 1.5.3
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Core object
from tyssue import Sheet
# Simple 2D geometry
from tyssue import PlanarGeometry as geom
# Visualisation
from tyssue.draw import sheet_view

sheet = Sheet.planar_sheet_2d(
    'basic2D', # a name or identifier for this sheet
    nx=10, # approximate number of cells on the x axis
    ny=10, # approximate number of cells along the y axis
    distx=1, # distance between 2 cells along x
    disty=1 # distance between 2 cells along y
)
geom.update_all(sheet) # Updates the Geometry with the new Sheet Object

# Tidying up the displayed sheet
sheet.sanitize(trim_borders=True) #THIS DOESN'T WORK FOR SOME REASON
geom.update_all(sheet)

# Displaying the Sheet
import matplotlib.pyplot as plt
fig, ax = sheet_view(
    sheet,
    mode = "2D",
    edge = {"color": "dodgerblue", "width": 1, "head_width": HEAD_WIDTH_VALUE}
) # Use the sheetview object to display sheets, edge keyword is ysed to adjust some edge properties, see draw_specs in docs

fig.set_size_inches(8, 8)
plt.show()