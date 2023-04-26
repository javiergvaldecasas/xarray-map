import numpy as np
import folium
import matplotlib.pyplot as plt


def plot_folium(self, m, colormap='viridis', opacity=0.6, vmax=None, vmin=None):

    if vmax is None:
        vmax = self.values[:].max()
    if vmin is None:
        vmin = self.values[:].min()

    values = np.flipud(self.values[:].astype(float))
    values = (values - vmin) / (vmax - vmin)

    if 'latitude' in self.dims and 'longitude' in self.dims:
        latitude = self.latitude
        longitude = self.longitude
    elif 'lat' in self.dims:
        latitude = self.lat
        longitude = self.lon
    else:
        raise Exception('dimensions: latitude or lat ')


    img = folium.raster_layers.ImageOverlay(
            name="",
            image= values,
            bounds=[[float(latitude.min().values), float(longitude.min().values)],
                    [float(latitude.max().values), float(longitude.max().values)]],
            opacity=opacity,
            interactive=True,
            cross_origin=False,
            zindex=1,
            colormap=plt.get_cmap(colormap)
        )

    img.add_to(m)
    return img

