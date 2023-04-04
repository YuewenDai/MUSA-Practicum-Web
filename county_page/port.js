var map = L.map('map', {
    center: [36.848253, -76.364559],
    zoom: 13
  });


var Stamen_Terrain = L.tileLayer('http://{s}.basemaps.cartocdn.com/rastertiles/voyager_nolabels/{z}/{x}/{y}.png', {
    attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    subdomains: 'abcd',
    minZoom: 0,
    maxZoom: 20,
    ext: 'png'
  }).addTo(map);

var port14_data = './county_page/data/port_14_10.tif';
var altText = 'Portsmouth Landcover 2014.';
var latLngBounds = L.latLngBounds([[36.848253, -76.364559], [36.87, -76.32]]);

var imageOverlay = L.imageOverlay(port14_data, latLngBounds, {
    opacity: 0.8,
    alt: altText,
    interactive: true
}).addTo(map);
L.rectangle(latLngBounds).addTo(map);

